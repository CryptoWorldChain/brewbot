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


class CcksEncrySign(object):
    def __init__(self):
        """
        keystore对照表：
        tx_keystore ： 59514f8d87c964520fcaf515d300e3f704bf6fcb
        """
        self.tx_keystore = "59514f8d87c964520fcaf515d300e3f704bf6fcb"
        self.ctx = ska.Ska(EC_256R1)

    def _join_string(self, a, b):
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
        print "my keystore is: ======>>\n", kp
        print("-----------------------------------")
        req = json_format.Parse(json_data, tximpl_pb2.ReqCreateMultiTransaction())
        print "create multi transaction is:======>>\n", req
        print("-----------------------------------")
        tx = tx_helper.impl2tx(req.transaction)

        tx.txBody.ClearField("signatures")
        print "multi transaction is: ======>>\n", tx
        print("-----------------------------------")
        bodyBytes = tx.txBody.SerializeToString()
        with self.ctx.txn() as txn:
            sign = tx.txBody.signatures.add()
            sign.signature = self.ctx.ecsign(txn, HASH_SHA256, SIGN_CWV, kp.pri(), bodyBytes)

        itx = tx_helper.tx2impl(tx)
        req.transaction.CopyFrom(itx)
        print "pre-send req is: ======>>\n", req
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
        url = self._join_string(api_url, api_path)
        try:
            res = requests.post(url=url, headers=headers, data=data, verify=False)
            return res
        except Exception as e:
            print("请求异常:{a}".format(a=e))
    
    def data_2_json(self, data):
        """
        把数据转换为json格式
        """
        my_data = json.dumps(data)
        return my_data
    
    def concurrent_transactions(self, api_url, api_path, json_data_1, json_data_2):
        """
        采用并发的方式来模拟，双花的交易测试场景
        | api_url（请求ip和端口号）   | api_path （接口路径地址） | json_data_1 （给用户A的交易数据）| json_data_2 （给用户B的交易数据）|
        """
        my_thread = []
        first_tx = self.deal_transaction(api_url, api_path, json_data_1)
        second_tx = self.deal_transaction(api_url, api_path, json_data_2)
        t1 = threading.Thread(target=first_tx)
        t2 = threading.Thread(target=second_tx)
        my_thread.append(t1)
        my_thread.append(t2)
        for i in my_thread:
            i.start()





if __name__ == "__main__":
    url = 'http://172.18.92.107:38000'
    path = "/cks/api/pbmtx.do"
    data_a = """
    {
                         "transaction": {
                                "txBody": {
                              "inputs": [
                              {
                                   "nonce": 1,
                                   "address": "19e51734fe9672b9698c623214b7cdfb0c19bea0",
                                   "amount": "20"
                              }
                               ],
                              "outputs": [
                              {
                                  "address": "b0243cd9e6cc356e864efcbdb6bbb193f116f184",
                                  "amount": "10"
                               },
                              {
                                  "address": "3f35b456edd05e67090fe46b005f62257e32f98e",
                                  "amount": "10"
                             }
                             ],
                             "data": "aa",
                              "timestamp": "1545367904324"
                           }
                        }
                   }
    """
    c = CcksEncrySign()
    a = c.deal_transaction(api_url=url, api_path=path, json_data=data_a)
    print(a)