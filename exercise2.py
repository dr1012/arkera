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
    x = random.randint(1,10000)
    test_prices.append(x)

start = time.time()
result = largest_loss([test_prices])
end = time.time()
print('LARGEST LOSS: ' + str(result))
print(str(end - start) + ' seconds')



