import os
from os import listdir
from os.path import isfile,join

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
        files=str(self.file).split(',')
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