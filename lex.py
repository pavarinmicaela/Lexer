from GLexica import *

LTT = [
 		("EOF",A_eof),
 		("FUN",A_fun),
 		("(",A_parI ),
 		(")",A_parII),
 		(",",A_coma),
 		(";",A_PuntCom),
		("VAR",A_Var),
 		(":",A_DosPunt),
 		("=",A_Igual),
 		("IF",A_If),
 		("FOR",A_for),
 		("ELSE",A_else),
 		("RETURN",A_return),
 		("WHILE",A_while),
 		("{",A_LlaveI),
 		("}",A_LlaveII),
 		("OR",A_Or),
 		("AND",A_And),
 		("==",A_IgualA),
 		("!=",A_DistintoA),
 		("<",A_Menor),
 		(">",A_Mayor),
 		("<=",A_MenIgual),
 		(">=",A_MayIgual),
 		("-",A_Resta),
 		("+",A_Suma),
 		("/",A_Barra),
 		("*",A_Asteris),
 		("!",A_Excl),
 		("TRUE",A_True),
 		("FALSE",A_False),
 		(".",A_Punto),
 		("NUM",A_Numero),
 		("STRING",A_String),
 		("ID",A_Id)
]

def TodosTrampa(lexeme):
    for tipo,automata in LTT: 
        if automata(lexeme) != RESULTADO_TRAMPA:
            return False
    return True

def lexer(cadena):
	cadena += ' ' #para que pueda romper el ciclo en el ultimo caracter, al tener un espacio al final de la cadena TodosTrampa = True
	tokens = []
	candidatos = []
	lexeme = ''
	index = 0
	end = 0

	while index < len(cadena):
		if cadena[index].isspace():
			index += 1
			continue		
		end=index

		while not TodosTrampa(lexeme):
			end += 1
			lexeme = cadena [index:end]
			for tipo,automata in LTT:
				if automata(lexeme) == RESULTADO_ACEPTADO:
					candidatos.append((tipo,lexeme))
					break
			
		tokens.append(candidatos[-1])
		lexeme = ''
		end -= 1
		index = end
		candidatos = []
	
	tokens.append(("EOF","EOF"))
	return tokens