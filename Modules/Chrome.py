from selenium import webdriver
import sys, os
from Modules.Times import Times
import time
import glob

times = Times()

chrome_driver = sys.path[1] + r'/bin/chromedriver'  # Путь до хромдрайвера
url = r'https://www.nalog.ru/rn77/service/actual_inn_ul/'


class Browser():
    '''Class Browser for Selenium lib'''

    def __init__(self, url):
        self.url = url


    def start(self):
        self.browser = webdriver.Chrome(chrome_driver)
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)  # seconds

    def get_url(self):
        self.browser.get(self.url)

    def screen(self, file):
        self.file = file
        #screen_dir = sys.path[1] + r'\screen\\' + file + '\\'
        self.screen_dir = sys.path[1] + r'/TESTS' +  r'/Screens' + '/' +self.file + '/'

        os.makedirs(self.screen_dir, exist_ok=True)
        self.screen_file = self.screen_dir + self.file + r'.' + times.date_now() + r'.png'
        self.browser.save_screenshot(self.screen_file)

    def drop_screen(self):
        self.screen_file_mask = self.screen_dir + self.file + '*'
        self.time_to_live = times.timeToLive()
        now = time.time()
        for f in glob.glob(self.screen_file_mask):
            if (os.stat(os.path.join(self.screen_file_mask, f)).st_mtime < now - self.time_to_live):
                try:
                    #print("Droped - ", f)
                    os.remove(f)
                except Exception as err:
                    print(err)
                    pass

    def quit(self):
        self.browser.close()
        self.browser.quit()



if __name__ == '__main__':

    check_inn = Browser(url)
    check_inn.start()
    check_inn.get_url()
    check_inn.quit()

