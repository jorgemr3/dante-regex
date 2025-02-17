# https://regex101.com/
#todo checar en la pagina

#region validos
# cadena = "+4.5E-2" VALIDO
# cadena = "4.5E-2" VALIDO
# cadena = "-4.5E-2" # VALIDO
# cadena = "444.53E-2" VALIDO
# cadena = "5E-2" VALIDO
# cadena = "-2" # VALIDO
# cadena = "0" VALIDO
# cadena = "0.0" VALIDO

#endregion

#region invalidos
# cadena = "E-2" # todo INVALIDO porque no tiene parte entera
# cadena = "-2." # todo INVALIDO porque no tiene parte decimal
# cadena = "+2." # todo INVALIDO mismo caso anterior
# cadena = "+." # todo INVALIDO porque no tiene parte entera ni decimal
# cadena = "+" # todo INVALIDO no puede empezar por signo
# cadena = "-" # todo INVALIDO mismo caso anterior
# cadena = ""  # todo INVALIDO no hay signo, ni inicia con un número, ademas que no hay nada
# cadena = "q" # todo INVALIDO aunque no tiene signo no es un número
# cadena = "=4.5E-2" # todo INVALIDO porque inicia con un signo diferente a + o -
# cadena = "444.533-2" # todo INVALIDO porque tiene un guion al final
# cadena = "444.53eE-2" # todo INVALIDO, el primer repetido que es invalido
# cadena = " " # todo INVALIDO, la cadena no empieza por un signo o digito
# cadena = "4.5e2." # todo INVALIDO, el punto al final
# cadena = "..4" # todo INVALIDO, empieza por punto
# cadena = "3..4" # todo INVALIDO, dos puntos seguidos
# cadena = "33..4" # todo INVALIDO 

#endregion

#region outliers
# TODO cadena = ".5E-2" valido, ES INVALIDO porque empieza por un punto (no tiene parte entera)
# cadena = "-0.0e0" valido # todo checar este caso especifico
# cadena = "+0.0e0" # todo checar este caso especifico

#endregion

#TODO DOCUMENTACION
# Componentes de la Expresión Regular:

# ^[+-]?: Valida que la cadena pueda comenzar con un signo + o -, o sin signo.

# (?=\d+\.?\d*$|\.?\d+): Asegura que después del signo (si existe) haya dígitos válidos, evitando casos como +.2 o -.

# (\d+(?:\.\d+)?|\.\d+): Valida la parte principal del número, que puede ser un entero (\d+), un decimal con dígitos antes y después del punto (\d+\.\d+), o un decimal que comience con punto pero solo si hay dígitos después (esto se maneja con lookaheads para asegurar cumplimiento de reglas).

# (?:[eE][+-]?\d+)?$: Valida la parte exponencial, que puede comenzar con e o E, seguido de un signo opcional y dígitos.

import re

#region regex
regex = r'^[+-]?(?=\d+\.?\d*$|\.?\d+)(\d+(?:\.\d+)?|\.\d+)(?:[eE][+-]?\d+)?$'
# regex_4 = #r'^([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?$'
regex_2 = r'^-[0-9]*\.[0-9]+$'
regex_3 = r'^\+[0-9]*\.[0-9]+$'
#endregion

# TODO: SI SIRVE

cadena = ""

# Verificar si la cadena coincide con el primer regex y NO con el segundo, el segundo es para rebotar errores como: -.e-2, -.e, -., -2.e-2
if re.fullmatch(regex, cadena) and not re.fullmatch(regex_2, cadena) and not re.fullmatch(regex_3, cadena):
    print(f"Estado de {cadena} : Válido")
else:
    print(f"Estado de {cadena} : Inválido")