#!/usr/bin/env python3

#import required packages
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import calendar
import time
import openpyxl as excel

#driver to open site
driver = webdriver.Firefox()

# liink to oopen a site
driver.get("https://web.whatsapp.com")

# 10 sec wait time to load, if good internet connection is not good then increase the time
# units in seconds
# note this time is being used below also
wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)
input("Scan the QR code and then press Enter")


wait = WebDriverWait(driver, 10)
wait5 = WebDriverWait(driver, 5)
input("Scan the QR code and then press Enter")

#Send message
def sendMessage(msgToSend, targetName):
    count = 0
    while count<len(msgToSend):
        #identitify time
        curTime = datetime.datetime.now()
        curHour = curTime.time().hour
        curMin = curTime.time().minute
        curSec = curTime.time().second
        
        #Todays date
        curDate = datetime.datetime.date().today()
        curDay = curDate.day()
        curMonth = curDate.month()
        
        #checks the current time
        if msgToSend[count][0] == curHour and  msgToSend[count][1] == curMin and msgToSend[count][2] == curSec:
            # utility variables to tract count of success and fails
            success = 0
            sNo = 1
            failList = []

            #itterate over selected contacts
            try:
                # Select the target
                x_arg = '//span[contains(@title,' + targetName +')]'
                try:
                    wait5index.until(EC.presence_of_element_located(By.XPATH,x_arg)))
                except :
                    SearchTarget(targetName)   
                
                #Select the target
                driver.find_element_by_xpath(x_arg).click()
                print("Target successfully selected")
                time.sleep(2)

                #select the inputbox
                inp_xpath = "//div[@contenteditable='true']"
                input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))
                time.sleep(1)
                
                #Send Message
                # target is your target Name and msgToSend is your message

                input_box.send_keys("Hello, " + targetName + "." + Keys.SHIFT + Keys.ENTER + msgToSend[count][3] + Keys.SPACE + Keys.ENTER)

                # Link preview time, reduce this time, if internet connection is good

                time.sleep(10)
                input_box.send_keys(Keys.ENTER)
                print("Successfully send message to:" + targetName + '/n')
                success+=1
                time.sleep(0.5)


def SearchTarget(targetName):
     # If contact is not found then search for it
    searchBoxPath = '//*[@id="input-chatlist-search]"'
    wait5.until(EC.presence_of_element_located((By.ID, "input-chatlist-search")))
    inputSearchBox = driver.find_element_by_id("inpyt-chatlist-search")
    time.sleep(0.5)
    # click the search button
    driver.find_element_by_xpath('html/body/div/div/div/div[2]/div/div[2]/div/button').click()
    time.sleep(1)
    inputSearchBox.clear()
    inputSearchBox.send_keys(targetName[1:len(targetName)-1])
    print('Target Searched')
    
    # Increase the time if searching a contact is taking too long
    time.sleep(4)
    
