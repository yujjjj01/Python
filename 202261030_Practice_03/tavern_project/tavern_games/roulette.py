# -*- coding: utf-8 -*-

import random

def spin_roulette(bet_color):
    colors=['紅','黑','綠']
    result = random.choice(colors)
    
    if bet_color  == result:
        message = "🎉 恭喜贏得金幣！"
        return (True,result,message)
    else:
        message = "💸 殘念，金幣被酒館收走了！"
        return(False,result,message)
    