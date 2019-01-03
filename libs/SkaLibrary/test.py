a = {
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

new_a = {key:value for key,value in a.items() if key is "transaction"}
print(new_a)




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


class CcksEncrySign(object):
    def __init__(self):
        """
        keystore对照表：
        tx_keystore ： 59514f8d87c964520fcaf515d300e3f704bf6fcb
        """
        self.tx_keystore = "59514f8d87c964520fcaf515d300e3f704bf6fcb"

    def deal_transaction(self, json_data):
        """
        交易接口的请求数据处理
        """
        ctx = ska.Ska(EC_256R1)
        json_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'keystore1.json')
        kp = tx_helper.loadkeystore(ctx, json_path)
        print(kp)
        print("1111111111111")
        # 截取想要的数据段
        my_dict = {key:value for key,value in json_data.items() if key is "transaction"}
        print(my_dict) 
        print("22222222222222")
        # 对单引号进行匹配转换
        send_data = re.sub("'", "\"", str(my_dict))
        print(send_data) 
        req = json_format.Parse(send_data, tximpl_pb2.MultiTransactionImpl())    # MultiTransactionImpl
        print("33333333333333")
        print("create multi transaction", req)
        tx = tx_helper.impl2tx(req)
        
        tx.txBody.ClearField("signatures")
        print("multi transaction", tx)
        bodyBytes = tx.txBody.SerializeToString()
        with ctx.txn() as txn:
            sign = tx.txBody.signatures.add()
            sign.signature = ctx.ecsign(txn, HASH_SHA256, SIGN_CWV, kp.pri(), bodyBytes)
        itx = tx_helper.tx2impl(tx)
        req.CopyFrom(itx)
        return json_format.MessageToJson(req)
        
        # print("pre-send req", req)
        # resp = tx_helper.post(url_mtx, req, tximpl_pb2.RespCreateTransaction())
        # print("resp", resp)
        # return resp



if __name__ == "__main__":
    data_a = {
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

    # new_a = {key:value for key,value in data_a.items() if key is "transaction"}
    # print(new_a)

    c = CcksEncrySign()
    a = c.deal_transaction(data_a)
