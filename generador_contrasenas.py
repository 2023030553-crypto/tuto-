import secrets
import string

def generar_contrasena(longitud):
    pool = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"

    # Garantizar al menos un carácter de cada tipo
    garantizados = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*()-_=+[]{}|;:,.<>?"),
    ]

    resto = [secrets.choice(pool) for _ in range(longitud - len(garantizados))]
    caracteres = garantizados + resto

    # Mezclar con aleatorio criptográfico
    for i in range(len(caracteres) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        caracteres[i], caracteres[j] = caracteres[j], caracteres[i]

    return "".join(caracteres)

def main():
    print("\n=== Generador de Contraseñas ===\n")

    while True:
        try:
            longitud = int(input("Ingresa la longitud (mínimo 12): "))
            if longitud < 12:
                print("  La longitud mínima es 12. Intenta de nuevo.\n")
            else:
                break
        except ValueError:
            print("  Por favor ingresa un número válido.\n")

    contrasena = generar_contrasena(longitud)

    print(f"\n  Tu contraseña: {contrasena}\n")
    print("================================\n")

if __name__ == "__main__":
    main()
