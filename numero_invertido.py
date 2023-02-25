print("------------------------------------")
print("-------- NÚMEROS INVERTIDOS --------")
print("------------------------------------")
n =input("Digite un número de tres cifras ")
n = int(n)

n1 = (n % 10) * 100
n2 = ((n % 100)//10) * 10
n3 = (n % 1000)//100

ni = n1 + n2 + n3
print("El número inverso es: "+ str(ni))