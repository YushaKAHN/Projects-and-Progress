def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40:
        reg = hours*rate
        otp = (hours - 40)*(rate*0.5)

        pay = reg+otp
    else:
        pay = hours * rate
        print("Pay:", pay)
       # print("Returning", pay)
        return pay


aa = input("Enter Hours:")
bb = input("Enter Rate:")

aaa = float(aa)
bbb = float(bb)
xp = computepay(aaa, bbb)
print("Pay:", xp)
