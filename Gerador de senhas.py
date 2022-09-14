#caracteres maiúsculos e minúsculos 
#símbolos e espaços

""" 
Security = chave
5ecur1ty = senha

hexadecimais:
1 = 1
2 = 2 até 9 = 9
10 = A
11 = B 
12 = C
13 = D
14 = E
15 = F
"""


chave = input("Digite a base de sua senha, logo ela sera convertida em números e símbolos para que fique mais segura! : ")

senha = ""#string

for letra in chave:
    if letra in "Aa":
        senha = senha + "4"
    
    elif letra in "Bb":
        senha = senha + "Bb"    
   
    elif letra in "Cc":
        senha = senha + "c"  
   
    elif letra in "Dd":
        senha = senha + "d"  
    
    elif letra in "Ee":
        senha = senha + "3"  
   
    elif letra in "Ff":
        senha = senha + "f"  
   
    elif letra in "Rr": 
        senha = senha + "#"
    
    elif letra in "Ss": 
        senha = senha + "$"
        
    elif letra in "Oo": 
        senha = senha + "0"
    
    elif letra in "Mm": 
        senha = senha + "m"
    else: senha = senha + letra
    
    
    

print("sua senha covertida em números e símbolos é: ", senha)

