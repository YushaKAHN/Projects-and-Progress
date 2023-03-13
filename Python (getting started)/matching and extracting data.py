import re
x = "My 2 favoruite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)


# greety madtching
# chooses the largest stamp templete
xy = "From:Using the : characters"
yx = re.findall("<F.+~.", xy)
print(yx)
