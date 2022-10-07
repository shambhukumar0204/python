print ('Enter number of element ')
n = int(input)
a = []
for i in range(n):
    print ('Enter {0} element '.format(i +1))
    ele = int(input())
    a.append(ele)
print('Enter of list are :',a)
print('Enter of list to search :')
key = int (input())
res = a.count(key)
if (res == 0):
    print ('not round')
else:
    print('Element present {0} times',res)
        
    

