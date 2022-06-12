import os 
import subprocess
import time

class SingelProcess:
    
    def __init__(self):
        p = subprocess.Popen('chdir C:\\ && mkdir Process', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.stdout.readlines()
        self.process_id=str(os.getpid())
     
    
    
    def killothers(self):
        with open('C:\\Process\\pid.txt','w') as file:
            file.write(self.process_id)
            file.close()
        time.sleep(1)
        with open('C:\\Process\\pid.txt','r') as file:
            check_pid=file.read().strip()
            file.close()
            print(check_pid,self.process_id)
        if check_pid==self.process_id:
            return check_pid
        return False
        
    
    def run_single(self):
        while True:
            with open('C:\\Process\\pid.txt','w') as file:
                file.write('0')
            time.sleep(0.5)