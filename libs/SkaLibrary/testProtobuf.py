import os, codecs
import tx_helper
from google.protobuf import json_format
import tximpl_pb2
import tx_pb2
from ctypes import *
import ska
from ska_defines import *

ctx = ska.Ska(EC_256R1)
#TODO data may be not hex

url_gtx = 'http://172.18.92.101:38000/cks/api/pbgtx.do'
url_mtx = 'http://172.18.92.101:38000/cks/api/pbmtx.do'

js = """
{
    "transaction": {
        "txBody": {
            "inputs": [
                {
                    "nonce": 2,
                    "address": "59514f8d87c964520fcaf515d300e3f704bf6fcb",
                    "amount": "100"
                }
            ],
            "outputs": [
                {
                    "address": "f192c303b6aac4b06ec8fae6473a98060fb7aaa3",
                    "amount": "100"
                }
            ],
            "data": "aa",
            "timestamp": "1545367904324"
        }
    }
}
"""

addr = 'eb55417992228cae6a521587bf25bfc88a3e9c45'
pri = 'a1925b83945365b610f5d771380b7c98ac88e4ca20754abf5228b9b20f92b7ae'

reqTxByHash = tximpl_pb2.ReqGetTxByHash()
reqTxByHash.hash = '36cd4830862d59e242d761979f986a0b7a2310b6a84fab8e6ea3645135d6bf39'
respTxByHash = tx_helper.post(url_gtx, reqTxByHash, tximpl_pb2.RespGetTxByHash()) 

# print("resp: {}".format(json_format.MessageToJson(respTxByHash))) 

# mtx = tx_helper.impl2tx(respTxByHash.transaction)
# mtx.txBody.ClearField("signatures")
# txBodyBytes = mtx.txBody.SerializeToString()

# signBytes = codecs.decode(respTxByHash.transaction.txBody.signatures[0].signature,'hex')

# with ctx.txn() as txn:
#     checkrest = ctx.ecverify(txn, HASH_SHA256, SIGN_CWV, '', txBodyBytes, signBytes)
#     print("tx check result:{}".format(checkrest))

# trans
json_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'keystore1.json')
kp = tx_helper.loadkeystore(ctx, json_path)
req = json_format.Parse(js, tximpl_pb2.ReqCreateMultiTransaction())
print "create multi transaction:\n", req
print("-----------------------------------")
tx = tx_helper.impl2tx(req.transaction)

tx.txBody.ClearField("signatures")
print "multi transaction:\n", tx
print("-----------------------------------")
bodyBytes = tx.txBody.SerializeToString()
with ctx.txn() as txn:
    sign = tx.txBody.signatures.add()
    sign.signature = ctx.ecsign(txn, HASH_SHA256, SIGN_CWV, kp.pri(), bodyBytes)

itx = tx_helper.tx2impl(tx)
req.transaction.CopyFrom(itx)
print "pre-send req:\n", req
print("-----------------------------------")
resp = tx_helper.post(url_mtx, req, tximpl_pb2.RespCreateTransaction())
print "resp:\n", resp




