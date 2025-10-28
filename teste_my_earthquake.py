import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import time
import os
import base64

caps = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Emulator-5554',
    appPackage='com.jrustonapps.myearthquakealerts',
    appActivity='com.jrustonapps.myearthquakealerts.controllers.MainActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, caps)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
# Teste dos pontos de localização

    def test_myearthquake(self) -> None:
        self.driver.start_recording_screen()

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="android:id/button1"]').click()

        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
        el.click()

        from time import sleep

        sleep(8)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-locpoint-1.png'
        self.driver.save_screenshot(directory + file_name)

        # mudar o ponto de pesquisa pra um que esteja no mapa no momento

        self.driver.swipe(135, 726, 684, 549)
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Offshore Bio-bio, Chile (3.20). 22:16: Offshore Bio-bio, Chile."]').click()

        sleep(3)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-locpoint-2.png'
        self.driver.save_screenshot(directory + file_name)

# Verificando eventos recentes

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/titles"]').click()
        sleep(5)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-eventlist-1.png'
        self.driver.save_screenshot(directory + file_name)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Navigate up"]').click()
        sleep(3)

        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
        el.click()

        sleep(2)

# verificar região selecionada
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="More options"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Settings"]').click()
        sleep(2)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-region-1.png'
        self.driver.save_screenshot(directory + file_name)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="My Region"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Your Region"]').click()
        sleep(2)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-region-2.png'
        self.driver.save_screenshot(directory + file_name)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Oceania"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]').click()
        sleep(2)

        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
        el.click()
        sleep(4)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-region-3.png'
        self.driver.save_screenshot(directory + file_name)

# verificar por país
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="More options"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Settings"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="My Region"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Your Country"]').click()
        sleep(2)

        self.driver.swipe(471, 1689, 484, 781)
        self.driver.swipe(514, 1320, 507, 708)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-country-1.png'
        self.driver.save_screenshot(directory + file_name)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Brazil"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]').click()
        sleep(2)

        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
        el.click()

        sleep(2)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-country-2.png'
        self.driver.save_screenshot(directory + file_name)

# Verificar as ocorrencias em determinada data

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/action_search"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateFrom"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="08 May 2023"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="OK"]').click()
        sleep(2)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-date-1.png'
        self.driver.save_screenshot(directory + file_name)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateTo"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="10 May 2023"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="OK"]').click()
        sleep(2)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-date-1.png'
        self.driver.save_screenshot(directory + file_name)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Interstitial close button"]').click()
        sleep(10)

        self.driver.swipe(511, 1534, 528, 653, 200)
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Navigate up"]').click()
        sleep(3)

# Verificar os diferentes tipos de mapa

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="More options"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Settings"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Maps"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Map Type"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@text="Satellite"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]').click()
        sleep(2)

        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@content-desc="Settings"]').click()
        sleep(5)

        WebDriverWait(self.driver, 200).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')))
        el = self.driver.find_element(
            by=AppiumBy.XPATH, value='//*[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]')
        el.click()

        sleep(6)

        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-map-1.png'
        self.driver.save_screenshot(directory + file_name)

        self.driver.swipe(871, 565, 141, 575, 200)

        sleep(5)

        filepath = os.path.join(directory, "screen_recording_chrome.mp4")
        payload = self.driver.stop_recording_screen()
        with open(filepath, "wb") as fd:
            fd.write(base64.b64decode(payload))


if __name__ == '__main__':
    unittest.main()
