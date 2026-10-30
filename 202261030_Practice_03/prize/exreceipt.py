# -*- coding: utf-8 -*-

import random

def reciept():
    num = random.randint(0,99999999)
    
    result = str(num).zfill(8)
    
    return result