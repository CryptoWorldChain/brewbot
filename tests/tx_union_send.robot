
*** Settings ***
Library        Collections
Library        RequestsLibrary
Library        String

Resource      ../res/vers.robot



Suite Setup    InitSession


*** Variables ***

${union_address}       e0c7d2a75ccd61af87aaa818cdcb2246706363a1
${amount}              1000000000000000000

@{rel_addresses}       f4fcdf9e5603a5375f9fe0c8bba951e085cdcdfc
               ...     8502208b949e7c08acb4c2f1aef06caa39891a79
               ...     3eb9c18610e35c7f039d3591a15f967d98b3d5b8
               ...     3db85d2797ddc2a4802e9fff1a0232b0bbf06c8a
               ...     ad081e743aa6174e4d2609fc8b0985718e77082d
               ...     b16657a7bf154da2aab8dc9a3484e9413c165ff1

@{rel_keys}            1a7264ae5078f2a0c5b5e567457bbcedf1bdc3263ad32576c9a3c512c386ed6f
               ...     fe420ae439f8d76999dd9e784ab87c400c04029076f9d22044d20d9bd1277e54
               ...     5e6517749743b5c1d2f16dcf411d521dabe73933d4cfc5225b53e3113e62990b
               ...     d3b23e124199532c16fb4a940b5faf6ff6615479734e3decba4e644428bbba5d
               ...     e7d9b59ff26536531c0e502b7ddcd222df8c8c01a90dfe03e136704d93c3fea3
               ...     fc1d181a38ebc2ccc0c0d4c605937de17bc5fdb347a9621b74c544463d02e3cb





${to_addr}             3eb9c18610e35c7f039d3591a15f967d98b3d5b8
${GET_ACCOUNT_JSON}           {"address" :"${to_addr}" }

${union_sign_count}       6
${wait_times}            100
${relTxHash}            ${EMPTY}
${rel_address}            ${EMPTY}
${rel_key}            ${EMPTY}



${JSON_BODY}           {
        ...    "unionAccountAddress": "${union_address}",
        ...    "amount": "${amount}",
        ...   "relAddress": "${rel_address}",
        ...    "relKey": "${rel_key}",
        ...    "relTxHash": "${relTxHash}",
        ...    "toAddress": "${to_addr}"
        ...   }

*** Keywords ***

GenSendJsonBody
       [Arguments]    ${rel_address}      ${rel_key}       ${relTxHash}
       ${jsBody} =   Catenate     {"unionAccountAddress": "${union_address}",
        ...    "amount": "${amount}",
        ...   "relAddress": "${rel_address}",
        ...    "relKey": "${rel_key}",
        ...    "relTxHash": "${relTxHash}",
        ...    "toAddress": "${to_addr}"
        ...   }
       #Log  to console      \nsendjson=${jsBody}
       [return]     ${jsBody}

SendAndCheckTX
       [Arguments]    ${rel_address}      ${rel_key}       ${relTxHash}
        # Log to console       \nSendAndCheckTX[addr=${rel_address},key=${rel_key},hash=${relTxHash}]
        ${jsBody} =     GenSendJsonBody      ${rel_address}      ${rel_key}       ${relTxHash}
        Log to console        \nsendbody=${jsBody}
        ${txhash} =     PostData      ${TST_Union_Send}      ${jsBody}       retMsg
        Log To Console        生成交易-txhash = ${jsBody}
        : FOR    ${INDEX}    IN RANGE    0    ${wait_times}
        \      ${transaction} =     PostData      ${GetTxByHash}     {"hash":"${txhash}"}       transaction
        \      Exit For Loop If  'status' in ${transaction}
       # \      Log to console      'wait..checking...'${txhash}
        \      sleep     1
        Log to console      交易入块成功..${txhash} status= ${transaction['status']}
        [return]      ${txhash}


*** Test Cases ***



001    [Documentation]      联合账户转账: ${to_addr}


        : FOR    ${INDEX}    IN RANGE    0    ${union_sign_count}
        \      Log to console       \naddr=@{rel_addresses}[${index}],key=@{rel_keys}[${index}],hash=${relTxHash}
        \      ${returnTxHash} =       SendAndCheckTX       @{rel_addresses}[${index}]      @{rel_keys}[${index}]      ${relTxHash}
        \      Log to console       returnhash=${returnTxHash},relhash=${relTxHash}
        \      ${relTxHash} =      Set Variable If      '${relTxHash}'==''     ${returnTxHash}          ${relTxHash}


002    [Documentation]      获取账户余额: ${to_addr}
        ${accountinfo} =     PostData      ${GetAccountCoin}       {"address" :"${to_addr}" }      account
        Log                  ${accountinfo}
        Log to console       ${accountinfo}
        Log to console       \nbalance=${accountinfo['balance']}     If  balance in ${accountinfo}






