#TRY_AND_EXCEPT_practical_Practice

a = input(" Enter a number:")

try:
    ival = int(a)
except: 
    ival = -1
    
if ival > 0 :
    print("nice work")

else:
    print("Not a number ")