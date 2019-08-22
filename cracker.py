# Simple ZIP file Cracker 1.1v
# 

import zipfile
import multiprocessing as mp
import os
from sys import exit
from time import sleep



class ZIP_cracker:

    def __init__(self,wordlist,ziped):

        self.wordlist = wordlist
        self.ziped = ziped


    def Extract(self,zip,password):

        if os.path.exists("Cracked"):
            pass
        else:
            os.system("mkdir Cracked")
        try:
            zip.extractall(path="Cracked/",pwd=password)
            print("\nPassword Found: "+password.decode())
            exit()
        except :
            pass

    def Main(self):

        print("\n\nSmall Zip crcker 1.0 ")
        print("\tNote: curnch tool is great to create powerful password\n\n")
        sleep(1)
        zip = zipfile.ZipFile(self.ziped)
        list = open(self.wordlist,'r').readlines()
        for password in list:
            x = password.replace("\n","").encode()
            print("testing :"+x.decode())
            process = mp.Process(target=self.Extract,args=(zip,x))
            process.start()
            

file = str(input("zip File>>>"))
wordlist = str(input("wordlist>>>"))
ZIP = ZIP_cracker(wordlist,file)
ZIP.Main()
