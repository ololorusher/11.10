import random
import matplotlib.pyplot as plt
import random as rnd
n1=100
n2=1000
n3=10000
n4=100000
rnd.seed(0)
plt.subplot(221)
values=[rnd.normalvariate(0,1) for i in range (n1)]
plt.hist(values, bins=100)

plt.subplot(222)
values=[rnd.normalvariate(0,1) for i in range (n2)]
plt.hist(values, bins=100)

plt.subplot(223)
values=[rnd.normalvariate(0,1) for i in range (n3)]
plt.hist(values, bins=100)

plt.subplot(224)
values=[rnd.normalvariate(0,1) for i in range (n4)]
plt.hist(values, bins=100)
plt.show()

