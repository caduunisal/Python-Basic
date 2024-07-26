
#nome = "Carlos"
#idade = 47
#cidade = "Santa Barbara Doeste"
#
#print(f"Ola!, Meu nome e {nome}, tenho {idade} anos e moro em {cidade}")


#numeros = [10, 20, 30, 40, 50]
#sum = 0
#
#for num in numeros:
#    sum += num
#    
#print(sum / 5)



#gastos_joao = [300, 500, 200, 800]
#gastos_pedro = [200, 300, 500, 700]
#
#tot_joao = sum(gastos_joao)
#tot_pedro = sum(gastos_pedro)
#
#print(tot_joao)
#print(tot_pedro)




#palavras = ["python", "asimov", "código", "web", "programação", "sistematicamente"]
#
#maior = palavras[0]
#menor = palavras[0]
#
#for palavra in palavras:
#    print(palavra)
#    if len(maior) < len(palavra):
#        maior = palavra
#    if len(menor) > len(palavra):
#        menor = palavra
#        
#print("Maior palavra: " + maior)
#print("Menor palavra: " + menor)




def pega_nome():
    nome = input("Digite seu nome: ")
    return "Seja bem vindo, " + nome.title() + "!"
    
print(pega_nome())









# ------------------------------------------------- Python Course ----------------------------

#print("Just a test")
#print("Learning Python")

#add = 2+2       #4
#expo = 2**3     #8
#modu = 7
#modu %= 3       #1
#assig = 5       
#assig += 7      #12
#val = ( 2.557 * 3.2 )
#val1 = round ( val, 2)

#print(add)
#print(expo)
#print(modu)
#print(assig)
#print(2 + 2 * ( 6 / 3 ))  #8
#print(val)
#print(val1)

#sum = (16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39) * 100
#print(sum / 100)

#sum = (16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39)
#print (round (sum, 2))

# Strings

#str = "Carlos"
#print (str[1])          # a
#print (str[0:3])        # Car
#print (str[:2])         # Ca
#print (str[2:])         # rlos
#print ("Python"[2])


#concatenated = "Carlos" + " " + "Eduardo"
#print (concatenated)
#print (concatenated[3])
#print (concatenated[1:4])


#str = "Just do it!"
#print (str[10])
#print (str[5:7])
#print (str[8:11])
#print (str[:4])
#print ("Don't" + " " + str[5:])

#var1 = 1.23
#var1 = str(1.23)
#var2 = "Linux"

#print (type (var1))
#print (type (var2))


#name = "Carlos"
#welcome = "Hello, my name is " + "\'" + name + "\'!"
#print (welcome)

#print ("*******\n *****\n  ***\n   *")

#number = int (input ("Type an number: "))
#print ("Welcome, " + name + "!")
#print (type (number))

#number = int (input ("Enter an integer: "))
#print (number + 10)


#def new_func (v1=10, v2=20):
#    return v1 + v2
#    
#    
#print ("Value: " + str(new_func(5) + 5))


#def hello_world_printer():
#    print ("Hello world!")
#
#    
#hello_world_printer()


#def name_printer(name):
#    print ("Hello, " + name)
#
#name = input ("Type your name: ")
#name_printer(name)


#def vol_calc(lenght, width, height):
#    vol = int(lenght) * int(width) * int(height)
#    print ("Volume in Cubic Feet: " + str(vol))
#    
#    
#lenght = input ("Lenght: ")
#width = input ("width: ")
#height = input ("Height: ")
#vol_calc(lenght, width, height)


#import random
#print (random.randint(1, 10))

#from random import *
#print (random())

#---------------------------------------------------------------------------
#import random
#import math
#gallons = random.randint(10, 25)
#miles = random.randint(200, 400)
#mil_gal = (int(miles) / int(gallons))
#
#print ("Gallons: " + str(gallons))
#print ("Miles: " + str(miles))
#print ("Miles per gallon: " + str(math.floor(mil_gal)) + "\n")

#---------------------------------------------------------------------------


#---------------------------------------------------------------------------

#print ( 1 == 1 )
#print ( 2 < 1 )

#name = input ("Type your name: ")
#
#if name == "Carlos":
#    print ("Welcome, " + name + "!")
#else:
#    print ("Welcome, user!")


#score = int(input("Type the score: "))
#
#if score >= 90:
#    print ("Grade A")
#else:
#    if score >= 80 and score < 90:
#        print ("Grade B")
#    else:
#        if score >= 70 and score < 80:
#            print ("Grade C")
#        else:
#            if score >= 60 and score < 70:
#                print ("Grade D")
#            else:
#                print ("Grade F")
                
                
                
#score = int(input("Type the score: "))
#
#if score >= 90:
#    print ("Grade A")
#elif score >= 80 and score < 90:
#    print ("Grade B")
#elif score >= 70 and score < 80:
#    print ("Grade C")
#elif score >= 60 and score < 70:
#    print ("Grade D")
#else:
#    print ("Grade F")
#              


#import random
#
#number = random.randint(1, 10)
#print(number)
#
#if number == 1:
#    print("|")
#elif number == 2:
#    print("||")
#elif number == 3:
#    print("|||")
#elif number == 4:
#    print("|V")
#elif number == 5:
#    print("V")
#elif number == 6:
#    print("V|")
#elif number == 7:
#    print("V||")
#elif number == 8:
#    print("V|||")
#elif number == 9:
#    print("|X")
#else:
#    print("X")
    

#---------------------------------------------------------------------------


#count = 10
#
#while count != 0:
#    print (str(count) + "\n")
#    count -= 1
 

#number = int(input("Enter an integer: "))
#number1 = number
#
#sum = 0
#while number > 0:
#    sum += number
#    number -= 1
#    
#print("The sum of " + str(number1) + " is " + str(sum))


#---------------------------------------------------------------------------


#word = "Learning Python!"
#
#sum = 0
#for letter in word:
#    #print(letter)
#    sum += 1
#    
#print("'" + word + "'" + " have " + str(sum) + " characters")
 

#str = range(1,50)
#
#for num in str:
#
#    if num % 3 == 0:
#        print(f"The number {num} is divisible by 3")

    
#---------------------------------------------------------------------------

#str = "carlos eduardo ramos"
#print("All UPPER: " + str.upper())
#print(str)
#str = "CARLOS EDUARDO RAMOS"
#print("All LOWER: " + str.lower())
#print(str)
 

#str = "carlos eduardo ramos"
#print(str.split())


#mixed_case = "A Song of Ice and Fire"
#print(mixed_case.isupper())
#print(mixed_case.islower())
#
#print(mixed_case.upper())
#print(mixed_case.lower())
#
#print(mixed_case.istitle())
#
#title_case  = mixed_case.title()
#print(title_case)
#
#print(mixed_case.startswith("a"))
#print(mixed_case.endswith("E"))
#
#words  = mixed_case.split()
#print(words)
#
#print("-".join(words))
#
#print("".join(words).isalpha())

#str = "Carlos Ramos"
#print(str.ljust(20))
