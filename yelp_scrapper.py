import requests
import pandas as pd
import xlwt
import xlrd
import time
import os
from bs4 import BeautifulSoup
loc=''
def m(loc):
    base_url="https://www.yelp.com/search?find_desc=Restaurants&find_loc="
    page=0
    url=base_url + loc + "&start=" + str(page)
    yelp_r=requests.get(url)
    yelp_soup=BeautifulSoup(yelp_r.text,'html.parser')
    my_data=[]
    while page<201:
        buss=yelp_soup.find_all('div',{'class':'biz-listing-large'})
        for biz in buss:
            d={}
            
            
            title=biz.find_all('a',{'class':'biz-name'})[0].text
            
            addres=biz.find_all('address')[0].text.replace(' ','')
         
            phone=biz.find_all('span',{'class':"biz-phone"})[0].text.replace(' ','')
            d['ALL_name']=title
            d['Full adress']=addres
            d['Phone']=phone
            my_data.append(d)
        page+=10
    return my_data
l=input("Enter the location: ")
time.sleep(1)
print("Please Wait::")
result=m(l)
time.sleep(2)


info=pd.DataFrame(result)
info.columns=['Full name','Adress','Mobile no']
info.to_excel('C:\Python34\{}_file.xls'.format(l))
print('Your file is ready:-')
print('If you want to see that press y otherwise press n:')
ch=input()
f='C:\Python34\{}_file.xls'.format(l)
if ch=='y':
    print('Please wait:: --')
    os.startfile(f)
    

if ch=='n':
    print("Thank you!")
