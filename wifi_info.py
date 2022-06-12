import subprocess
class Wifi_information():
 
    def wifi_info_exp(self): 
        p = subprocess.Popen("netsh wlan show  profile", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        profiles=[]
        for line in p.stdout.readlines():
            line=line.decode()
            if 'All User Profile'in line:
                line=line.strip().split(' : ')
                profiles.append(line[-1])                
        data_out=''
    
        expend_wifi_info=[]
        for i in range(len(profiles)):
            p = subprocess.Popen("netsh wlan show  profile "+profiles[i]+' key=clear', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                line=line.decode().strip()
                data_out+=line
                data_out+='\r\n'
            expend_wifi_info.append(data_out)
            data_out=''
        return expend_wifi_info
    
    
    
    def wifi_passwords(self):
        passwords=self.wifi_info_exp()
        res=''
        for i in passwords:
            key_contant=''
            name=''
            i=i.split('\r\n')
            for n in i:
                if "Name" in n:
                    n=n.replace('\n','').split(" : ")
                    name=n[-1]
                    
                elif "Key Content" in n:
                    n=n.replace('\n','').split(" : ")
                    key_contant=n[-1]
                    
            if len(key_contant)<2 and len(name)>1:
                key_contant='None'
            if len(name)>1:
                res+=(f'{name:<20}{key_contant:>20}')
                res+='\n'
        return res
                    
        