import datetime
import time

class Times():
    ''' Class Times for functions with TIME'''

    def timeToLive(self):
        self.time = 3600 #Hour
        return self.time

    def sleep(self):
        time_sleep = 30
        time.sleep(time_sleep)

    def date_now(self):
        return datetime.datetime.today().strftime("%Y.%m.%d-%H.%M.%S")

    def time_fu(self):
        temp = str(int((time.mktime(datetime.datetime.now().timetuple()))))
        return temp



if __name__ == '__main__':

    lol = Times()
    print(lol.timeToLive())