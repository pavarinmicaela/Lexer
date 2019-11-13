#Gramatica Lexicografica#


estado_trampa = -1
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_ACEPTADO = "ESTADO ACEPTADO"
RESULTADO_NO_ACEPTADO = "ESTADO NO ACEPTADO"


def d_eof(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == 'e':
        return 1
    if estado_anterior == 1 and caracter == 'o':
        return 2
    if estado_anterior == 2 and caracter == 'f':
        return 3
   
    return estado_trampa 

def A_eof(cadena):
    finales = [3]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_eof(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA

    if estado_actual in finales:
            return RESULTADO_ACEPTADO
             
    return RESULTADO_NO_ACEPTADO


def d_fun(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "u": 
        return 2
    if estado_anterior == 2 and caracter == "n":
        return 3 
    
    return estado_trampa

def A_fun(cadena):
    finales = [3]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_fun(estado_actual,caracter)
        estado_actual = estado_proximo 
        
        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
           
    if estado_actual in finales:
            return RESULTADO_ACEPTADO 

    return RESULTADO_NO_ACEPTADO 


def d_parI(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "(":
        return 1
    
    return estado_trampa

def A_parI(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_parI(estado_actual,caracter)
        estado_actual = estado_proximo
        
        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_parII(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ")":
        return 1
    
    return estado_trampa

def A_parII(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_parII(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_coma(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ",":
        return 1
    
    return estado_trampa

def A_coma(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_coma(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
            

def d_DosPunt(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ":":
        return 1
    
    return estado_trampa

def A_DosPunt(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_DosPunt(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_PuntCom(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ";":
        return 1
    
    return estado_trampa

def A_PuntCom(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_PuntCom(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_Var(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "v":
        return 1
    if estado_anterior == 1 and caracter == "a":
        return 2
    if estado_anterior == 2 and caracter == "r":
        return 3
    
    return estado_trampa

def A_Var(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Var(estado_actual, caracter)
        estado_actual = estado_proximo
        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    
    return RESULTADO_NO_ACEPTADO


def d_Igual(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1

    return estado_trampa

def A_Igual(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Igual(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_If(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "i":
        return 1
    if estado_anterior == 1 and caracter == "f":  
        return 2

    return estado_trampa

def A_If(cadena):
    finales = [2]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_If(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
    
    return RESULTADO_NO_ACEPTADO


def d_for(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "o":
        return 2
    if estado_anterior == 2 and caracter == "r":
        return 3
    
    return estado_trampa

def A_for(cadena):
    finales = [3]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_for(estado_actual,caracter)
        estado_actual = estado_proximo        

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_else(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "e":
        return 1
    if estado_anterior == 1 and caracter == "l":
        return 2
    if estado_anterior == 2 and caracter == "s":
        return 3
    if estado_anterior == 3 and caracter == "e":
        return 4           
    
    return estado_trampa

def A_else(cadena):
    finales = [4]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_else(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_return(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "r":
        return 1
    if estado_anterior == 1 and caracter == "e":
        return 2
    if estado_anterior == 2 and caracter == "t":
        return 3
    if estado_anterior == 3 and caracter == "u":
        return 4
    if estado_anterior == 4 and caracter == "r":
        return 5
    if estado_anterior == 5 and caracter == "n":
        return 6    

    return estado_trampa

def A_return(cadena):
    finales = [6]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_return(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO

    return RESULTADO_NO_ACEPTADO


def d_while(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "w":
        return 1
    if estado_anterior == 1 and caracter == "h":
        return 2
    if estado_anterior == 2 and caracter == "i":
        return 3
    if estado_anterior == 3 and caracter == "l":
        return 4  
    if estado_anterior == 4 and caracter == "e":
        return 5         
   
    return estado_trampa

def A_while(cadena):
    finales = [5]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_while(estado_actual,caracter)
        estado_actual = estado_proximo
        
        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO

    return RESULTADO_NO_ACEPTADO


def d_LlaveI(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "{":
        return 1

    return estado_trampa

def A_LlaveI(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_LlaveI(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_LlaveII(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "}":
        return 1

    return estado_trampa

def A_LlaveII(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_LlaveII(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_Or(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "o":
        return 1
    if estado_anterior == 1 and caracter == "r":  
        return 2
    
    return estado_trampa

def A_Or(cadena):
    finales = [2]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Or(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
    
    return RESULTADO_NO_ACEPTADO


def d_And(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "a":
        return 1
    if estado_anterior == 1 and caracter == "n":  
        return 2
    if estado_anterior == 2 and caracter == "d":
        return 3     
    
    return estado_trampa

def A_And(cadena):
    finales = [3]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_And(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_IgualA(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1
    if estado_anterior == 1 and caracter == "=":  
        return 2
    
    return estado_trampa

def A_IgualA(cadena):
    finales = [2]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_IgualA(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO 


def d_DistintoA(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "!":
        return 1
    if estado_anterior == 1 and caracter == "=":  
        return 2
    
    return estado_trampa

def A_DistintoA(cadena):
    finales = [2]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_DistintoA(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_Menor(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "<":
        return 1

    return estado_trampa

def A_Menor(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Menor(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_Mayor(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ">":
        return 1
    
    return estado_trampa

def A_Mayor(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Mayor(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_MenIgual(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "<":
        return 1
    if estado_anterior == 1 and caracter == "=":  
        return 2
    
    return estado_trampa

def A_MenIgual(cadena):
    finales = [2]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_MenIgual(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_MayIgual(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ">":
        return 1
    if estado_anterior == 1 and caracter == "=":  
        return 2

    return estado_trampa

def A_MayIgual(cadena):
    finales = [2]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_MayIgual(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO

    return RESULTADO_NO_ACEPTADO 


def d_Resta(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "-":
        return 1

    return estado_trampa

def A_Resta(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Resta(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_Suma(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "+":
        return 1

    return estado_trampa

def A_Suma(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Suma(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO  


def d_Barra(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "/":
        return 1

    return estado_trampa

def A_Barra(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Barra(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO 


def d_Asteris(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "*":
        return 1

    return estado_trampa

def A_Asteris(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Asteris(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
       
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_Excl(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "!":
        return 1

    return estado_trampa

def A_Excl(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Excl(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_True(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "t":
        return 1
    if estado_anterior == 1 and caracter == "r":
        return 2
    if estado_anterior == 2 and caracter == "u":
        return 3
    if estado_anterior == 3 and caracter == "e":
        return 4    

    return estado_trampa

def A_True(cadena):
    finales = [4]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_True(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO   


def d_False(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "a":
        return 2
    if estado_anterior == 2 and caracter == "l":
        return 3
    if estado_anterior == 3 and caracter == "s":
        return 4     
    if estado_anterior == 4 and caracter == "e":
        return 5      

    return estado_trampa

def A_False(cadena):
    finales = [5]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_False(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO 


def d_Punto(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == ".":
        return 1

    return estado_trampa

def A_Punto(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Punto(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
            return RESULTADO_ACEPTADO


def d_Numero(estado_anterior,caracter):
    if estado_anterior == 0 and caracter.isdigit():
        return 1
    if estado_anterior == 1 and caracter.isdigit():
        return 1
    if estado_anterior == 1 and caracter == "." :
        return 2
    if estado_anterior == 2 and caracter.isdigit():
        return 3
    if estado_anterior == 3 and caracter.isdigit():
        return 3        
    
    return estado_trampa

def A_Numero(cadena):
    finales = [1,3]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Numero(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA

    if estado_actual in finales:
        return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_String(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == "'" :
        return 1
    if estado_anterior == 1 and caracter.isdigit():
        return 2
    if estado_anterior == 1 and caracter.isalpha():
        return 2
    if estado_anterior == 2 and caracter.isdigit():
        return 2
    if estado_anterior == 2 and caracter.isalpha():
        return 2
    if estado_anterior == 2 and caracter == "'" :
        return 3

    return estado_trampa

def A_String(cadena):
    finales = [3]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_String(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
       
    if estado_actual in finales:
        return RESULTADO_ACEPTADO
        
    return RESULTADO_NO_ACEPTADO


def d_Id(estado_anterior, caracter):
    if estado_anterior == 0 and caracter.isalpha():
        return 1
    if estado_anterior == 1 and caracter.isalpha():
        return 1
    if estado_anterior ==  1 and caracter.isdigit():
        return 1

    return estado_trampa

def A_Id(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Id(estado_actual, caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA
        
    if estado_actual in finales:
        return RESULTADO_ACEPTADO
   
    return RESULTADO_NO_ACEPTADO

def d_Espacio(estado_anterior,caracter):
    if estado_anterior == 0 and caracter == " ":
        return 1

    return estado_trampa

def A_Espacio(cadena):
    finales = [1]
    estado_actual = 0
    for caracter in cadena:
        estado_proximo = d_Espacio(estado_actual,caracter)
        estado_actual = estado_proximo

        if estado_proximo == estado_trampa:
            return RESULTADO_TRAMPA

    if estado_actual in finales:
        return RESULTADO_ACEPTADO

#Casos

caso_If = [
           ("if", RESULTADO_ACEPTADO),
           ("ifvar", RESULTADO_TRAMPA),  
           ("i", RESULTADO_NO_ACEPTADO)
]
    
for cadena , resultado in caso_If:
    assert A_If(cadena) == resultado

caso_else = [
             ("else", RESULTADO_ACEPTADO),
             ("elsevar", RESULTADO_TRAMPA),
             ("els", RESULTADO_NO_ACEPTADO)
]

for cadena, resultado in caso_else:
    assert A_else(cadena) == resultado

caso_And = [
            ("and",RESULTADO_ACEPTADO),
            ("andvar", RESULTADO_TRAMPA),
            ("a", RESULTADO_NO_ACEPTADO)
]

for cadena, resultado in caso_And:
    assert A_And(cadena) == resultado

caso_Fun = [
            ("fun", RESULTADO_ACEPTADO),
            ("funvar", RESULTADO_TRAMPA),
            ("fu", RESULTADO_NO_ACEPTADO)
]

for cadena, resultado in caso_Fun:
    assert A_fun (cadena) == resultado 

caso_While = [
              ("while", RESULTADO_ACEPTADO),
              ("whp", RESULTADO_TRAMPA),
              ("wh", RESULTADO_NO_ACEPTADO)
]

for cadena, resultado in caso_While:
    assert A_while(cadena) == resultado

caso_Return= [
            ("return", RESULTADO_ACEPTADO),
            ("reut", RESULTADO_TRAMPA),
            ("ret", RESULTADO_NO_ACEPTADO)
]

for cadena, resultado in caso_Return:
    assert A_return(cadena) == resultado

caso_for= [
            ("for", RESULTADO_ACEPTADO),
            ("fot", RESULTADO_TRAMPA),
            ("fo", RESULTADO_NO_ACEPTADO)
]

for cadena, resultado in caso_for:
    assert A_for(cadena) == resultado