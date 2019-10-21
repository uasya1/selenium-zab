import os
from Modules.GetLog import Logs
from Modules.Chrome import Browser
from Modules.ZabbixSend import ZabbixSend
from Modules.Times import Times

#Web
chrome = Browser(r'https://www.google.com/')
file_name = os.path.splitext(os.path.basename(__file__))[0]

#Zabbix
send = ZabbixSend()

#Logs
logs = Logs(file_name)

#Times
times = Times()

while True:
    try:
        logs.clear()
        tmp_msg = '0----------Start----------0'
        chrome.start()
        chrome.get_url()
        logs.info(tmp_msg)
        chrome.browser.implicitly_wait(1)


        tmp_msg = 'Go to I`m Feeling Lucky'
        chrome.browser.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/div[1]/div[3]/center/input[2]').click()
        logs.info(tmp_msg)

        tmp_msg = 'Check'
        chrome.browser.implicitly_wait(1)
        test = chrome.browser.find_element_by_xpath('//*[@id="nav-list"]/li[2]/a')
        if 'About' not in test.text:
            raise Exception("Error, About not found")
        logs.info(tmp_msg)

        tmp_msg = 'Search lol'
        chrome.browser.find_element_by_xpath('//*[@id="searchinput"]').send_keys('lol')
        chrome.browser.find_element_by_xpath('//*[@id="searchbtn"]').click()
        logs.info(tmp_msg)

        tmp_msg = 'Screenshot'
        chrome.screen(file_name)
        logs.info(tmp_msg)

        tmp_msg = 'Exit'
        chrome.quit()
        logs.info(tmp_msg)
        logs.other()


    except Exception as err:
        chrome.screen(file_name)
        chrome.quit()
        logs.error(tmp_msg, err)
        logs.other()

    finally:
        chrome.drop_screen()
        send.send(file_name)
        times.sleep()

