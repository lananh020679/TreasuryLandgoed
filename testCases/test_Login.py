from utilities.readProperties import configure
from pageObjects.loginPage import Login
from utilities.customLogger import LogGen
import pytest
class Test_001_Login:
    logger=LogGen.loggen()
    baseUrl=configure.getUrl()
    company=configure.getCompany()
    username=configure.getUsername()

    @pytest.mark.function
    def test_homePageTitle(self,setup):
        self.logger.info("**********Begin testcase: Test for good logging***********")
        self.driver=setup

        self.logger.info("Go to Treasury page")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.logger.info("Enter company name:")
        self.lp.setCompany(self.company)
        #time.sleep(2)
        self.logger.info("Enter username:")
        self.lp.setUsername(self.username)
        #time.sleep(1)
        self.logger.info("Click Login button:")
        self.lp.clickLogin()
        #time.sleep(1)
        if self.driver.title=="Trace & Treasury":
            self.logger.info("Goed loging")
            assert True,"Succesfully Login Tresury"
            self.driver.quit()
        else:
            self.logger.info("Wrong username or companyname")
            self.driver.quit()
            assert False,"Wrong CompanyName or UserName"