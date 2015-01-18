#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      liyongquan
#
# Created:     09/01/2015
# Copyright:   (c) liyongquan 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#-*-coding:utf-8-*-
import platform
import re
import os


class Hostoper:
    def __init__(self):
        self.system=platform.system()
        if self.system=='Windows':
            self.hosts_address=r'C:\Windows\System32\drivers\etc\hosts'
            #self.hosts_address=r'D:\py_work\hosts.txt'
        elif self.system=='Linux':
            self.hosts_address=r'/etc/hosts'
    def rHosts(self,file_name,*host_address):
        ip=[]
        self.hosts_name=[]
        try:
            os.path.exists(file_name)
        except:
            print "Sorry, I cannot find the %s file" % file_name
            return
        rtxt=open(file_name)

        if len(host_address)!=0:
            host_name=rtxt.read()
            for tmp in host_address:
                pattern  = re.compile(r'#'+tmp+'([^\#]*\n[^\#]*)*#'+tmp+' '+'END',re.I)
                ip.append('\n'.join(pattern.findall(host_name)[0].split('\n')))
                self.hosts_name.append(r'#'+tmp)
                for tmp1 in ip:
                    for tmp2 in tmp1.strip().split('\n'):
                        self.hosts_name.append(tmp2)
                self.hosts_name.append(r'#'+tmp+' '+'END')
        else:
            host_name=rtxt.readlines()
            for tmp1 in host_name:
                self.hosts_name.append(tmp1.strip())

    def wHosts(self):
        f=open(self.hosts_address,'a')
        f.write('\n')
        for tmp in self.hosts_name:
            f.write(tmp)
            f.write('\n')
        f.close()

    def dHosts(self):
        f=open(self.hosts_address)
        tmp_host=[]
        for tmp in f.readlines():
            tmp_host.append(tmp.strip())
        f.close()
        for tmp in self.hosts_name:
            if tmp in tmp_host:
                tmp_host.remove(tmp)
        f=open(self.hosts_address,'w')
        for tmp in tmp_host:
            f.write(tmp)
            f.write('\n')
        f.close()


if __name__ == '__main__':
    oper=Hostoper()
    oper.rHosts(r'D:\py_work\host.txt','ERP','SAF')
    #oper.rHosts(r'D:\py_work\host.txt')
    oper.dHosts()



