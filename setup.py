#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from time import sleep
import sys

def color(string, color=None):
    attr = []
    attr.append('1')
    
    if color:
        if color.lower() == "red":
            attr.append('31')
        elif color.lower() == "green":
            attr.append('32')
        elif color.lower() == "blue":
            attr.append('34')
        elif color.lower() == "yellow":
            attr.append('33')
        return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
def arquivo(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print 'erro'.format(**locals())
            
    
    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)


def hours():
    os.system("clear")
    print color ("  Hours        Date","green")
    os.system(' date +"  %R      %D" ')


hours()
print color("""
      ,/|         _.--''^``-...___.._.,;
     /, \'.     _-'          ,--,,,--'''
    { \    `_-''       '    /}
     `;;'            ;   ; ;
 ._.--''     ._,,, _..'  .;.'
  (,_....----'''     (,..--''
         
       Checking System ...
""","green")

if os.system("xterm -v > /dev/null 2>&1"):
    print color(" [ X ] xterm ","red")
    print color(" Installing...","green")
    os.system("sudo apt-get install xterm")
    print color(" [ ✔ ] xterm ","yellow")
else:
    print color(" [ ✔ ] xterm ","yellow")
sleep(1.0)
if os.system("apktool --version > /dev/null 2>&1"):
    print color(" [ X ] apktool ","red")
    print color(" Installing...","green")
    os.system('xterm -T "Installing apktool" -geometry 100x30 -e "sudo apt-get install apktool -y"')
    print color(" [ ✔ ] apktool ","yellow")
else:
    print color(" [ ✔ ] apktool ","yellow")
sleep(1.0)
if os.system("cat /bin/zipalign > /dev/null 2>&1"):
    print color(" [ X ] zipalign ","red")
    print color(" Installing...","green")
    os.system('xterm -T "Installing zipalign" -geometry 100x30 -e "sudo apt-get install zipalign -y"')
    print color(" [ ✔ ] zipalign ","yellow")
else:
    print color(" [ ✔ ] zipalign ","yellow")
sleep(1.0)
if os.system("apksigner --version > /dev/null 2>&1"):
    print color(" [ X ] apksigner ","red")
    print color(" Installing...","green")
    os.system('xterm -T "Installing apksigner" -geometry 100x30 -e "sudo apt-get install apksigner -y"')
    print color(" [ ✔ ] apksigner ","yellow")
else:
    print color(" [ ✔ ] apksigner ","yellow")
sleep(1.0)
if os.system("cat /bin/msfvenom > /dev/null 2>&1"):
    print color(" [ X ] metasploit framework ","red")
    print color(" Installing...","green")
    os.system('xterm -T "Installing metasploit-framework" -geometry 100x30 -e "chmod +x config/msfinstall && ./config/msfinstall"')
    print color(" [ ✔ ] metasploit-framework ","yellow")
else:
    print color(" [ ✔ ] metasploit-framework ","yellow")
sleep(1.0)
print("")
print color(" [ ... ] checking openjdk ","green")
os.system('xterm -T "checking openjdk" -geometry 100x30 -e "sudo apt-get install openjdk-8* -y"')
os.system('xterm -T "checking openjdk" -geometry 100x30 -e "sudo apt-get install openjdk-11* -y"')
print("")
print color(" All Ready =] ","green")
print("")


