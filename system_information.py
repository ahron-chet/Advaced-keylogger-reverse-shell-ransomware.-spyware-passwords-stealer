import psutil
import platform
from datetime import datetime
import requests
import os


class Computer_inforamtion:
    
    def regional_time(self):
        r=requests.get(r'https://ipinfo.io/json')
        cuntry=r.json()['country'].strip()
        city=r.json()['timezone'].strip().split('/')[-1]
        now=datetime.now()
        dt=now.strftime("%d/%m/%Y %H:%M:%S")
        return f"Zone: {cuntry} {city}"+'\n'+f"Time: {dt}"+'\n'+'-'*25+'\n'
        
        
    def boot_time(self):
        rt=psutil.boot_time()
        bt = datetime.fromtimestamp(rt)
        return '='*40+'Boot time'+'='*40+'\n'+f"{'Boot time:':<20} {bt.year:}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"+'\n'

    def get_size(self,size):
        sizes=['B','KB','MB','GB','TB','PB','EB','ZB','YB']
        for i in range(len(sizes)):
            if 1024>size:
                return str(round(size,1))+sizes[i]
            size=size/1024
        return size
            
    def system_info(self):
        out=''
        p=platform.uname()
        out+="="*40+" System Information "+"="*40+'\n'
        out+=f"{'System':<20} {p.system:<40}"+'\n'
        out+=f"{'Computer Name':<20} {p.node:<40}"+'\n'
        out+=f"{'User name':<20} {str(os.getlogin()):<40}"+'\n'
        out+=f"{'Release':<20} {p.release:<40}"+'\n'
        out+=f"{'Version':<20} {p.version:<40}"+'\n'
        out+=f"{'Machine':<20} {p.machine:<40}"+'\n'
        out+=f"{'Processor':<20} {p.processor:<40}"+'\n'
        return out
    
    def cpu_info(self):
        out=''
        out+="="*40+" CPU Info "+ "="*40+'\n'
        out+=f"{'Physical cores:':<20} {str(psutil.cpu_count(logical=False)):<45}"+'\n'
        out+=f"{'Total cores:':<20} {str(psutil.cpu_count(logical=True)):<45}"+'\n'
        cpufreq = psutil.cpu_freq()
        out+=f"{'Max Frequency:':<20} {str(round(cpufreq.max,2))+' Mhz':<45}"+'\n'
        out+=f"{'Min Frequency:':<20} {str(round(cpufreq.min,2))+' Mhz':<45}"+'\n'
        out+=f"{'Current Frequency:':<20} {str(round(cpufreq.current,2))+' Mhz':<45}"+'\n\n'
        out+='='*20+" CPU Usage Per Core: "+'='*20+'\n'
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            out+=f"{'Core:'+str(i):<20} {str(percentage)+'%':<45}"+'\n'
        out+=f"{'Total CPU Usage:':<20} {str(psutil.cpu_percent())+'%':<45}"+'\n'
        return out

    def memory_info(self): 
        out=''
        out+="="*40+" Memory Information "+"="*40+'\n'
        svmem = psutil.virtual_memory()
        out+=f"{'Total:':<20} {self.get_size(svmem.total):<45}"+'\n'
        out+=f"{'Available:':<20} {self.get_size(svmem.available):<45}"+'\n'
        out+=f"{'Used:':<20} {self.get_size(svmem.used):<45}"+'\n'
        out+=f"{'Percentage:':<20} {str(svmem.percent)+'%':<45}"+'\n\n'
        out+="="*20+" SWAP "+"="*20+'\n'
        swap = psutil.swap_memory()
        out+=f"{'Total:':<20} {self.get_size(swap.total):<45}"+'\n'
        out+=f"{'Free:':<20} {self.get_size(swap.free):<45}"+'\n'
        out+=f"{'Used:':<20} {self.get_size(swap.used):<45}"+'\n'
        out+=f"{'Percentage:':<20} {str(swap.percent)+'%'}"+'\n'
        return out
        
    def disk_info(self):
        out=''
        out+="="*40+" Disk Information "+"="*40+'\n'
        out+='='*20+" Partitions and Usage "+'='*20+'\n'
        partitions=psutil.disk_partitions()
        for partition in partitions:
            out+=f"  === Device: {partition.device} ===\n"
            out+=f"{'  Mountpoint:':<20} {partition.mountpoint:<45}"+'\n'
            out+=f"{'  File system type:':<20} {partition.fstype:<45}"+'\n'
            try:
                partition_usage=psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            out+=f"{'  Total Size:':<20} {self.get_size(partition_usage.total):<45}"+'\n'
            out+=f"{'  Used:':<20} {self.get_size(partition_usage.used):<40}"+'\n'
            out+=f"{'  Free:':<20}{self.get_size(partition_usage.free):20}"+'\n'
            out+=f"{'  Percentage:':<20} {str(partition_usage.percent)+'%'}"+'\n'

        disk_io = psutil.disk_io_counters()
        out+=f"Total read: {self.get_size(disk_io.read_bytes)}"+'\n'
        out+=f"{'Total write:':<20} {self.get_size(disk_io.write_bytes):<45}"+'\n'
        return out

    
    def network_info(self):
        out=''
        out+="="*40+" Network Information "+"="*40
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                out+=f"=== Interface: {interface_name} ==="+'\n'
                if str(address.family) == 'AddressFamily.AF_INET':
                    out+=f"{'  IP Address:':<20} {address.address}"+'\n'
                    out+=f"{'  Netmask:':<20} {address.netmask}"+'\n'
                    out+=f"{'  Broadcast IP:':<20} {address.broadcast}"+'\n'
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    out+=f"{'  MAC Address:':<20} {address.address}"+'\n'
                    out+=f"{'  Netmask:':<20} {address.netmask}"+'\n'
                    out+=f"{'  Broadcast MAC:':<20} {address.broadcast}"+'\n'
        net_io = psutil.net_io_counters()
        out+=f"Total Bytes Sent: {self.get_size(net_io.bytes_sent):<20}"+'\n'
        out+=f"Total Bytes Received: {self.get_size(net_io.bytes_recv):<20}"+'\n'
        return out

    
    def public_ip_information(self):
        ainfo = 'ip hostname city country loc'.split()
        binfo = 'public,rout V,city,country,loc'.split(',')
        r = requests.get(r'https://ipinfo.io/json')
        data="="*40+" Public ip information "+"="*40+'\n'
        for i in range(len(ainfo)):
            try:
                info=r.json()[ainfo[i]]
                info=format(info)
                data+=(f'{binfo[i]:<20}{info:<80}')+'\n'
            except Exception as e :
                print(e)
                pass
        try:
            loc=r.json()['loc']
            loc=format(loc)
            data+=(f'{"map":<20}{"https://www.google.com/maps/search/google+map++" + loc:<80}')+'\n'
        except: 
            pass
        return data
