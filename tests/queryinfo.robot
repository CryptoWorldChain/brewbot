***Settings***
Library    Collections
Library    RequestsLibrary
Library    String

Resource   ../res/vers.robot


Suite Setup    InitSession

***Test Cases***

001     [Documentation]     获取信息
    ${m}     Get Account Info  e0c7d2a75ccd61af87aaa818cdcb2246706363a1  server=REMOTE
    Log To Console  account:${m}
    ${m}     Get Block By Number  0  server=REMOTE
    Log To Console  block0:${m}
    ${txhash}    Set Variable  ${m["header"]["txHashs"]}[0]
    Log To Console     txhash=${txhash}
    ${m}     Get Tx By Hash  ${txhash}    transaction  txHash     server=REMOTE
    Log To Console     get tx by hash=${m}
    ${m}     Get Last Block    server=REMOTE
    Log To Console  last block:${m}  stream=STDOUT  no_newline=False
    ${m}     Get Summary    server=REMOTE
    Log To Console  summary:${m}  stream=STDOUT  no_newline=False
