
*** Settings ***
Library        Collections
Library        RequestsLibrary
Library        String

Resource      ../res/vers.robot



Suite Setup    InitSession


*** Keywords ***

SendAndCheckTx
    [Arguments]    ${wait_times}=100
        ${txhash} =     FetchInfo      ${TST_SendOneTx}     txhash
        Log To Console        生成交易-txhash = ${txhash}
#        sleep     ${Block_Time}

        : FOR    ${INDEX}    IN RANGE    0    ${wait_times}
        \      ${transaction} =     PostData      ${GetTxByHash}     {"hash":"${txhash}"}       transaction
        \      Exit For Loop If  'status' in ${transaction}
       # \      Log to console      'wait..checking...'${txhash}
        \      sleep     1
        Log to console      交易入块成功..${txhash} status= ${transaction['status']}
        [return]      ${txhash}      ${transaction['status']}


*** Test Cases ***


001    [Documentation]      发送并检查模拟交易:${arg_gentxnum}
        Log To Console       发送模拟交易
        : FOR    ${INDEX}    IN RANGE    0    ${arg_gentxnum}
        \     ${TxhashAndStatus} =     SendAndCheckTx       10
        #\      Log to console         Send OK: ${TxhashAndStatus}
        \      Should Be Equal As Strings       @{TxhashAndStatus}[1]     D
        \      sleep     1s










