#Euclids ALgorithm
m = int(input())
n = int(input())
prod=m*n
while(n>0):
    rem=m%n
    m=n
    n=rem
gcd=m
print(f"HCF={gcd} LCM={prod//gcd}")