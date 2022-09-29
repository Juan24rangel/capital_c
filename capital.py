#  capital

# input
("Halle en cuantos meses se duplica el valor del capital.")

C = int (input("Digite el capital: "))
#processing
B = 2*C
n = 0
while C < B:
    C = 1.05 * C
    n = n+1
    
#output
print("Meses en que se duplica: "+str(n))