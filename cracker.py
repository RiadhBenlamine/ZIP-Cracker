# ZIP file Cracker 1.3V
# written by Riadh Benlamine
###################################################### Report me for any bug or error .                  ######################################################

__author__ = "Riadh Benlamine"
__version__ = 1.2


import zipfile
import multiprocessing as mp
import os
from sys import exit
from time import sleep



class ZIP_cracker:
    ''' ZIP cracker class '''
    def __init__(self,wordlist,ziped):
        ''' Initialize this class '''
        self.wordlist = wordlist
        self.ziped = ziped


    def Extract(self,zip,password):
        ''' Here the passwords will be tested '''
        try:
            zip.extractall(path=".",pwd=password)
            print("Passowrd : ",password.encode())
            exit()
        except :
            pass

    def Main(self):
        ''' Program Main '''
        print("\n\n Zip crcker 1.2 ")
        print("\tNote: curnch tool is great to create powerful password\n\n")
        print("You will Be notifited if the password is found , just let the program run.\n")
        sleep(1)
        try:
            zip = zipfile.ZipFile(self.ziped)
            wordlist = open(self.wordlist,'r').readlines()

            def DEL(LIST):
                ''' Delete any item is taken by part_(one,two,three,four) '''
                for item in LIST:
                    wordlist.remove(item)

            part_one = wordlist[:(len(wordlist)//6)]
            DEL(part_one)
            part_two = wordlist[:(len(wordlist)//4)]
            DEL(part_two)
            part_three = wordlist[:(len(wordlist)//2)]
            DEL(part_three)
            part_four = [ item for item in wordlist ]

            def brute(PART):
                ''' Brute force '''
                for password in PART:
                    x = password.replace("\n","").encode()
                    Process = mp.Process(target=self.Extract,args=[zip,x])
                    Process.start()

            p1 = mp.Process(target=brute,args=[part_one])
            p2 = mp.Process(target=brute,args=[part_two])
            p3 = mp.Process(target=brute,args=[part_three])
            p4 = mp.Process(target=brute,args=[part_four])

            p1.start()
            p2.start()
            p3.start()
            p4.start()

        except FileNotFoundError:
            print("Zip or Wordlist file not Found")
                
            

file = str(input("zip File>>>"))
wordlist = str(input("wordlist>>>"))
ZIP = ZIP_cracker(wordlist,file)
ZIP.Main()
