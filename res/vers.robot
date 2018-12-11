
*** Variables ***

#服务器及端口
${BASE_URL}         http://localhost:8000


#访问的路径
${Base_Path}         /cks

#访问的路径
${API_Path}         ${Base_Path}/api

##获取最新的高度
${GetLatestBlock}   ${API_Path}/pbglb.do


#打块时间
${Block_Time}           5s


#生成测试交易
${Gen_Tx_data}       ${Base_Path}/tst/pbltp.do
#检查测试交易数量
${GetTestTxCount}       ${Base_Path}/tst/pbltr.do
#每次生成多少个测试交易
${arg_gentxnum}        100

*** Keywords ***
InitSession
    Create Session      LOCAL       ${BASE_URL}
    Create Session      REMOTE      ${BASE_URL}



FetchInfo
    [Arguments]    ${arg1}   ${arg2}
    ${resp}=    Get Request     LOCAL      ${arg1}
    ${body}=  To Json  ${resp.content}
    LOG         ${body['${arg2}']}
    [return]    ${body['${arg2}']}



GenerateTestData
    [Arguments]    ${txcount}=1000
    ${resp}=    Post Request     LOCAL      ${Gen_Tx_data}     data={"defaultTx":${txcount}}
    ${body}=  To Json  ${resp.content}
    LOG         ${body}
    [return]    ${body['retcode']}










