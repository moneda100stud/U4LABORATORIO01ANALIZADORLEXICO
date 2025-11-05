import re

class Token:

    def __init__(self, tipo, valor, Linea):
        self.tipo = tipo

        self.valor = valor

        self.linea = Linea

    def __str__(self):
        return f"Tipo: {self.tipo:<15} Valor: '{self.valor}'"


class AnalizadorLexico:

    def __init__(self, codigo):

        self.codigo = codigo

        self.pos = 0

        self.linea = 1

# Especificación de tokens (el orden importa)

# Completa cada patrón y agrega lo que haga falta

        self.patrones = [

('KEYWORD', r'\b(if while for return|int|float)\b'),

('IDENTIFIER', r' [a-zA-Z_] [a-zA-Z0-9_]*'),

('NUMBER', r'\d+\.?\d*'),

('OPERATOR', r'[*=]=?'),

('DELIMITER', r'[;]'),

('WHITESPACE', r'[ \t]+'),

('NEWLINE', r'\n'),

('ERROR', r'.')

]


    def tokenizar (self):

        tokens = []

        while self.pos < len(self.codigo):
            encontrado = False


            for tipo, patron in self.patrones:

                regex = re.compile(patron)
                match = regex.match(self.codigo, self.pos)

                # If a match is found
                if match:

                    valor = match.group(0)

                    if tipo == 'NEWLINE':

                        self.linea += 1

                    elif tipo not in ['WHITESPACE', 'NEWLINE']:
                        tokens.append(Token (tipo, valor, self.linea))

                    self.pos = match.end()

                    encontrado = True
                    break

            if not encontrado:
                self.pos += 1


        return tokens



# Ejemplo 1: Código simple
print("=" * 50)
print("EJEMPLO 1: Código simple")
 
print("=" * 50)


codigo1 = "int x = 10 ;"

lexer1 = AnalizadorLexico (codigo1)
tokens1 = lexer1.tokenizar()
print (f"Código fuente: {codigo1}")
print("\nTokens generados:")
print(f"{'Tipo':<15} {'Valor':<15}")
print("-" * 30)
for token in tokens1:
    print(f"{token.tipo:<15} {repr(token.valor):<15}")