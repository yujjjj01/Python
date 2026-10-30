# -*- coding: utf-8 -*-

from tavern_games import roulette,duel
import announcer as spk


def run_game():
    spk.speak("歡迎來到黑鬍子酒館！準備好賭上你的海賊榮耀了嗎？")
    win,color,message = roulette.spin_roulette("紅")
    spk.speak(f"輪盤開出的顏色：{color}")
    spk.speak(message)
    
    player,emeny,message = duel.weapon_clash()
    spk.speak(f"玩家武器：{player}")
    spk.speak(f"對手武器：{emeny}")
    spk.speak(message)

if __name__ == '__main__':
    run_game()