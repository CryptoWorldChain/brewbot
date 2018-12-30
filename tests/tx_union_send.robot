
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

@{rel_keys}            6fed86c312c5a3c97625d33a26c3bdf1edbc7b4567e5b5c5a0f27850ae64721a
               ...     547e27d19b0dd24420d2f9769002040c407cb84a789edd9969d7f839e40a42fe
               ...     0b99623e11e3535b22c5cfd43339e7ab1d521d41cf6df1d2c1b543977417655e
               ...     5dbabb2844644ebaec3d4e73795461f66faf5f0b944afb162c539941123eb2d3
               ...     a3fec3934d7036e103fe0da9018c8cdf22d2dc7d2b500e1c533665f29fb5d9e7
               ...     cbe3023d4644c5741b62a947b3fdc57be17d9305c6d4c0c0ccc2eb381a181dfc





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
       [Arguments]      ${rel_address}      ${rel_key}          ${relTxHash}
        Log to console  \nSendAndCheckTX[addr=${rel_address},key=${rel_key},hash=${relTxHash}]
        ${jsBody} =     GenSendJsonBody     ${rel_address}      ${rel_key}       ${relTxHash}
        Log to console  \nsendbody=${jsBody}
        ${txhash} =     Post Data           ${TSTUnionSend}     ${jsBody}        retMsg       server=REMOTE
        Log To Console  生成交易-txhash = ${jsBody}
        : FOR           ${INDEX}    IN RANGE    0    ${wait_times}
        \               ${transaction} =     Post Data      ${APIGetTxByHash}     {"hash":"${txhash}"}       transaction   server=REMOTE
        \               Exit For Loop If  'status' in ${transaction}
       # \              Log to console      'wait..checking...'${txhash}
        \               sleep     1
        Log to console  交易入块成功..${txhash} status= ${transaction['status']}
        [return]        ${txhash}


*** Test Cases ***



001    [Documentation]      联合账户转账: ${to_addr}


        : FOR    ${INDEX}    IN RANGE    0    ${union_sign_count}
        \      Log to console       \naddr=@{rel_addresses}[${index}],key=@{rel_keys}[${index}],hash=${relTxHash}
        \      ${returnTxHash} =       SendAndCheckTX       @{rel_addresses}[${index}]      @{rel_keys}[${index}]      ${relTxHash}
        \      Log to console       returnhash=${returnTxHash},relhash=${relTxHash}
        \      ${relTxHash} =      Set Variable If      '${relTxHash}'==''     ${returnTxHash}          ${relTxHash}


002    [Documentation]      获取账户余额: ${to_addr}
        ${accountinfo} =     Post Data Remote      ${APIGetAccountInfo}       {"address" :"${to_addr}" }      account
        Log                  ${accountinfo}
        Log to console       ${accountinfo}
        Log to console       \nbalance=${accountinfo['balance']}     If  balance in ${accountinfo}






