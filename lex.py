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
	tokens = []
	subcadena = ''
	candidatos = []
	index = 0
	start = 0
	end = 0

	while index < len(cadena):
		if cadena[index].isspace():
			index += 1
			continue		
		start = index
		end += 1
		lexeme = cadena [start:end]
		if end > len(cadena):
			for tipo,automata in LTT:
				if automata(subcadena) == RESULTADO_ACEPTADO:
					tokens.append((tipo,subcadena))
					break
			break
		for tipo,automata in LTT:
			if automata(lexeme) == RESULTADO_ACEPTADO:
				candidatos.append((tipo,lexeme))
				new_start = end
				subcadena = lexeme
		if TodosTrampa(lexeme):
			for tipo,automata in LTT:
				if automata(subcadena) == RESULTADO_ACEPTADO:
					tokens.append((tipo,subcadena))
					lexeme = ''
					start = end = new_start
					index = start
					if cadena[start].isspace():
							start += 1
							end += 1
							new_start += 1
							index = start
					break
				candidatos = []
	return tokens