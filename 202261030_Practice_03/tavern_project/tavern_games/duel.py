# -*- coding: utf-8 -*-

import random

def weapon_clash():
    weapons = ['佩刀', '火繩槍', '水手西洋劍']
    
    player = random.choice(weapons)
    enemy = random.choice(weapons)
    
    if player == enemy:
        message = "🤝 雙方武器相同，平手！"
    elif player == "佩刀" and enemy == "水手西洋劍":
        message = "🎉 玩家獲勝！"
    elif player == "水手西洋劍" and enemy == "火繩槍":
        message = "🎉 玩家獲勝！"
    elif player == "火繩槍" and enemy == "佩刀":
        message = "🎉 玩家獲勝！"
        
    else:
        message = "💀 玩家落敗！"
        
    return(player,enemy,message)
    
    
    