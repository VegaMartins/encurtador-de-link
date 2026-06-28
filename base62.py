# base62.py

ALFABETO = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALFABETO)

def codificar(numero_id):

    if numero_id == 0:
        return ALFABETO[0]
    
    caracteres = []
    
    while numero_id > 0:
        numero_id, resto = divmod(numero_id, BASE)
        caracteres.append(ALFABETO[resto])
    
    caracteres.reverse()
    return ''.join(caracteres)

if __name__ == '__main__':
    print("Testando ID 11157:", codificar(11157)) # Esperado: 2TX
    print("Testando ID 1:", codificar(1))         # Esperado: 1
    print("Testando ID 61:", codificar(61))       # Esperado: Z
    print("Testando ID 62:", codificar(62))       # Esperado: 10
    print("Testando ID 9999:", codificar(9999))   # Esperado: 2Bh