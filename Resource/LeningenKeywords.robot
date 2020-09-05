*** Settings ***
Library  SeleniumLibrary
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
Click On FinanInstrumenten Menu
    Wait Until Page Contains Element     ${mnu_FinanInstrumenten_xpath}    10
    Click Element   ${mnu_FinanInstrumenten_xpath}
Click On Leningen Item
    Wait Until Page Contains Element    ${mnuitem_Leningen_xpath}   10
    Click Element   ${mnuitem_Leningen_xpath}
Click On Nieuw Button
    Wait Until Page Contains Element    ${btn_Nieuws_xpath}
    Click Element    ${btn_Nieuws_xpath}
Choice Sort Leningen
    Wait Until Page Contains Element    ${drd_Sortleningen_xpath}
    Click Element   ${drd_Sortleningen_xpath}
Click OK Button
    Wait Until Page Contains Element    ${btn_OK_xpath}
    Click Button   ${btn_OK_xpath}
# Fulling Lening Screen
Handeling Drp SoortLeningen
    [Arguments]     ${value}
    Wait Until Page Contains Element    ${drd_ChoiceSortLeningen_xpath}
    select from list by lable   ${drd_ChoiceSortLeningen_xpath}     ${value}