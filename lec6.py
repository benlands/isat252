"""
lec 6
"""

demo_str = "this is my string"

#for str_item in demo_str:
  #  print(str_item)
  
#for word_item in demo_str.split():
   # print(word_item)
    #print(word_item.title())
    #for str_item in word_item:
       # print(str_item)
    #if word_item != "my":
        #print(word_item)
        
for each_num in range(5):
    print(each_num)
    
#for each_num in range(1,5):
    #print(each_num)
    
#for each_num in range(1,5,2):
   # print(each_num)
   
num_list = [213,321,123,312]

max_item = num_list[0]

for num in num_list:
    if max_item <= num:
        max_item = num
        
print(max_item)