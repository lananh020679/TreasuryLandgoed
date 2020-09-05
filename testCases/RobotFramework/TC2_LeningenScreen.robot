*** Settings ***
Library  SeleniumLibrary
Resource  ../../Resource/LeningenKeywords.robot
*** Variables ***
${browser}  Chrome
${InfrastructureUrl}    https://treasury201804.aareoncloud.nl/
${companyName}      Keylib omgeving
${userName}     anhpham
${value}    Lening
*** Test Cases ***
LoginTest
    Open my Browser    ${InfrastructureUrl}   ${browser}
    Enter Company Name      ${companyName}
    Enter User Name     ${userName}
    Click Login
    Validate Succesfull Login
    #sleep    2    seconds
    Click On FinanInstrumenten Menu
    #sleep    2   seconds
    Click On Leningen Item
    #Close My Browser
    sleep    2   seconds
    Click On Nieuw Button
    Choice Sort Leningen
    Click OK Button
    sleep    2   seconds
    Handeling Drp SoortLeningen ${value}
*** Keywords ***