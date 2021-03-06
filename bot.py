import time
from selenium import webdriver
from chromedriver_py import binary_path

class Bot:

    def __init__(self,city:str,headlessMode:bool):
        self.city = city
        self.options = webdriver.ChromeOptions()
        self.options.set_headless(headless=headlessMode)
        self.options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(executable_path=binary_path,chrome_options=self.options)

    def startBot(self):
        self.callWebsite()
        self.chooseCity(self.city)
        self.checkAppointment()

    def callWebsite(self):
        baseUrl = "https://www.impfen-saarland.de/service/waitlist_entries"
        self.driver.get(baseUrl)
        time.sleep(0.35)

    def checkAppointment(self):
        time.sleep(0.35)
        element_AppointmentIsNotAvailable = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/h5')
        time.sleep(0.35)
        if(element_AppointmentIsNotAvailable.get_attribute('innerHTML')=="Keine Termine verfügbar. "):
            element_Back = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div/button')
            element_Back.click()
            time.sleep(0.35)
            self.chooseCity(self.city)
            time.sleep(0.35)
            self.checkAppointment()

        elif(element_AppointmentIsNotAvailable.get_attribute('innerHTML')=="Impftermine auswählen"):
            element_Appointment = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/div[2]')
            element_Appointment.click()
            element_Continue = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            element_Continue.click()
            time.sleep(0.35)
            if(self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')):
                elementLogin = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
                elementLogin.click()                         
                time.sleep(0.35)
            else:
                element_Back = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[1]')
                element_Back.click()
                

    def chooseCity(self,city):
        if(city == "Saarbrücken"):
            time.sleep(0.35)
            elementSaarbrücken = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[1]')
            time.sleep(0.35)
            elementSaarbrücken.click()
            element_Continue = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            time.sleep(0.35)
            element_Continue.click()
            time.sleep(0.35)
        if(city == "Saarlouis"):
            time.sleep(0.35)
            elementSaarlouis = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[2]')
            elementSaarlouis.click()
            element_Continue = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            element_Continue.click()
            time.sleep(0.35)
        if(city == "Neunkirchen"):
            time.sleep(0.35)
            elementNeunkirchen = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[3]')
            elementNeunkirchen.click()
            element_Continue = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            element_Continue.click()
            time.sleep(0.35)
        if(city == "Lebach"):
            time.sleep(0.35)
            elementLebach = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[4]')
            elementLebach.click()
            element_Continue = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            element_Continue.click()
            time.sleep(0.35)
        if(city == "LebachNacht"):
            time.sleep(0.35)
            elementLebachNacht = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[1]/button[35]')
            elementLebachNacht.click()
            element_Continue = self.driver.find_element_by_xpath('//*[@id="logged-in-area"]/div/div[2]/div[2]/button[2]')
            element_Continue.click()
            time.sleep(0.35)
        

