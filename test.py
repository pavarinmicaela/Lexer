from lex import *

casosLexer = [
    (
        "if ( a >= b then *",
        [('IF', 'if'), ('(','('), ('ID', 'a'), ('>=', '>='), ('ID', 'b'), ('ID', 'then'), ('*', '*'),("EOF","EOF")]
     ),

    (
        "if while variable fun", 
        [('IF', 'if'), ('WHILE', 'while'), ('ID', 'variable'), ('FUN', 'fun'),("EOF","EOF")]
    ),

    (
        "while ( a + b == c ) then", 
        [('WHILE', 'while'), ('(', '('), ('ID', 'a'), ('+', '+'), ('ID', 'b'), ('==', '=='), ('ID', 'c'), (')', ')'), ('ID', 'then'),("EOF","EOF")]
    ),

    (
        "palabra = 'palabra'", 
        [('ID', 'palabra'), ('=', '='), ('STRING', "'palabra'"),("EOF","EOF")]
    ),

    (
        "while eof ! else variable",
        [('WHILE', 'while'), ('EOF', 'eof'), ('!', '!'), ('ELSE', 'else'), ('ID', 'variable'),("EOF","EOF")]
    ),

    (
        "if ( a + b = x ) and ( a + x = c )", 
        [('IF', 'if'), ('(', '('), ('ID', 'a'), ('+', '+'), ('ID', 'b'), ('=', '='), ('ID', 'x'), (')', ')'), ('AND', 'and'), ('(', '('), ('ID', 'a'), ('+', '+'), ('ID', 'x'), ('=', '='), ('ID', 'c'), (')', ')'),("EOF","EOF")]
    ),

    (
        "var vector = ( 1 , casa ) , ( 2 , mesa )",
        [('VAR', 'var'), ('ID', 'vector'), ('=', '='), ('(', '('), ('NUM', '1'), (',', ','), ('ID', 'casa'), (')', ')'), (',', ','), ('(', '('), ('NUM', '2'), (',', ','), ('ID', 'mesa'), (')', ')'),("EOF","EOF")]
    ),

    (
        "var casa = 'CUadERNO'", 
        [('VAR', 'var'), ('ID', 'casa'), ('=', '='), ('STRING', "'CUadERNO'"),("EOF","EOF")]
    ),

    (
        "vector { 2 } = 32",
        [('ID', 'vector'), ('{', '{'), ('NUM', '2'), ('}', '}'), ('=', '='), ('NUM', '32'),("EOF","EOF")]
    ),

    (
        "var b - a - c = 15",
        [('VAR', 'var'), ('ID', 'b'), ('-', '-'), ('ID', 'a'), ('-', '-'), ('ID', 'c'), ('=', '='), ('NUM', '15'),("EOF","EOF")]
    ),

    (
        "if ( a = b ) and c = 15 then",
        [('IF', 'if'), ('(', '('), ('ID', 'a'), ('=', '='), ('ID', 'b'), (')', ')'), ('AND', 'and'), ('ID', 'c'), ('=', '='), ('NUM', '15'), ('ID', 'then'),("EOF","EOF")]
    ),

    (
        "botella = 'bo' + 'tella'", 
        [('ID', 'botella'), ('=', '='), ('STRING', "'bo'"), ('+', '+'), ('STRING', "'tella'"),("EOF","EOF")]
    ),

    (
        "while ( b = c ) or ( a = c )", 
        [('WHILE', 'while'), ('(', '('), ('ID', 'b'), ('=', '='), ('ID', 'c'), (')', ')'), ('OR', 'or'), ('(', '('), ('ID', 'a'), ('=', '='), ('ID', 'c'), (')', ')'),("EOF","EOF")]
    ),

    (
        "1 + 2 + 3 + 4 = 11", 
        [('NUM', '1'), ('+', '+'), ('NUM', '2'), ('+', '+'), ('NUM', '3'), ('+', '+'), ('NUM', '4'), ('=', '='), ('NUM', '11'),("EOF","EOF")]
    ),

    (
        "'casa' + 'aldo' = 'casaDeAldo'", 
        [('STRING', "'casa'"), ('+', '+'), ('STRING', "'aldo'"), ('=', '='), ('STRING', "'casaDeAldo'"),("EOF","EOF")]
    ) 
]

for cadena, resultado in casosLexer:
    assert lexer(cadena) == resultado