#!/usr/bin/env python3
import os
import re
import textract
import sys
from unidecode import unidecode
     
#Open files 
file_pathholder = open("filepaths.txt", 'a+')



thisdir = os.getcwd()
    
#walk through the directories
for root, directories, files in os.walk(thisdir):
    for file in files:
        if file.endswith(".txt"): 
            findarray = []
            try:
                #read lines and search for credit card numbers
                with open(os.path.join(root, file)) as open_file:
                    for line in open_file:
                        #regex for 6 different credit card formats
                        credits = re.findall(r'''4\d{3}\s?\d{4}\s?\d{4}\s?\d{1}\d{3}?|
                        5[1-5]\d{2}\s?\d{4}\s?\d{4}\s?\d{4}|
                        30[0-5]\d{11}|
                        3[68]\d\d{11}|
                        3[47]\d{13}|
                        6011\d{12}|
                        65\d{2}\d{12}
                        ''', line)
                        findarray.extend(credits)
                    if findarray:
                        print(os.path.join(root, file))
                        print(findarray)
            except:
                print ("Could not open file " + os.path.join(root, file))
            file_pathholder.write(os.path.join(root, file) + "\n")
        elif file.endswith(".xlsx") or file.endswith(".XLSX") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".png"):
            text = textract.process(os.path.join(root, file)).decode('utf-8','ignore')
            try:
                text = textract.process(os.path.join(root, file)).decode('utf-8','ignore')
                credits = re.findall(r'''4\d{3}\s?\d{4}\s?\d{4}\s?\d{1}\d{3}?|
                        5[1-5]\d{2}\s?\d{4}\s?\d{4}\s?\d{4}|
                        30[0-5]\d{11}|
                        3[68]\d\d{11}|
                        3[47]\d{13}|
                        6011\d{12}|
                        65\d{2}\d{12}
                        ''', text)
                if credits:
                    print(os.path.join(root, file))
                    print(credits)                  
            except:
                print ("Could not open file " + os.path.join(root, file)) 


#close files
file_pathholder.close()
