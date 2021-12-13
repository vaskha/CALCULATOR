r1= int(input("Ilk sayıyı giriniz : "))
r2= int(input("Ikinci sayıyı giriniz :  "))
hell= str(input("Islemi seciniz (+,-,*,/):  "))
if hell == "+":
    print(r1 + r2)
elif hell == "-":
    print(r1 - r2)
elif hell == "*":
    print(r1 * r2)
elif hell == "/":
    print(r1 / r2)
else:
    print("Dogru islem seciniz")
 
