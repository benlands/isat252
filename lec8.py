"""
lec 8
"""

#def calculate_abs(a):
    
 #   if type(a) is str:
 #       return("wrong data type")
        
   # e#lif a >=0:
      #  return a
      #  
   # else:
      #  return -a
        
    #print(calculate_abs("a"))
    
def cal_sigma(m,n):

    result = 0 
    for i in range(n,m+1):
        result = result +i
    
    return result  

print(cal_sigma(5,3))

def cal_pi(m,n):

    result = 1 
    for i in range(n,m+1):
        result = result +i
    
    return result  

print

def cal_f(m):
    if m==0:
        return 1
    else:
        return m * cal_f(m-1)