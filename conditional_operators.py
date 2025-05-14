if True:    
    print("Hello, world")

#Hello, world    
if False:    
    print("Hello, world")
#Nothing

x=10
if x>0:
    print("x is positive")
#x is positive    
y=0
if y>0:
    print("x is positive")
elif y < 0:
    print("x is negative")
else:   
    print("x is zero")     
#x is zero

z = 10
i = 20
if z > 0 and i > 0: 
    print("z and i are pozitive")
#z and i are pozitive

message = "Hello, world"
if message: 
    print("message is not empty")    
#message is not empty

year =2001

if year %4 == 0 and year % 100 != 0:
    print("Year is leap")
elif year % 400 == 0:
    print("Year is leap")   
else:     
    print("Year is not leap")

#Year is not leap
year1 =2000
if not year1 %4  and year1 % 100 :
    print("Year is leap")
elif not year1 % 400:
    print("Year is leap")   
else:     
    print("Year is not leap")

#Year is leap