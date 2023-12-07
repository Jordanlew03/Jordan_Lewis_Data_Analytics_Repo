#Jordan Lewis
import math
num_stores = int(input())
sales = []


for num in range(1, num_stores + 1):
    s = int(input())
    sales.append(s)
print('SALES BAR CHART')
for (pos, s) in enumerate(sales):
    num_atr = '*' * math.ceil(s/100)
    print(f'Store {pos + 1}: {num_atr}')
    
    

