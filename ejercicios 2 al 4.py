import re

# ======================================
# Clase Analizador Léxico
# ======================================
class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo

        # Expresiones regulares por categoría
        self.tokens = [
            ("PALABRA_RESERVADA", r"\b(int|float|if|else|return|for|while)\b"),
            ("IDENTIFICADOR", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
            ("NUMERO", r"\b\d+(\.\d+)?\b"),
            ("OPERADOR", r"[+\-*/=<>!]"),
            ("DELIMITADOR", r"[(){};]"),
            ("ESPACIO", r"[ \t\n]+"),
            ("DESCONOCIDO", r".")  # Para capturar cualquier otro símbolo
        ]

    def tokenizar(self):
        tokens_encontrados = []
        codigo_restante = self.codigo

        while codigo_restante:
            match = None
            for tipo, patron in self.tokens:
                regex = re.compile(patron)
                match = regex.match(codigo_restante)
                if match:
                    valor = match.group(0)
                    if tipo != "ESPACIO":  # No mostrar espacios
                        tokens_encontrados.append((tipo, valor))
                    codigo_restante = codigo_restante[len(valor):]
                    break
            if not match:
                print(f"Error: no se pudo analizar: {codigo_restante[0]}")
                break

        return tokens_encontrados


# ======================================
# EJEMPLO 2: Declaración con operaciones
# ======================================
print("\n" + "=" * 50)
print("EJEMPLO 2: Declaración con operaciones")
print("=" * 50)

codigo2 = "float precio = 99.99 + 10;"
lexer2 = AnalizadorLexico(codigo2)
tokens2 = lexer2.tokenizar()

print(f"Código fuente: {codigo2}")
print("\nTokens generados:")
for token in tokens2:
    print(token)


# ======================================
# EJEMPLO 3: Estructura de control
# ======================================
print("\n" + "=" * 50)
print("EJEMPLO 3: Estructura de control")
print("=" * 50)

codigo3 = """if (x > 5) {
    return x;
}"""
lexer3 = AnalizadorLexico(codigo3)
tokens3 = lexer3.tokenizar()

print(f"Código fuente:\n{codigo3}")
print("\nTokens generados:")
for token in tokens3:
    print(token)


# ======================================
# EJEMPLO 4: Programa completo
# ======================================
print("\n" + "=" * 50)
print("EJEMPLO 4: Programa completo")
print("=" * 50)

codigo4 = """int suma = 0;
for (i = 1; i < 10; i = i + 1) {
    suma = suma + i;
}
return suma;"""
lexer4 = AnalizadorLexico(codigo4)
tokens4 = lexer4.tokenizar()

print(f"Código fuente:\n{codigo4}")
print(f"\nTotal de tokens generados: {len(tokens4)}")
print("\nTokens generados:")
for token in tokens4:
    print(token)
