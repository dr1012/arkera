from tqdm import tqdm
import numpy as np


def largest_loss(pricelist):
    '''
    This function takes a list of prices and finds the largest loss.

    The first 4 lines of code are not mendotary for the function to work but improve its overall speed as argmax/argmin are much faster to calculate than going through the nested for loops.

    'tqdm' is used to see a progress bar for the operation (in case the nested for loops are actually used).
    '''

    index_max = np.argmax(pricelist)
    index_min = np.argmin(pricelist)
    if(index_max > index_min):
        return pricelist[index_max] - pricelist[index_min]
    else:
        maximum = 0
        for i in tqdm(range(len(pricelist))):
            for j in range(i+1,len(pricelist)):
                    if((pricelist[j]-pricelist[i])>maximum):
                        maximum = pricelist[j]-pricelist[i] 
        return maximum




######### testing ###############

import random
import time

test_prices = []

for i in range(0,10000):
    x = random.randint(1,1000)
    test_prices.append(x)

start = time.time()
result = largest_loss(test_prices)
end = time.time()
print('LARGEST LOSS random sequence: ' + str(result))
print(str(end - start) + ' seconds')


case1 = [1,2,3,4,5,6,7,8,9]
result1 = largest_loss(case1)
case2 = [9,8,7,6,5,4,3,2,1]
result2 = largest_loss(case2)
case3 = [1,1]
result3 = largest_loss(case3)
case4 = [3,5,2,4,11,5,9,10,1]
result4 = largest_loss(case4)

print('LARGEST LOSS case1: ' + str(result1))
print('LARGEST LOSS case2: ' + str(result2))
print('LARGEST LOSS case3: ' + str(result3))
print('LARGEST LOSS case4: ' + str(result4))



