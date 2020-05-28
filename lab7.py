"""
lab7
"""
#3.1
i = 6
while i>0:
    i= i - 1
    if i == 3:
        continue
    print(i)
    
#3.2
p = 1
result = 1
while p <=5:
    result = result *p
    p=p+1
print(result)

#3.3
L = 1
result_33 = 0
while L <=5:
    result_33 = result_33 +L
    L=L+1
print(result_33)

#3.4
R = 3
result_34 = 1
while R <=8:
    result_34 = result_34 *R
    R=R+1
print(result_34)

#3.5
W = 1
result_35 = 1
while W <=8:
    result_35 = result_35 *W
    W=W+1
    
D = 1
result_35b = 1
while D  <=3:
    result_35b = result_35b *D
    D=D+1
    
print(result_35/result_35b)

#3.6
num_list = [12,32,43,35]

while num_list:
    num_list.remove(num_list[0])
    print(num_list)
    