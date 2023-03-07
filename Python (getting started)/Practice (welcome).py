print(" Welcome user ")
name1 = input("What is your name user:")
age1 = int(input("What year were you born: "))

actAge = (2023-age1)
print("Hello", name1, "i cant belive you are", actAge, "already!!!")

ready1 = input(
    "Get in the space ship, are you ready for lift off(Yes/No) case senstive:")
ready2 = ready1

if ready2 == "Yes":
    print("Blast off!!!")
else:
    print("Get ready for the count down")
