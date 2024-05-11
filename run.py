# Definimos un diccionario para almacenar las variables
variables = {}

from colorama import Fore, init
init()

# Definimos una función que ejecuta código LIWX
def ejecutar_liwx(codigo):
    # Dividimos el código en líneas
    lineas = codigo.split('\n')
    
    # Verificamos si hay un mensaje de importación
    mensaje_importacion = False
    for linea in lineas:
        if linea.startswith('import __lwx.engine__'):
            mensaje_importacion = True
            break

    # Si no se encuentra el mensaje de importación, detenemos la ejecución
    if not mensaje_importacion:
        print(Fore.RED + "Error: No se encontró el mensaje de importación '__lwx.engine__'.")
        return

    # Iteramos sobre cada línea y ejecutamos la acción correspondiente
    for linea in lineas:
        # Si la línea comienza con 'printly', imprimimos los textos entre paréntesis
        if linea.startswith('printly'):
            texto = linea.split('(')[1].split(')')[0]
            # Buscamos si hay variables en el texto y las reemplazamos
            for var, val in variables.items():
                texto = texto.replace(var, str(val))
            # Separamos los argumentos por '|'
            argumentos = texto.split('|')
            # Imprimimos los argumentos sin un salto de línea entre ellos
            print(''.join(arg.strip('\"') for arg in argumentos), end='')
            if not texto:
                print(Fore.RED + "Error type=1.!. Not tracke:", texto)
        # Si la línea contiene una operación de asignación
        elif '=' in linea:
            variable, valor = linea.split('=')
            variable = variable.strip()
            valor = valor.strip()
            # Si el valor es una operación matemática, evaluamos la expresión
            if any(op in valor for op in ['+', '-', '*']):
                # Si la operación es una suma
                if '+' in valor:
                    op1, op2 = valor.split('+')
                    variables[variable] = int(op1.strip()) + int(op2.strip())
                # Si la operación es una resta
                elif '-' in valor:
                    op1, op2 = valor.split('-')
                    variables[variable] = int(op1.strip()) - int(op2.strip())
                # Si la operación es una multiplicación
                elif '*' in valor:
                    op1, op2 = valor.split('*')
                    variables[variable] = int(op1.strip()) * int(op2.strip())
            else:
                # Si no hay operaciones matemáticas, asignamos el valor directamente a la variable
                variables[variable] = int(valor)

# Función principal que lee un archivo LIWX y lo ejecuta
def ejecutar_archivo_liwx(archivo):
    with open(archivo, 'r') as f:
        codigo = f.read()
        ejecutar_liwx(codigo)

# Ejemplo de uso: ejecutar un archivo LIWX
if __name__ == "__main__":
    archivo_liwx = "ejemplo.lwx"
    ejecutar_archivo_liwx(archivo_liwx)
