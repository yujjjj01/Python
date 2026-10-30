# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:32:23 2026

@author: user
"""

# ============================課堂練習2-2-1=================================
# # SBP = int(input("請輸入您的收縮壓數值:"))

# # if SBP>140:
# #     print("您的收縮壓偏高，請列入自主健康管理並諮詢醫師")
# # else:
# #     print("您的收縮壓正常")
# ==========================================================================
    
    

# ===========================課堂練習2-2-2==================================
# # WE= float(input("請輸入您的工作年資:"))
# 
# # if WE>=2:
# #     print("符合面試資格")
# # else:
# #     print("資歷尚未達標，您的履歷已存入人才庫備查")
# ==========================================================================


# ========================課堂練習2-2-3=====================================
# goods_price= int(input("請輸入商品單價:"))
# 
# if goods_price>5000:
#     goods_price=goods_price*0.8
# elif goods_price>3000:
#     goods_price=goods_price*0.9
# else:
#     goods_price=goods_price
# print("最後金額總共:","$",goods_price)
# ===========================================================================




# =============================課堂練習2-3-1=================================
# for i in range(10,101,10):
#     print(i)

# for i in range(10,101):
#     if i%10==0:
#         print(i)
# ===========================================================================

# ====================================課堂練習2-3-2==========================
# deposit = 1000
# months = 0
# while deposit<5000:
#     deposit+=500
#     months+=1
# print("需要",months,"個月")
# ===========================================================================


# ====================================綜合練習===============================

print(">>> 歡迎來到黑市太空港自動結帳系統 V3.0 <<<")

# 原始價格
price_list = [4000, 800, 15000, 500, 6200]

# 物品名稱
item_list = ["光束粒子砲", "加速推進劑", "反物質核心",
             "太空乾糧", "隱形匿蹤斗篷"]

# 折扣後價格：大於 2000 打 9 折
discount_price = [int(p * 0.9) if p > 2000 else p
                  for p in price_list]

print("今日特價資產清單：")
for i in range(len(item_list)):
    print(i, item_list[i], "：", discount_price[i], "星幣")

total_bill = 0

# 購買迴圈
while True:
    try:
        choice = int(input("\n請輸入購買商品索引 (0-4)，結帳請按 -1："))

        if choice == -1:
            break

        if 0 <= choice <= 4:
            select_price = discount_price[choice]
            total_bill += select_price
            print("【成功裝載】目前累計金額：", total_bill, "星幣")
        else:
            print("【聯邦警訊】查無此物資代碼，請重新輸入！")

    except ValueError:
        print("【輸入錯誤】請輸入整數編號！")

# 計算階梯優惠
print("\n===== 🚀 交易總結明細 =====")

if total_bill >= 15000:
    total_bill -= 2000
    msg = "梟雄級大宗交易"
elif total_bill >= 8000:
    total_bill -= 800
    msg = "狂徒級買賣"
else:
    msg = "小規模走私"

print("交易評級：", msg)

# 隱密協定
if total_bill % 50 == 0:
    total_bill += 1
    safety_status = "已啟動隱密協定，已加收誘餌訊號費"
    print("【隱密協定】偵測到聯邦雷達共振！已加收 1 星幣發射干擾誘餌！")
else:
    safety_status = "安全，未觸發雷達共振"

# 最終明細
print("安全狀態：", safety_status)
print("【實付星幣總額】：", total_bill, "星幣")
print("===== 交易完成，祝走私順利！ =====")
    






