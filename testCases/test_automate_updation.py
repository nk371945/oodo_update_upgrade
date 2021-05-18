import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class TestUpdate:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    def test_update(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.lp.enterUserName(self.username)
        self.lp.enterPassword(self.password)
        self.alp = self.lp.login()

        time.sleep(10)

        current_url = self.driver.current_url
        debugMode = '?debug'
        index_of_hash = current_url.find('#')
        debugModeUrl = current_url[:index_of_hash] + debugMode + current_url[index_of_hash:]

        self.driver.get(debugModeUrl)

        self.alp.clickMenu()
        self.alp.selectApps()
        self.alp.clickUpdateAppList()
        self.alp.clickUpdateModuleBtn()

        time.sleep(60)

        self.alp.logout()

        self.driver.close()
