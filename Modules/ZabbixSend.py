import sys,os


class ZabbixSend():
    ''' class ZabbixSend for send message to Zabbix '''

    def __init__(self):
        self.file_name =  os.path.basename(__file__)

    def send(self,f):
        self.zabbix_server = 'www.zabbix.ru'
        os.chdir(sys.path[1])
        #self.zabbix_sender = r'zabbix_sender.exe'
        self.log_file = sys.path[1] + r'/ZabFiles/' + f + '.log'
        #os.system(self.zabbix_sender + ' -z %s -T -i "%s" -vv' % (self.zabbix_server, self.log_file))
        os.system('zabbix_sender -z %s -T -i "%s" -vv' % (self.zabbix_server, self.log_file))

if __name__ == '__main__':

    send = ZabbixSend()
    send.send('abnal')