valor = (input("ingrese ºC o ºF")).upper()
temp = input("ingrese temp")
print(valor)

if valor == "F":
        c=(float(temp) - 32 )* 5/9
        print(f"la temperatura es de {c} celcius")        
             
elif valor == "C":
        f=(9/5)* int(temp) + 32
        print(f"La temperatura es de {f} faengeit")

else: print("es c ó f tontito")
    
     




