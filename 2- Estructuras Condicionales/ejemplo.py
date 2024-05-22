def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "Es un número par."
    else:
        return "Es un número impar."

# Ejemplo de uso
numero_usuario = int(input("Ingresa un número: "))
print(es_par_o_impar(numero_usuario))