"""
lab 8
"""

#3.1 and 3.2

my_str = "hello world"


#print(len(my_str.split()))
        
def wordsplit(input_str):
    return len(input_str.split())
    
print(wordsplit(my_str))
  

#3.3

def findmin(inpu_list):
    
    min_item = inpu_list[0]
   
    for num in inpu_list:
            if type(num) is not str:
                if min_item >= num:
                    min_item = num
       
    return min_item

#3.4        
demo_list = [1,2,3,4,5,6]
print(findmin(demo_list))

#3.5
mix_list = [1,2,3,4,"a",6]
print(findmin(mix_list))