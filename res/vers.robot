
*** Variables ***

#服务器及端口
${LOCAL_URL}        http://127.0.0.1:8000
${REMOTE_URL}         http://172.16.211.2:38000


#访问的路径
${Base_Path}         /cks

#API访问的路径
${API_Path}         ${Base_Path}/api

#TST访问的路径
${TST_Path}         ${Base_Path}/tst

####账户相关接口####

##账户相关
#获取用户余额(GetAccountImpl)
${APIGetAccountInfo}      ${API_Path}/pbgac.do
#获取账户存储(GetAccountStorageImpl)
${APIGetAccountStore}     ${API_Path}/pbqas.do
#获取ECR721信息(GetCryptoTokenInfoImpl)
${APIGetCrytoInfo}        ${API_Path}/pbqii.do
#获取ECR20信息(GetTokenInfoImpl)
${APIGetTokenInfo}        ${API_Path}/pbqio.do
#获取ECR20列表(GetTokenListImpl)
${APIGetTokenList}        ${API_Path}/pbqic.do


##区块相关
#根据hash获取Block(GetBlockByHashImpl)
${APIGetBlockByHash}      ${API_Path}/pbgbh.do
#根据高度获取Block(GetBlockByNumberImpl)
${APIGetBlockByNum}       ${API_Path}/pbgbn.do
#根据交易获取区块(GetBlockByTxHashImpl)
${APIGetBlockByTxHash}    ${API_Path}/pbgba.do
#获取区块(GetBlockImpl)
${APIGetBlockImpl}        ${API_Path}/pbgba.do
#获取区块信息(GetSummaryImpl)
${APIGetBlockInfo}        ${API_Path}/pbbio.do
#根据高度获取区块列表(GetBlocksByNumberImpl)
${APIGetBlocksByNum}      ${API_Path}/pbgbs.do
#获取区块存储(GetBlockStoreByNumberImpl)
${APIGetBlockStoreByNum}  ${API_Path}/pbgbt.do
#获取最新的区块高度(GetLastBlockImpl)
${APIGetLatestBlock}      ${API_Path}/pbglb.do

#获取概要(GetSummaryImpl)
${APIGetSummary}          ${API_Path}/pbsum.do


##交易相关
#根据hash获取交易(GetTxByTxHashImpl)
${APIGetTxByHash}         ${API_Path}/pbgtx.do
#保存交易SaveMultiTransactionImpl
${APISaveMultiTx}         ${API_Path}/pbmtx.do


####测试相关接口####

##Load测试
##主链币
#生成测试交易(TransactionLoadTestPerImpl)
${TSTGenTxdata}           ${TST_Path}/pbltp.do
#检查测试交易数量(TransactionLoadTestPerResultImpl)
${TSTGetTestTxCount}      ${TST_Path}/pbltr.do
#发送一笔模拟交易(TransactionLoadTestExecImpl)
${TSTSendOneTx}           ${TST_Path}/pblte.do


##主链币交易
#创建联合账户(CreateUnionAccountSample)
${TSTCreateUnion}         ${TST_Path}/pbtca.do
#普通账户转账交易(TransactionSampleImpl)
${TSTTxSend}              ${TST_Path}/pbstt.do
#联合账户转账交易(UnionAccountTransactionSample)
${TSTUnionSend}           ${TST_Path}/pbtua.do

##ERC Token交易
#创建Token(CreateTokenTransactionSample)
${TSTCreateToken}         ${TST_Path}/pbtct.do
#Token Burn
${TSTBurnToken}           ${TST_Path}/pbbto.do
#Token增发(MintTokenTransactionSample)？
${TSTMintToken}           ${TST_Path}/pbmto.do
#普通账户ERC20交易(TokenTransactionSample)
${TSTTokenSend}           ${TST_Path}/pbtoo.do
#ERC20联合账户转账交易(UnionAccountTokenTransactionSample)
${TSTUnionTokenSend}      ${TST_Path}/pbtut.do

##ECR721 加密币交易
#创建Crypto(CreateCryptoTokenTransactionSample)
${TSTCreateCrypto}        ${TST_Path}/pbtco.do
#普通账户ERC721交易(CryptoTransactionSample)
${TSTCryptoSend}          ${TST_Path}/pbtro.do

#创建合约(TransactionCreateContract)
${TSTCreateContract}      ${TST_Path}/pbtcc.do
#执行合约(TransactionCallContract)
${TSTCallContract}        ${TST_Path}/pbtec.do


####设置####
#打块时间
${Block_Time}           5s

#每次生成多少个测试交易
${arg_gentxnum}       3000

#默认服务器，当没有server参数时，Post Data和Fatch Info默认链接的服务器名称
${Default_Server}     REMOTE


#for test
${Vers_Path}     ${CURDIR}

*** Keywords ***
InitSession
    Create Session      LOCAL       ${LOCAL_URL}
    Create Session      REMOTE      ${REMOTE_URL}


Post Data
    [Documentation]    发送请求
    [Arguments]        ${method}    ${data}     @{retfields}       ${server}=${Default_Server}      
    Log                postdata=${data}
    ${resp}            Post Request  ${server}  ${method}  data=${data}
    ${body} =          To Json       ${resp.content}
    Log                body=${body}
    ${ret} =           Set Variable  ${body}
    :FOR    ${item}    IN    @{retfields}
    \       ${ret} =   Set Variable  ${ret["${item}"]}
    [Return]           ${ret}

Fetch Info
    [Documentation]    发送请求,无Data
    [Arguments]        ${method}    @{retfields}       ${server}=${Default_Server} 
    ${resp}            Post Data  ${method}  None  @{retfields}  server=${server}
    [Return]           ${resp}

Post Data Local
    [Documentation]     发送数据到LOCAL
    [Arguments]        ${method}    ${data}    @{retfields}
    ${ret}             Post Data    ${method}    ${data}    @{retfields}
    [Return]           ${ret} 

Post Data Remote
    [Documentation]     发送数据到LOCAL
    [Arguments]        ${method}    ${data}    @{retfields}
    ${ret}             Post Data    ${method}    ${data}    @{retfields}    server=REMOTE
    [Return]           ${ret} 

Get Account Info
    [Documentation]    获取账户信息
    [Arguments]        ${address}    @{retfields}     ${server}=${Default_Server} 
    ${resp}             Post Data    ${APIGetAccountInfo}     {"address":"${address}"}    @{retfields}    server=${server}
    [Return]           ${resp}

#TODO get account store

Get Crypto Info
    [Documentation]    获取加密币信息
    [Arguments]        ${symbol}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetCrytoInfo}    {"symbol":"${symbol}"}    @{retfields}    server=${server}
    [Return]           ${resp}

Get Token Info
    [Documentation]    获取Token信息
    [Arguments]        ${token}    ${address}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetTokenInfo}    {"token":"${token}", "address":"${address}"}    @{retfields}    server=${server}
    [Return]           ${resp}

Get Token List
    [Documentation]    获取Token列表
    [Arguments]        ${token}    ${address}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetTokenList}    {"token":"${token}", "address":"${address}"}    @{retfields}    server=${server}
    [Return]           ${resp}

Get Block By Hash
    [Documentation]    通过区块Hash查询区块
    [Arguments]        ${hash}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetBlockByHash}    {"hash":"${hash}"}    @{retfields}    server=${server}
    [Return]           ${resp}

Get Block By Number
    [Documentation]    通过区块高度查询区块
    [Arguments]        ${number}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetBlockByNum}    {"number":"${number}"}    @{retfields}    server=${server}
    [Return]           ${resp}

Get Block By Tx Hash
    [Documentation]    通过交易的Hash查询区块
    [Arguments]        ${hash}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetBlockByTxHash}    {"hash":"${hash}"}    @{retfields}    server=${server}
    [Return]           ${resp}

#TODO Get Block

Get Summary
    [Documentation]    获取概要
    [Arguments]        @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetSummary}    data=None    server=${server}
    [Return]           ${resp}

Get Last Block
    [Documentation]    获取最新区块
    [Arguments]        @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetLatestBlock}    data=None    server=${server}    
    [Return]           ${resp}

Get Tx By Hash
    [Documentation]    通过Hash查询交易
    [Arguments]        ${hash}    @{retfields}     ${server}=${Default_Server} 
    ${resp}            Post Data    ${APIGetTxByHash}    {"hash":"${hash}"}    @{retfields}    server=${server}
    [Return]           ${resp}
    
#TODO save multi transaction

GenerateTestData
    [Arguments]      ${txcount}=1000    ${server}=${Default_Server} 
    ${resp}          Post Data  ${TSTGenTxdata}  {"defaultTx":${txcount}}  retcode  server=${server}
    [return]         ${resp}

