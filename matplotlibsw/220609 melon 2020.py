from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
import time as t
import os
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import matplotlib.pyplot as plt
import numpy as np
#pyplot 모듈은 함수의 모음
#그래프를 만들 수 있다.
import pandas as pd
from pandas import *
#한글 깨짐문제 해결 메소드
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
f=open("melon2020.csv","w",encoding='UTF-8')
f.write("순위,곡명,가수명,좋아요,\n")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020")


xpath1="/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
xpath3="]/td[4]/div/div/div[1]/span/strong/a"
xpath4="/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
xpath5="]/td[4]/div/div/div[2]/div[1]/a"
xpath6="/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
xpath7="]/td[5]/div/button/span[2]"
list1=[]
for xpath2 in range(1, 51):
    xpath100 = xpath1 + str(xpath2) + xpath3
    xpath101 = xpath4 + str(xpath2) + xpath5
    xpath102 = xpath6 + str(xpath2) + xpath7
    print(str(xpath2))
    print("곡명: %s" % driver.find_element(By.XPATH, xpath100).text)
    print("가수명: %s" % driver.find_element(By.XPATH, xpath101).text)
    print("좋아요: %s" % driver.find_element(By.XPATH, xpath102).text.replace(",",""))
    x=driver.find_element(By.XPATH, xpath100).text.replace(",","")
    y=driver.find_element(By.XPATH, xpath101).text.replace(",","")
    z=driver.find_element(By.XPATH, xpath102).text.replace(",","")
    f.write(str(xpath2)+","+x+","+y+","+z+","+"\n")
    list1.append(xpath2)
f.close()
data=read_csv("melon2020.csv",encoding='utf-8')

print("1~50위 사이 가장 많이 순위권에 포함된 가수 : %s" % data.value_counts('가수명').idxmax())

print("가수별 순위에 몇번 등록되었는가")
print(data.value_counts('가수명'))


a=data.value_counts('가수명').head(5)
x=np.arange(5)
objects=a.index
values=np.array(a[0:].tolist())
colors=['orange','pink','green','blue','purple']
plt.ylim([0,10])
plt.bar(x,values, color=colors)
plt.xlabel('가수명')
plt.ylabel('횟수')
plt.xticks(x,objects,fontdict={'size':7})
plt.title('가장 많이 랭크된 가수 TOP 5')
plt.show()

print("전체 가수의 좋아요 평균 : %s" % data['좋아요'].mean())

