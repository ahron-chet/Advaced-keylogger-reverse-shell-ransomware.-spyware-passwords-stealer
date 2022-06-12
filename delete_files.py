
import subprocess
import os
from os import listdir
from os.path import isfile,join 

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
        return self.to_send
       
    
    def recursive_fles_delete(self,path):
        p = subprocess.Popen('rd /s /q "'+path+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        c = p.stdout.readline()
        if len(c)<2:
            return 'Successfully deleted'
        return c
       