import socket
from socket import getservbyname, getservbyport

class Scanner_ports():
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.baners_verision=[]
        self.counter=0
        self.out_data=''
           
        
    def port_scaner(self,host,port):
        try:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            sock.connect((host,port))
            try:
                service_baner = sock.recv(1024).decode()
                self.baners_verision.append(service_baner.replace('\n','').replace('\r','')+' on host '+host)
            except:
                service_baner=''
            try:
                port_name = getservbyport(port)
            except:
                port_name = ''
            print('{+}'+' port '+port_name+' '+str(port)+" is open! "+service_baner[:-1])
            self.out_data+='{+}'+' port '+port_name+' '+str(port)+" is open! "+service_baner[:-1]+'\n'
            self.counter=1

        except socket.error:
            pass


    def get_host_name(self,name): 
        host_by_name=socket.gethostbyname(name)
        return host_by_name


    def range_of_ports(self,strat_range_port,end_range_port,host):
        strat_range_port=int(strat_range_port)
        end_range_port=int(end_range_port)
        host=self.get_host_name(host)
        self.out_data+=('\nscannig for open ports on '+host+'...\n')
        self.out_data+=('='*50)+'\n'
        for i in range(strat_range_port,end_range_port+1):
            self.port_scaner(host,i)
        if self.counter==0:
            self.out_data+=("not found..")+'\n'
        self.counter=0
        self.out_data+=('-'*50)+'\n'
            



    def ip_range(self,start_ip,end_ip):
        start_ip=start_ip.split('.')
        end_ip=end_ip.split('.')

        list_ip_range=[]
        for i in range(len(start_ip)):
            if start_ip[i]!=end_ip[i]:
                if i == 3:
                    for n in range(int(start_ip[i]),int(end_ip[i])+1):
                        end_ip[i]=str(n)
                        list_ip_range.append(str(end_ip)[1:-1].replace(', ','.').replace("'",''))
                    break

                if i == 2:
                    for n in range(int(end_ip[i])):
                        end_ip[i]=n
                        for j in range(255):
                            end_ip[i+1]=j
                            list_ip_range.append(str(end_ip)[1:-1].replace(', ','.').replace("'",''))
                    break
        return list_ip_range


    def scaning_for_ports_open(self): 
        
        if '-'in self.host:
            if '-'in self.port:
                self.port=self.port.split('-')
                start_port=self.port[0]
                end_port=self.port[-1]
            else:
                start_port=int(self.port)
                end_port=self.port
            host=self.host.split('-')
            start_ip=host[0]
            end_ip=host[-1]
            ranges=self.ip_range(start_ip,end_ip)
            for i in ranges:
                 self.range_of_ports(start_port,end_port,i)
            self.out_data+=('end.')+'\n'
    
        else:
            if '-'in self.port:
                self.port=self.port.split('-')
                start_port=self.port[0]
                end_port=self.port[-1]
            else:
                start_port=int(self.port)
                end_port=self.port
                
            host=self.get_host_name(self.host)
            self.range_of_ports(start_port,end_port,host)
            self.out_data+=('end.')+'\n'
        return self.out_data
            
            
            
    
    def scan_for_vulnerabilities(self,path):
        vulnerabilities=[]
        with open(path,'r')as file:
            for i in file:
                vulnerabilities.append(i.replace('\r','').replace('\n',''))
        
        self.scaning_for_ports_open()
        p=len(self.baners_verision)-1
        self.out_data+=('\n\nvulnerabilities')+'\n'
        self.out_data+=('='*50)+'\n'
        count=0

        for i in self.baners_verision:
            v=str(i).split(' on host')
            v=v[0]
            if v in vulnerabilities:
                self.out_data+=(i)+'\n'
                count=1
        if count==0:
            self.out_data+=('not found vulnerabilities')
        return self.out_data

def main():
    v=str(input("to scan for ports enter 1 for ports and vulnerabilities enter full path of vulnerabilitie list: "))
    p=input('\n\nTo scan for one target and one port enter ip, port (ex:192.167.1.1, 80)\nto scan range of ports enter ip, start_port-end_port (ex: 192.167.1.1, 0-500)\nto scan multiple targets enter start_ip-end_ip ,port/start_port-end_port (ex:10.0.0.1-10.0.0.6, 0-500:\n')
    p=p.split(',')
    if v=='1':
        print(Scanner_ports(p[0],p[-1]).scaning_for_ports_open())
    else:
        print(Scanner_ports(p[0],p[-1]).scan_for_vulnerabilities(v))


if __name__=='__main__':
    main()
