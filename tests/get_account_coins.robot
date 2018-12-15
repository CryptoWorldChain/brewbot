
*** Settings ***
Library        Collections
Library        RequestsLibrary
Library        String

Resource      ../res/vers.robot



Suite Setup    InitSession


*** Variables ***

${to_addr}             e21ceee76f77b613fac3e9bb4fe34cdd4e7b3ea5
${JSON_BODY}           {"address" :"${to_addr}" }

*** Test Cases ***





001    [Documentation]      获取目标地址余额:   ${to_addr}
        ${accountinfo} =     PostData      ${GetAccountCoin}      ${JSON_BODY}      account
        Log     ${accountinfo}
        Log to console       \nbalance=${accountinfo['balance']}     If  balance in ${accountinfo}












