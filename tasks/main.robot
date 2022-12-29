*** Settings ***
Variables         ../resources/settings.py    ${env}
Library           TOSLibrary    ${db_server}    ${db_name}
...               ${DB_CRED_USR}    ${DB_CRED_PSW}    ${db_auth_source}
Library           ../libraries/RpaChallengeLibrary.py
Library           ../stages/Stage0.py
Library           ../stages/Stage1.py
Library           ../stages/Stage2.py

*** Test Cases ***
Producer stage
    [Tags]    stage_0
    [Documentation]    This is the producer stage
    Stage0.Main Loop

Consumer stage
    [Tags]    stage_1
    [Setup]    Stage1.Setup
    [Documentation]    This is the first consumer stage
    Stage1.Main Loop
    [Teardown]    Stage1.Teardown

Consumer stage
    [Tags]    stage_2
    Stage2.Main Action

