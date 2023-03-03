aaa = input(" Enter how many hours worked:")
bbb = input("Enter rate:")

try :
    aaa1 = float(aaa)
    bbb1 = float(bbb)

except: 
    print(" Error this is not a number ")
    quit()


#print(aaa1,bbb1)

if aaa1 > 40 :
    
    
    #print("Overtime")
    reg = aaa1 * bbb1
    otp = (aaa1 - 40)  * (bbb1 * 0.5)
    
    #print (reg , otp)
    xp = reg + otp
else:
    xp =aaa1*bbb1
print("Pay :",xp)
