*** Settings ***
Library  SeleniumLibrary
Resource    ../../Resource/LoginKeywords.robot

*** Variables ***
${browser}  Chrome
${InfrastructureUrl}    https://treasury201804.aareoncloud.nl/
${companyName}      Keylib omgeving
${userName}     anhpham

*** Test Cases ***
LoginTest
    Open my Browser    ${InfrastructureUrl}   ${browser}
    Enter Company Name      ${companyName}
    Enter User Name     ${userName}
    Click Login
    Validate Succesfull Login
    Close My Browser

*** Keywords ***

