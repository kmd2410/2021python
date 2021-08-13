from random import *

numb = range(1,46)
numbb = list(numb)
shuffle(numbb)
numbbb = sample(numbb,6)
print("로또번호생성기 : {0}".format(numbbb[1:]))
print("보너스번호 : {0}".format(numbbb[0]))
