*** Settings ***
Library     SeleniumLibrary
Variables    ../pageObjects/Locators.py


*** Keywords ***
Open my Browser
    [Arguments]     ${baseUrl}  ${browser}
    Open Browser     ${baseUrl}  ${browser}
    Maximize Browser Window


Enter Company Name
    [Arguments]     ${companyName}
    Input Text      ${txt_Company_id}    ${companyName}


Enter User Name
    [Arguments]     ${userName}
    Input Text      ${txt_Username_id}      ${userName}


Enter User Password
    [Arguments]     ${passWord}
    Input Text      ${txt_Password_id}      ${passWord}

Click Login
    click button    ${btn_Login_id}

Validate Succesfull Login
    title should be     Trace & Treasury

Close My Browser
    close all browsers
