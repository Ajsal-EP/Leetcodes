m = int(input())
n = int(input())
HCF=1
for i in range(2,m+1):
    if(m%i==0 and n%i==0):
        HCF=i;
LCM = int((m*n)/(HCF))
print(f"HCF={HCF} LCM={LCM}")