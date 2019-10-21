import logging
import sys, os
from Modules.Times import Times
from logging.handlers import RotatingFileHandler

#Times
times = Times()

class Logs():
    ''' Logging files of autotests '''

    def __init__(self, name_log_file, level=logging.DEBUG):

        self.name_log_file = name_log_file
        self.key = 'key'

        # Create the Logger
        self.logger = logging.getLogger(__name__)

        # Formater
        formatter = logging.Formatter('%(asctime)-1s %(process)d %(levelname)s %(message)s', datefmt='%d_%b_%y - %H:%M:%S')

        # Check directory
        self.dir_log = sys.path[1] + r'/Logs/' #For logs
        #self.dir_log = r'\\dpc.tax.nalog.ru\root\GRs\NPK\gr264\LOGS\_test\Selenium_Py\TESTS' + r'\Logs\\'
        self.tmp_log = sys.path[1] + r'/ZabFiles/' #For temp zabbix files
        self.bc_log = self.dir_log + r'/backups/' + self.name_log_file + '/' #For temp zabbix files

        os.makedirs(self.dir_log, exist_ok=True)
        os.makedirs(self.tmp_log, exist_ok=True)
        os.makedirs(self.bc_log, exist_ok=True)

        #name log file
        self.tmp_file = self.dir_log + self.name_log_file + '.log'
        self.file_tmp = self.tmp_log + self.name_log_file + r'.log'

        #backups files
        self.buckup_file = self.bc_log + self.name_log_file + '.log'


        #Rotation add
        rotationHandler = RotatingFileHandler(self.buckup_file,'a',maxBytes=1024*1024, backupCount=5) # 5 Files
        rotationHandler.setFormatter(formatter)
        self.logger.addHandler(rotationHandler)


        fileHandler = logging.FileHandler(self.tmp_file, mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        self.logger.setLevel(level)
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(streamHandler)

    def clear(self):
        ''' Clear cmd, and clear temp log file to Zabbix'''
        try:
            os.system('cls')
            self.current_number = 0
            self.file = open(self.file_tmp, 'w+')
            self.file.write('')
            self.file.close()
            self.time_start = times.time_fu()
        except:
            print('Error clear method')


    def debug(self, *args):
        ''' Logging in to log file and tmp log file. lvl - DEBUG'''

        try:
            self.current_number += 1
            for b in args:
                self.logger.debug(str(self.current_number)  + '. ' +  str(b))
        except Exception as err:
            print('Error logfile debug method. Error - ', err)

        try:
            self.file = open(self.file_tmp, 'a+')
            self.file.write(self.name_log_file + ' ' + self.key + ' ' + times.time_fu() + ' DEBUG ' + str(self.current_number) + '. ' + str(args[0]) + '\n')
            self.file.close()
        except:
            print('Error zab log file debug method')

    def info(self, *args):
        ''' Logging in to log file and tmp log file. lvl - INFO'''

        try:
            self.current_number += 1
            for b in args:
                self.logger.info(str(self.current_number)  + '. ' +  str(b))
        except Exception as err:
            print('Error logfile info method. Error - ', err)

        try:
            self.file = open(self.file_tmp, 'a+')
            self.file.write(self.name_log_file + ' ' + self.key + ' ' + times.time_fu() + ' INFO ' + str(self.current_number) + '. ' + str(args[0]) + '\n')
            self.file.close()
        except:
            print('Error zab log file info method')

    def warning(self, *args):
        ''' Logging in to log file and tmp log file. lvl - WARNING'''

        try:
            self.current_number += 1
            for b in args:
                self.logger.warning(str(self.current_number)  + '. ' +  str(b))
        except Exception as err:
            print('Error logfile warning method. Error - ', err)

        try:
            self.file = open(self.file_tmp, 'a+')
            self.file.write(self.name_log_file + ' ' + self.key + ' ' + times.time_fu() + ' WARNING ' + str(self.current_number) + '. ' + str(args[0]) + '\n')
            self.file.close()
        except:
            print('Error zab log file warning method')

    def error(self, *args):
        ''' Logging in to log file and tmp log file. lvl - ERROR'''

        try:
            self.current_number += 1
            for b in args:
                self.logger.error(str(self.current_number)  + '. ' +  str(b))
        except Exception as err:
            print('Error logfile error method. Error - ', err)

        try:

            self.file = open(self.file_tmp, 'a+')
            self.file.write(self.name_log_file + ' ' + self.key + ' ' + times.time_fu() + ' ERROR ' + str(self.current_number) + '. ' + str(args[0]) + '\n')
            self.file.close()
        except:
            print('Error zab log file error method')

    def critical(self, *args):
        ''' Logging in to log file and tmp log file. lvl - CRITICAL'''
        try:
            self.current_number += 1
            for b in args:
                self.logger.critical(str(self.current_number)  + '. ' +  str(b))
        except Exception as err:
            print('Error logfile critical method. Error - ', err)

        try:
            self.file = open(self.file_tmp, 'a+')
            self.file.write(self.name_log_file + ' ' + self.key + ' ' + times.time_fu() + ' CRITICAL ' + str(self.current_number) + '. ' + str(args[0]) + '\n')
            self.file.close()
        except:
            print('Error zab log file critical method')


    def other(self):

        self.time_end = int(times.time_fu()) - int(self.time_start)
        try:
            self.logger.info(str('Время выполнения скрита - '  + str(self.time_end)))
        except Exception as err:
            print('Error logfile other method. Error - ', err)

        try:
            self.file = open(self.file_tmp, 'a+')
            self.file.write(self.name_log_file + ' ' + self.key + ' ' + times.time_fu() + ' OTHER ' + 'Время выполнения скрита - '  + str(self.time_end) +  '\n')
            self.file.close()
        except:
            print('Error zab log file other method')



def main():

    test_log = Logs('testlog')
    test_log.clear()
    test_log.debug('test debug')
    test_log.info('test info')
    test_log.warning('test warning')
    test_log.error('test error', 'error')
    test_log.critical('test critical', 'error')

if '__main__' == __name__:
    main()
