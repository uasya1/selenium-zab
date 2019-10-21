import os
from Modules.GetLog import Logs
from Modules.Chrome import Browser
from Modules.ZabbixSend import ZabbixSend
from Modules.Times import Times

#Web
chrome = Browser(r'https://www.yahoo.com/')
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



        tmp_msg = 'Input text'
        chrome.browser.find_element_by_xpath('//*[@id="uh-search-box"]').send_keys('google')
        logs.info(tmp_msg)

        tmp_msg = 'Click search'
        chrome.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[2]/div/div/form/table/tbody/tr/td[2]/button/i').click()
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
