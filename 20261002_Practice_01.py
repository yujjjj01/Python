# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:06:52 2026

@author: user
"""

# =========================input&print練習============================
# celsius_str = float(input ("請輸入現在攝氏幾度:"))
# 
# fahrenheit = celsius_str*(9/5)+32
# 
# print("轉換後的華氏為:",fahrenheit,"度")
# 
# name = input("請輸入您的名字:")
# age  = input("請輸入您的年齡:")
# 
# print(name,"您好~","原來您",age,"歲",sep="",end="")
# print(name,"您好~","原來您",age,"歲",sep="")
# print(f'{name}您好，原來您{age}歲!!')
# print(name+"您好!!原來您"+age+"歲")
# =========================input&print練習============================


# ===========================本金利息練習=============================
# money = int(input("請輸入您的本金多少:"))
# rate  = float(input("年利率是多少:"))
# 
# #第一年
# year1 = money*(1+rate)
# print("第一年本利和:",year1)
# 
# #第二年
# year2 = year1*(1+rate)
# print("第二年本利和:",year2)
# 
# #第三年
# year3 = year2*(1+rate)
# print("第三年本利和:",year3)
# ===========================本金利息練習=============================


# ===========================運算式實作練習-1==============================
# #//& % 的運算練習
# Name = input("請輸入巫師的名字:")
# powder = float(input("請輸入你想加入幾克魔法粉末："))
# 
# TotalLiquidAmount = 150+(powder*2.5)
# beaker = int(TotalLiquidAmount//100)
# smalltesttube = TotalLiquidAmount%100
# 
# print(f"\n嗨，{Name}巫師!調配報告如下:")
# print(f"調配出的藥水總量為: {TotalLiquidAmount} 毫升。")
# print(f"你需要準備: {beaker} 瓶大燒杯。")
# print(f"剩下不滿一瓶的 {smalltesttube} 毫升，請裝在小試管中。")
# ===========================運算式實作練習-1===============================





# ===========================資料容器(List)實作練習-2=======================
# pot = ["草蛉蟲", "雙角獸角粉末", "節肢動物的眼睛", "河童的鱗片"]
# 
# pot.pop() #如果要移除最後一個元素就不用輸入索引位置
# print(pot)
# 
# pot.insert(0, "催狂魔的眼淚")
# print(pot)
# 
# pot[2]="獨角獸的毛"
# print(pot)
# 
# pot.reverse()
# print(pot)
# 
# print("最後大釜清單:",pot)
# ===========================資料容器(List)實作練習-2=======================





#  ===========================資料容器(dict)實作練習-2-1====================
# shop = {"泡麵": 50, "罐頭": 80, "純淨水": 100}
#
# shop["純淨水"] = 300
# print(shop)
#  
# shop["散彈槍子彈"] =500
# print(shop)
# 
# if "泡麵" in shop:
#   print(f"泡麵還有貨！價格是 {shop["泡麵"]} 硬幣")
#  
# del shop["泡麵"]
# print(shop)
#  ===========================資料容器(dict)實作練習-2-1====================





# ===========================資料容器(set)實作練習-2-2=====================
# Roster=["張三", "李四", "王五", "張三", "趙六"]
# Roster1=["李四", "王五", "神祕外星人X", "趙六", "李四"]
# 
# Roster_set=set(Roster)
# print(Roster_set)
# 
# 
# Roster1_set=set(Roster1)
# print(Roster1_set)
# 
# #交集(同時出現的名單)
# print(Roster_set.intersection(Roster1_set))
# #差集(沒有出現在Roster的名單上)
# print(Roster1_set.difference(Roster_set))
# 
# #交集另一種寫法(同時出現的名單)
# print(Roster_set&Roster1_set)
# 
# #差集另一種寫法(沒有出現在Roster的名單上)
# print(Roster1_set-Roster_set)
# ===========================資料容器(set)實作練習-2-2=====================


# ===========================綜合練習======================================
# #使用Dict
# menu = {
#     "珍珠奶茶": 60,
#     "宇宙紅茶": 30,
#     "流星綠茶": 35
# }
# 
# 
# #使用List
# orders = ["珍珠奶茶", "珍珠奶茶", "宇宙紅茶"]
# 
# #Set 任務（計算點了幾種飲料）
# orders_set=set(orders)
# print(f"1.顧客總共點了 {len(orders_set)} 種不同的飲料")
# print("-"*40)
# 
# #Dict 任務（手動查詢價格）
# print(f"2.第一杯飲料價格是:{menu[orders[0]]}元")
# print("-"*40)
# 
# #互動任務（收錢與找零計算）
# Price=int(input("3.請輸入您支付的金額："))
# Total = 150
# change = Price-Total
# print(f"最後找零{change}元")
# ===========================綜合練習======================================




