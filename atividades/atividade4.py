A=[0]*10
M=[0]*10
x=2
numero=len(A)
for x in range(numero):
 A[x]=int(input("digite um numero: "))
mult=int(input("Digite o multlipicador: "))
for z in range(numero):
   M[z]=A[z]*mult

print(A)
print(mult)
print(M)