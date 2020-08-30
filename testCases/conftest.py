from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    driver=webdriver.Chrome()
    if browser=="chrome" or browser=="Chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox" or browser== "Firefox":
        driver=webdriver.Firefox()
    return  driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to settup method
    return request.config.getoption("--browser")


######Pytest HTML Report######
# It is hook for Adding Enviroment infor HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Treasury Verniewing'
    config._metadata['Module Name'] = 'Test in Selenium franework'
    config._metadata['Tester'] = 'Anh Pham'


# Its is hook for deleting or modifing Enviroment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)