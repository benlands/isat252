"""
lab 6
"""
#3.1
for num in range(6):
    if num != 3:
        print(num)

#3.2

five_factorial = 1

for num in range(1,6):
    five_factorial = five_factorial * num
    
print(five_factorial)

#3.3

result_5 = 1
 
for num in range(2,6):
    result_5 = result_5 + num
     
print(result_5)

#3.4

result_34 = 1

for num in range(3,9):
    result_34 = result_34 * num
    
print(result_34)

#3.5

result_35 = 1

for num in range(1,9):
    result_35 = result_35 * num
  
denom = 1
  
for numbers in range(1,4):
    denom = denom * numbers
    
answer_35 = result_35/denom
    
print(answer_35)

#3.6

result_36 = 0
for word in  "this is my sixth string".split():
   result_36 = result_36 + 1
   
print(result_36)

#3.7

my_tweet = {
            "favorite_count":1138,
            "lang":"en",
            "coordinates":(-75,40),
            "entities":{
                        "hashtags":["preds","pens","singinrospring"]
                        
                        }
           
            }
            
result_37 = 0
for hashtag in my_tweet["entities"]["hashtags"]:
    result_37=result_37+ 1
    
print(result_37)