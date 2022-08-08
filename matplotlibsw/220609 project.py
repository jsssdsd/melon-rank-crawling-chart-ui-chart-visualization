from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
import time as t
import os
from selenium.webdriver.common.keys import Keys
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

data=read_csv("melon2020.csv",encoding='utf-8')
data1=read_csv("melon2021.csv",encoding='utf-8')

a=data1['순위']
aval=a.values


def plus(x):
    return x+50

result=data1['순위'].apply(plus)

data1['순위']= data1['순위'].replace(aval.tolist(),result)
df= merge(data,data1,how='outer')
print(df)
df.to_csv('melon_all.csv')



data_all=read_csv("melon_all.csv",encoding='utf-8')

while True:
    search=input("검색 년 입력:")
    if search=="2020":
        data = read_csv("melon2020.csv", encoding='utf-8')
        while search:
            rank = input("순위검색 or 가수검색:")
            if rank=="순위":
                InputRank = input("순위입력")
                try:
                    result0 = data.loc[data['순위'] ==int(InputRank)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            elif rank=="가수":
                InputSinger = input("가수입력")
                try:
                    result0 = data.loc[data['가수명'] == InputSinger]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            else:
                print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
                print("*" * 200)
                continue
    elif search=="2021":
        data1 = read_csv("melon2021.csv", encoding='utf-8')
        while search:
            rank = input("순위검색 or 가수검색:")
            if rank == "순위":
                InputRank = input("순위입력")
                try:
                    result0 = data.loc[data['순위'] == int(InputRank)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            elif rank == "가수":
                InputSinger = input("가수입력")
                try:
                    result0 = data.loc[data['가수명'] == InputSinger]
                    print(result0)
                    break
                except:
                    print("잘못 입력하셨습니다.")
                    continue
            else:
                print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
                print("*" * 200)
                continue
    else:
        print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
        print("*"*200)
        continue