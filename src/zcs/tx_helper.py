import os
import codecs
import struct
from ctypes import *
import json

import requests

from google.protobuf import json_format
from gens import tximpl_pb2
from gens import tx_pb2
from gens import oentity_pb2

import ska
from ska_defines import *


class PyKeyPair(object):

    def __init__(self, pub, pri, addr, bcuid):
        self.__pub = pub
        self.__pri = pri
        self.__addr = addr
        self.__bcuid = bcuid

    def __str__(self):
        return '(bcuid:{}, addr:{}, pri:{}, pub:{})'.format(
            self.__bcuid, self.__addr, codecs.encode(self.__pri, 'hex'), codecs.encode(self.__pub, 'hex')
        )

    def pub(self):
        return self.__pub

    def pri(self):
        return self.__pri

    def addr(self):
        return self.__addr

    def bcuid(self):
        return self.__bcuid


def int2bytes(n_):
    _fmts = ['>Q', '>QQ', '>QQQ', '>QQQQ']
    _arr = []
    if n_ > 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF:
        raise ValueError('n out of length.')
    while n_ > 0:
        _arr.append(n_ & 0xFFFFFFFFFFFFFFFF)
        n_ = n_ >> 64
    if len(_arr) == 0:
        return '\0'
    _s = struct.pack(_fmts[len(_arr)-1], *_arr[::-1])
    _bb = bytearray(_s)

    _cnt = 0
    for b in _bb:
        if b == 0:
            _cnt = _cnt+1
        else:
            break
    return _s[_cnt:]


def bytes2int(b):
    _fmts = ['>Q', '>QQ', '>QQQ', '>QQQQ']
    _prefix = [b'',b'\0',b'\0\0',b'\0\0\0',b'\0\0\0\0',b'\0\0\0\0\0',b'\0\0\0\0\0\0', b'\0\0\0\0\0\0\0']
    bl = len(b)
    if bl == 0 or bl > 32:
        raise ValueError("b out of length.")

    l = int((bl+7)/8)
    a = l*8-bl
    str = _prefix[a] + b
    i = l-1
    n2 = struct.unpack(_fmts[i], str)
    n3 = 0
    for nn in n2:
        n3 = n3 + (nn << (i*64))
        i = i-1
    return n3


def impl2tx(impl):
    """convert from tximpl_pb2.MultiTransactionImpl to tx_pb2.MultiTransaction"""
    _txBody = impl.txBody
    #TODO set signs

    _mtx = tx_pb2.MultiTransaction()
    _mtx.txHash = impl.txHash

    # MultiTransactionBody
    # body inputs
    for oinput in _txBody.inputs:
        minput = _mtx.txBody.inputs.add()
        minput.nonce = oinput.nonce
        minput.address = codecs.decode(oinput.address, 'hex')
        minput.amount = int2bytes(int(oinput.amount,10))
        minput.token = oinput.token
        minput.symbol = oinput.symbol
        minput.cryptoToken = codecs.decode(oinput.cryptoToken, 'hex')
    # body outputs
    for ooutput in _txBody.outputs:
        moutput = _mtx.txBody.outputs.add()
        moutput.address = codecs.decode(ooutput.address, 'hex')
        moutput.amount = int2bytes(int(ooutput.amount))
        moutput.symbol = ooutput.symbol
        moutput.cryptoToken = codecs.decode(ooutput.cryptoToken, 'hex')
    # body exdata
    _mtx.txBody.exdata = codecs.decode(_txBody.exdata, 'hex')
    # body signatures
    for osign in _txBody.signatures:
        msign = _mtx.txBody.signatures.add()
        msign.signature = codecs.decode(osign.signature, 'hex')
    # body delegate
    for odelegate in _txBody.delegate:
        mdelegate = _mtx.txBody.delegate.add()
        mdelegate = codecs.decode(odelegate, 'hex')
    # body data
    _mtx.txBody.data = codecs.decode(_txBody.data, 'hex')
    # body timestamp
    _mtx.txBody.timestamp = _txBody.timestamp
    # body type
    _mtx.txBody.type = _txBody.type

    ## MultiTransactionNode txNode
    # _mtx.txNode.node = impl.node.node
    # if impl.node is not None and impl.node.address is not None:
    #     _mtx.txNode.address = codecs.decode(impl.node.address, 'hex')
    # _mtx.txNode.bcuid = impl.node.bcuid
    return _mtx


def tx2impl(tx):
    """convert from tx_pb2.MultiTransaction to tximpl_pb2.MultiTransactionImpl """
    body = tx.txBody
    m = tximpl_pb2.MultiTransactionImpl()
    m.txHash = tx.txHash
    m.status = tx.status
    if "D" == tx.status:
        m.result = codecs.encode(tx.result, 'hex')
    elif len(tx.result) != 0:
        m.result = codecs.encode(tx.result, "utf-8")
    m.txBody.type = tx.txBody.type
    m.txBody.data = codecs.encode(tx.txBody.data, 'hex')
    for odelegate in tx.txBody.delegate:
        dlg = m.txBody.delegate.add()
        dlg.delegate = codecs.encode(odelegate.delegate, 'hex')
    m.txBody.exdata = codecs.encode(tx.txBody.exdata, 'hex')
    for oinput in tx.txBody.inputs:
        minput = m.txBody.inputs.add()
        minput.address = codecs.encode(oinput.address, 'hex')
        minput.amount = str(bytes2int(oinput.amount))
        minput.cryptoToken = codecs.encode(oinput.cryptoToken, 'hex')
        minput.nonce = oinput.nonce
        minput.symbol = oinput.symbol
        minput.token = oinput.token
    for ooutput in tx.txBody.outputs:
        moutput = m.txBody.outputs.add()
        moutput.address = codecs.encode(ooutput.address, 'hex')
        moutput.amount = str(bytes2int(ooutput.amount))
        moutput.cryptoToken = ooutput.cryptoToken
        moutput.symbol = ooutput.symbol
    for osign in tx.txBody.signatures:
        msign = m.txBody.signatures.add()
        msign.signature = codecs.encode(osign.signature, 'hex')
    m.txBody.timestamp = tx.txBody.timestamp
    #TODO copy node
    return m


def loadkeystore(ctx, filepath):
    """load CWV keystore json file"""
    ks = None
    pykp = None
    with open('keystore1.json', 'r') as kfile:
        ks = json.load(kfile)
    ciphertext = codecs.decode(ks["cipherText"], 'hex')
    pwd = codecs.encode(ks["pwd"], 'ascii')
    iv = codecs.decode(ks["cipherParams"]["iv"], 'hex')
    dklen = int(ks["params"]["dklen"])
    c = int(ks["params"]["c"])
    l = int(ks["params"]["l"])
    salt = codecs.decode(ks["params"]["salt"], 'hex')
    with ctx.txn() as txn:
        source = pwd+salt
        ivsz = int(c/8)
        keysz = int(dklen/8)
        needlen = keysz+ivsz
        key = create_string_buffer(needlen)
        offset = 0
        while 1 == 1:
            md5 = ctx.md5(txn, source)
            hashlen = len(md5)
            if needlen < hashlen:
                hashlen = needlen
            key[offset:offset+hashlen] = md5[0:hashlen]
            offset = offset + hashlen
            needlen = needlen-hashlen
            if needlen == 0:
                break
            source = md5+pwd+salt
        ctx.cipherreset(txn, CIPHER_AES_256_CBC, CIPHER_PADDING_NONE, key[:keysz], key[keysz:keysz+ivsz])
        plant = ctx.decrypt(txn, ciphertext)
        kv = oentity_pb2.KeyStoreValue()
        kv.ParseFromString(plant[:l])
        pubk = kv.pubkey.replace(' ', '').replace('\n', '')
        prik = kv.prikey.replace(' ', '').replace('\n', '')
        print("pub:{}, pri:{}, publen:{}, prilen:{}".format(pubk, prik, len(pubk), len(prik)))
        pubk = codecs.decode(pubk, 'hex')
        prik = codecs.decode(prik, 'hex')
        prik = prik[::-1]
        pubk = pubk[::-1]
        x = pubk[32:]
        y = pubk[:32]
        pubk = b'\x04'+x+y
        pykp = PyKeyPair(pubk, prik, codecs.encode(kv.address,'ascii'), codecs.encode(kv.bcuid, 'ascii'))
    return pykp

def post(url, req, resp):
    """port req to url, resp is response Object"""
    jreq = json_format.MessageToJson(req)
    r = requests.post(url=url, data=jreq)
    return json_format.Parse(r.content, resp)
    pass


if __name__ == '__main__':
    implJson = """
{
    "txHash": "a1d7e55b33b579dff7c6161e04bd9161c38af5d3effa7cb11f5229a01df887c0",
    "txBody": {
        "inputs": [
            {
                "nonce": 0,
                "amount": "9800000000000000000000000000"
            },
            {
                "nonce": 0,
                "amount": "97900000000000000000000000",
                "token": "CWS"
            }
        ],
        "outputs": [
            {
                "address": "e0c7d2a75ccd61af87aaa818cdcb2246706363a1",
                "amount": "9800000000000000000000000000"
            },
            {
                "address": "e0c7d2a75ccd61af87aaa818cdcb2246706363a1",
                "amount": "97900000000000000000000000"
            }
        ],
        "signatures": [
            {
                "signature": "80c052f6bb9544929a66a0e4b279e0d3f40f87112b28ff1dfb79f289f8c4acf16a8dcb89f70ef72c05d4b6be0d5c94057151f8a5987e92067151ed765db3eb60e0c7d2a75ccd61af87aaa818cdcb2246706363a169a713ad12f5f4ca57429be8a40dda3bf08c524bb7f66125cc095870176cd43b1ca7bea50928f516b6754658a791a0934ba326a104dd45c0ca4b380c0f7f25c9"
            },
            {
                "signature": "aac052f6bb9544929a66a0e4b279e0d3f40f87112b28ff1dfb79f289f8c4acf16a8dcb89f70ef72c05d4b6be0d5c94057151f8a5987e92067151ed765db3eb60e0c7d2a75ccd61af87aaa818cdcb2246706363a169a713ad12f5f4ca57429be8a40dda3bf08c524bb7f66125cc095870176cd43b1ca7bea50928f516b6754658a791a0934ba326a104dd45c0ca4b380c0f7f25aa"
            }				
        ],
        "data": "0a010012010018062214f4fcdf9e5603a5375f9fe0c8bba951e085cdcdfc22148502208b949e7c08acb4c2f1aef06caa39891a7922143eb9c18610e35c7f039d3591a15f967d98b3d5b822143db85d2797ddc2a4802e9fff1a0232b0bbf06c8a2214ad081e743aa6174e4d2609fc8b0985718e77082d2214b16657a7bf154da2aab8dc9a3484e9413c165ff1",
        "timestamp": 1539854885522,
        "type": 2
    },
    "node": {},
    "status": "D"
}
    """
    tximpl = json_format.Parse(implJson, tximpl_pb2.MultiTransactionImpl())
    tx = impl2tx(tximpl)
    # tx.txBody.ClearField("signatures")
    print(json_format.MessageToJson(tx))
    tximpl2 = tx2impl(tx)
    print(json_format.MessageToJson(tximpl))
    print(json_format.MessageToJson(tximpl2))
    ctx = ska.Ska(EC_256R1)
    pykp = loadkeystore(ctx, 'keystore1.json')
    print("kp", str(pykp))

    del ctx


