import csv  
from bs4 import BeautifulSoup
from docx import Document
import os
import requests
import webbrowser
import wget

target_name='result.txt'
file_name="scm.csv"
final=[]
with open(file_name, 'w') as csvfile:  
    csvwriter = csv.writer(csvfile) 
    with open (target_name) as t:
            for i in t:
                if len(i.split())!=0 and len(i.split())>4:
                    if i.split()[2]=='Average':
                        csvwriter.writerow(["Professor"+"  "+"Name: ",i.split()[0]+"   "+
                                            i.split()[1][:-1]])
                    else:
                        
                        csvwriter.writerow(["Professor"+"  "+"Name: ",i.split()[0]+"   "+
                                            i.split()[2][:-1]])
                    
                    if i.split()[6].isalpha()==True:
                        #print(i.split()[5])
                        csvwriter.writerow(["Average"+"  "+"Grade: ",i.split()[5]])
                    else:
                        #print(i.split()[6])
                        csvwriter.writerow(["Average"+"  "+"Grade: ",i.split()[6]])
                    #print(i.split()[-3])
                    csvwriter.writerow(["Median"+"  "+"Grade: ",i.split()[-3]])
                if len(i.split())==4:
                    csvwriter.writerow("\n\n\n")
                    csvwriter.writerow([i.split()[0]+"  "+i.split()[1]+"   "+i.split()[3]])
                    csvwriter.writerow("\n\n\n")
                        
            

# writing to csv file  

    # creating a csv writer object  
     
        
    # writing the fields  
    #csvwriter.writerow(fields)  
        
    # writing the data rows  
    
