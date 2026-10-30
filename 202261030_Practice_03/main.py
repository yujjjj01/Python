# -*- coding: utf-8 -*-


# =================================ex02===================================
# import exlotto

# numbers=exlotto.lotto(48, 6)

# numbers.sort()

# print(numbers)
# =================================ex02===================================


# ================================ex03====================================
# from exlotto import lotto

# numbers =lotto(48,6)

# print(sorted(numbers))
# =================================ex03===================================


# =================================ex04===================================

# import exlotto as ex

# numbers = ex.lotto(46, 8)

# print(sorted(numbers))

# =================================ex04===================================


# =================================ex06===================================
from prize import exlotto,exreceipt

lottos = exlotto.lotto(48,6)
receipt = exreceipt.reciept()

print(sorted(lottos,reverse=True))
print(receipt)


# =================================ex06===================================