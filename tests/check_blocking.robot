
*** Settings ***
Library	Collections
Library	RequestsLibrary

Resource   ../res/vers.robot


Suite Setup    InitSession


*** Test Cases ***

001    [Documentation]       检查是否正在打块,出块间隔等待${Block_Time}。
       [Tags]        Blocking Check
        ${num1} =      FetchInfo      ${GetLatestBlock}     number
        Log To Console        check.1==>${num1}
        Sleep       ${Block_Time}
       ${num2} =      FetchInfo      ${GetLatestBlock}     number
        Log To Console        check.2==>${num2}
        Sleep       ${Block_Time}
        ${num3} =      FetchInfo      ${GetLatestBlock}     number
        Log To Console      check==>${num1},${num2},${num3}
        Should Be True    ${num1}<${num2}<${num3}
