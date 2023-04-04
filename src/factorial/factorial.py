#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

#numero = input("ingrese un numero para calcular su Factorial!")
input("\nBienvenido/a! \nEste Script le permitirá Calcular el Factorial de un número. Continuamos?")

numero = int(input("\nPor favor, a continuacion Ingrese un numero: "))

#input("\nPor favor, a continuacion Ingrese un numero: ")

#if len(sys.argv) == 0:
if(numero < 0):
   print("Por favor, ingrese un numero Mayor a 0!")
   sys.exit()
#num=int(sys.argv[1])
else:
    num=numero
    print("Factorial ",num,"! es ", factorial(num)) 

