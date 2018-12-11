
*** Settings ***
Library        Collections
Library        RequestsLibrary
Library        String

Resource      ../res/vers.robot



Suite Setup    InitSession


*** Test Cases ***

001    [Documentation]       生成模拟交易${arg_gentxnum}
        [Tags]        Generate Transaction
        ${retcode} =      GenerateTestData      ${arg_gentxnum}
        Log        hello==>${retcode}
        Should Be True    ${retcode} == 0
        : FOR    ${INDEX}    IN RANGE    1    100
        \     ${result} =     FetchInfo      ${GetTestTxCount}     retmsg
        \     ${numtx} =      Get Substring       ${result}     7
        \      Log To Console        get-result = ${numtx}
        \      Exit For Loop If    ${numtx} >= ${arg_gentxnum}
        \      sleep     1s







