s1 = (input("enter the string 1 :"))
s2 = (input("enter the string 2 :"))

res = len(set(s1.lower()) & set(s2.lower()))
print(res)