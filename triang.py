

def edges(a, b, c):  
      if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return False
    else: 
        return True        
a = 2
b = 4
c = 6
if edges(a, b, c): 
    print("Valid")  
else: 
    print("Invalid") 


