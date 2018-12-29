
*** Settings ***
Library        Collections
Library        RequestsLibrary
Library        String

Resource      ../res/vers.robot



Suite Setup    InitSession


*** Variables ***

${to_addr}             e0c7d2a75ccd61af87aaa818cdcb2246706363a1
${JSON_BODY}           {"address" :"${to_addr}" }

*** Test Cases ***





001    [Documentation]      获取目标地址余额:   ${to_addr}
        ${accountinfo} =     Post Data      ${APIGetAccountInfo}      ${JSON_BODY}      account    server=REMOTE
        Log     ${accountinfo}
        Log to console       \nbalance=${accountinfo['balance']}     If  balance in ${accountinfo}












