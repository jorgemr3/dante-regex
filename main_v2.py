def es_numero_valido(cadena: str) -> bool:
    if not cadena:
        return False
    
    pos = 0
    if cadena[0] in "+-":
        pos = 1
    
    if pos >= len(cadena):
        return False
    
    resto = cadena[pos:]
    e_index = -1
    for i, c in enumerate(resto):
        if c in 'eE':
            if e_index != -1: 
                return False
            e_index = i

    if e_index != -1:
        base = resto[:e_index]
        exponente = resto[e_index+1:]
        if not exponente:  
            return False
    else:
        base = resto
        exponente = None
    
    if base.startswith('.') or base.endswith('.'):
        return False
    
    puntos = base.count('.')
    if puntos > 1:
        return False
    
    if '.' in base:
        entero_str, decimal_str = base.split('.', 1)
        if not entero_str and not decimal_str:
            return False
 
        if entero_str and not entero_str.isdigit():
            return False
        if decimal_str and not decimal_str.isdigit():
            return False
    else:
        if not base.isdigit():
            return False

    if exponente is not None:
        exp_pos = 0
        if exponente[0] in "+-":
            exp_pos = 1
        
        exp_restante = exponente[exp_pos:]
        if not exp_restante or not exp_restante.isdigit():
            return False
    
    return True

# validos = ["1", "+3", "-3", "4.5", "4.5e1", "+4.5E-2", "2e2", "2E2", "+0.0e0"]
# invalidos = ["-", "=1", "+", "2.", ".2", "+.2", "-2E", "-2e#", "123.45.6", "e5"]

# for caso in validos:
#     print(f"{caso}: {'Válido' if es_numero_valido(caso) else 'Inválido'}")

# print("\nCasos inválidos:")
# for caso in invalidos:
#     print(f"{caso}: {'Válido' if es_numero_valido(caso) else 'Inválido'}")


while True:
    cadena = input("Ingrese una cadena: ")
    if not cadena:
        break
    print(f"{cadena}: {'Válido' if es_numero_valido(cadena) else 'Inválido'}")
