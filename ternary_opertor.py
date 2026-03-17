x = int(input("enter first number :"))
y = int(input("enter second number :" ))
z = int(input("enter third number :"))
min = x if x<y and x<z else y if y<z else z
print("smallest number",min)
