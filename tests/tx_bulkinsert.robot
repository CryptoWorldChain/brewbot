
*** Settings ***
Library        Collections
Library        RequestsLibrary
Library        String

Resource      ../res/vers.robot



Suite Setup    InitSession


*** Test Cases ***

001    [Documentation]      测试模拟交易笔数-${arg_gentxnum}
        [Tags]        Bulk Generate Transactions
        Log To Console        开始生成交易
        ${retcode} =      GenerateTestData      ${arg_gentxnum}
        Log To Console        结果==>${retcode}
        Should Be True    ${retcode} == 0

002    [Documentation]      检查交易笔数-${arg_gentxnum}
        Log To Console        循环检查交易
        : FOR    ${INDEX}    IN RANGE    1    ${arg_gentxnum}
        \     ${result} =     Fetch Info      ${TSTGetTestTxCount}     retmsg
        \     ${numtx} =      Get Substring       ${result}     7
        \      Log To Console        get-result = ${numtx}
        \      Exit For Loop If    ${numtx} >= ${arg_gentxnum}
        \      sleep     1s



