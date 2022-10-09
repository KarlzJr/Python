fset1 = frozenset([1,2,3,4,5,5,5])
print(fset1)

for item in fset1:
    print(item, end=" ")
fset2 = frozenset([1,10])
for item in fset2:
    if item in fset1:
        print(f"{item} is in both sets.", end=" ")  # " " is a space
    else:
        print(f"{item} is only in set 2.", end=" ") # " " is a space

