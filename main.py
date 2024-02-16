import math

a = 0
b = 0
aF = 0
bF = 0
c = 0
cF = 0
cR = 0.0

print("Enter A value:")
numinp1 = input("")
print("Enter B value:")
numinp2 = input("")

a = int(numinp1)
b = int(numinp2)

# DO MATH
aF = a**2
bF = b**2
c = aF + bF
cF = math.sqrt(c)
cR = round(cF, 2)

print("Answer: " + str(cR))
