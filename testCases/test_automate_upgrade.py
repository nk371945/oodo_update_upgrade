import time

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class TestUpgrade:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    def test_upgrade(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.alp = self.lp.login()

        self.alp.clickMenu()
        self.alp.selectApps()
        time.sleep(10)
        self.alp.upgradeApp()

        self.alp.logout()

        self.driver.close()
