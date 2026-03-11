P = int(input("enter tha P value :"))
R = int(input("enter tha R value :"))
T = int(input("enter tha T value :"))

A = P * (1 + R/100) ** T
CI = A - P

print("Compound interest:", CI)