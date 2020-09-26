from bs4 import BeautifulSoup
from docx import Document
import os
import requests
import webbrowser
import wget
import csv  

    
 
 
''' 
code=''
course=''
course_code=input().upper().replace(' ','')
for i in course_code:
    if i.isdigit()==True:
        code+=i
    elif i=='X':
        code+=i
    else:
        course+=i
'''
CSE=['100','101','102',"131",'201','220','231','232','260','291',
     '320','325','331','335','402','404','410','415','420','422','425',
     '429','431','435','440','450','460','471','472','473','476','480',
     '482','484','491','498']
SCM=['303','304','371','372','373','460','461','462','463','470','471','472','474',
     '475','476','479','490','491']
MTH=['132','133','234','235','299','309','310','320','314']
REL=['220','101','306']

code=REL
course='REl'

path = os.path.join(os.getcwd(), course) 
 
#os.mkdir(path)
with open ('course.txt','w') as txt:
    
    for i in code:
        
      
     
        url = "https://msugrades.com/course/{}/{}".format(course,i)
        
        
        r = requests.get(url)
        soup=BeautifulSoup(r.text,'lxml')
        content=soup.body.find('div',id='grade-content')
        i=1
        list_length=len(content.find_all('div',class_='tab-pane fade'))
        course_title=content.find('div',id='tab0').h3.text
         
        txt.write(str(course_title))
        txt.write("\n\n")
        
        
        
        while i<=list_length:
            
           
            div=content.find('div',id='tab'+str(i))
            data={}
            prof=div.h3.text
            prof_info=str(div.find_all('p')[1].text).replace('\n',' ')
            data[prof]=prof_info
            final=str(data).replace("{",'').replace('}','  ').replace("'",'')
            
            txt.write(final)
            txt.write("\n\n")
            i+=1
            #csv_path=os.path.join(path,str(course_title)+'.docx')
            #csv.save(csv_path)

       
     

 

    
    
    
 
    
 
    
    
     
 


 


 




 
 
 
 
    
 


 

