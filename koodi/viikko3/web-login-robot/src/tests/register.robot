*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Create User

*** Test Cases ***

Register With Valid Username And Password
    Set Username  Validi
    Set Password  validi66
    Set Password Confirmation  validi66
    Create Account
    Creating Account Should Succeed

Register With Too Short Username And Valid Password
    Set Username  V
    Set Password  validi66
    Set Password Confirmation  validi66
    Create Account
    Creating Account Should Fail With Message  Username or Password invalid

Register With Valid Username And Too Short Password
    Set Username  Valid
    Set Password  v
    Set Password Confirmation  v
    Create Account
    Creating Account Should Fail With Message  Username or Password invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  Vali
    Set Password  validi66
    Set Password Confirmation  validi6
    Create Account
    Creating Account Should Fail With Message  Passwords not matching




*** Keywords ***
Creating Account Should Succeed
    Welcome Page Should Be Open

Creating Account Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create Account
    Click Button  Register


Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Go To Create User
    Go To Register Page
    Register Page Should Be Open