# -*- coding:utf-8 -*-

import os, codecs
import tx_helper
from google.protobuf import json_format
import tximpl_pb2
import tx_pb2
from ctypes import *
import ska
from ska_defines import *
import json
import re
import requests
import json
import threading


class SkaSignTool(object):
    def __init__(self):
        """
        keystore对照表：
        tx_keystore ： 59514f8d87c964520fcaf515d300e3f704bf6fcb
        """
        self.tx_keystore = "59514f8d87c964520fcaf515d300e3f704bf6fcb"
        self.ctx = ska.Ska(EC_256R1)

    def __url_combine(self, a, b):
        res_str = a + b
        print(res_str)
        return res_str
    
    def deal_transaction(self, api_url, api_path, json_data):
        """
        交易接口的请求数据处理:
        | api_url（请求ip和端口号）   | api_path （接口路径地址） | json_data （请求数据为json数据，用“”“引起来） |
        """
        print(json_data)
        json_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'keystore1.json')
        kp = tx_helper.loadkeystore(self.ctx, json_path)
        print ("my keystore is: ======>>\n", kp)
        print("-----------------------------------")
        req = json_format.Parse(json_data, tximpl_pb2.ReqCreateMultiTransaction())
        print ("create multi transaction is:======>>\n", req)
        print("-----------------------------------")
        tx = tx_helper.impl2tx(req.transaction)

        tx.txBody.ClearField("signatures")
        print ("multi transaction is: ======>>\n", tx)
        print("-----------------------------------")
        bodyBytes = tx.txBody.SerializeToString()
        with self.ctx.txn() as txn:
            sign = tx.txBody.signatures.add()
            sign.signature = self.ctx.ecsign(txn, HASH_SHA256, SIGN_CWV, kp.pri(), bodyBytes)

        itx = tx_helper.tx2impl(tx)
        req.transaction.CopyFrom(itx)
        print ("pre-send req is: ======>>\n", req)
        print("-----------------------------------")
        url_mtx = self._join_string(api_url, api_path)
        resp = tx_helper.post(url_mtx, req, tximpl_pb2.RespCreateTransaction())
        print(resp.txHash)
        return resp.txHash
        # return resp
        # print resp.txHash
        
    def bc_post(self, api_url, api_path, data, interface_word=None, headers=None):
        """
        发送区块链接口post请求
        | api_url（请求ip和端口号）   | api_path （接口路径地址）  | data （请求体数据）  | interface_word (返回结果关键字,可以为空，为空时返回整个responses)  |
        """
        url = self.__url_combine(api_url, api_path)
        try:
            res = requests.post(url=url, headers=headers, data=data, verify=False)
            return res
        except Exception as e:
            print("请求异常:{a}".format(a=e))
    
    def bc_sign_dropnode(self, prikey, nid, bcuids):
        b = codecs.encode(','.join(bcuids),'utf-8')
        r = None
        with self.ctx.txn() as txn:
            h = self.ctx.sha2(txn, b)
            r = self.ctx.ecsign(txn, HASH_SHA256, SIGN_CWV, prikey, h)
            r = codecs.encode(r, 'hex')
            r = codecs.decode(r, 'utf-8')
        j = {"drop_bcuids":bcuids, "sign":r, "nid":nid}
        return json.dumps(j)    

    def data_2_json(self, data):
        """
        把数据转换为json格式
        """
        my_data = json.dumps(data)
        return my_data

    def ctx(self):
        return self.ctx;    
    


if __name__ == "__main__":
    
    print(ks)
    pri = codecs.decode('1a7264ae5078f2a0c5b5e567457bbcedf1bdc3263ad32576c9a3c512c386ed6f', 'hex')
    bcuids = ["a", "b", "c"]
    skatool = SkaSignTool()
    msg = skatool.bc_sign_dropnode(pri, "dpos", bcuids)
    print(msg)
