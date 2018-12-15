
*** Variables ***

#服务器及端口
${BASE_URL}         http://localhost:8000


#访问的路径
${Base_Path}         /cks

#访问的路径
${API_Path}         ${Base_Path}/api

##获取最新的高度
${GetLatestBlock}   ${API_Path}/pbglb.do


#根据hash获取交易
${GetTxByHash}      ${API_Path}/pbgtx.do

##获取用户余额
${GetAccountCoin}   ${API_Path}/pbgac.do



#打块时间
${Block_Time}           5s



#生成测试交易
${TST_Gen_Tx_data}       ${Base_Path}/tst/pbltp.do
#检查测试交易数量
${TST_GetTestTxCount}       ${Base_Path}/tst/pbltr.do
#发送一笔模拟交易
${TST_SendOneTx}       ${Base_Path}/tst/pblte.do




#发送一笔模拟交易
${TST_Union_Send}       ${Base_Path}/tst/pbtua.do


#每次生成多少个测试交易
${arg_gentxnum}       3

*** Keywords ***
InitSession
    Create Session      LOCAL       ${BASE_URL}
    Create Session      REMOTE      ${BASE_URL}



FetchInfo
    [Arguments]    ${method}   ${resultcolumn}
    ${resp}=    Get Request     LOCAL      ${method}
    ${body}=  To Json  ${resp.content}
    LOG         ${body['${resultcolumn}']}
    [return]    ${body['${resultcolumn}']}



PostData
    [documentation]   发送数据
    [Arguments]    ${method}    ${data}    ${resultcolumn}
    LOG            postdata=${data}
    ${resp}=    Post Request     LOCAL      ${method}     data=${data}
    ${body}=  To Json  ${resp.content}
    LOG         ${body}
    [return]    ${body['${resultcolumn}']}


GenerateTestData
    [Arguments]    ${txcount}=1000
    ${resp}=    Post Request     LOCAL      ${TST_Gen_Tx_data}     data={"defaultTx":${txcount}}
    ${body}=  To Json  ${resp.content}
    LOG         ${body}
    [return]    ${body['retcode']}










