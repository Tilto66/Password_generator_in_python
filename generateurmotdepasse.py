import random
import string
import time

def generate_password(longueur=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Aucun type de caractères sélectionné.")
        exit()

    password = ''.join(random.choice(characters) for _ in range(longueur))
    return password

# --- Interface utilisateur simple ---
print("                                       === Générateur de mots de passe ===")
print("Ce générateur de mots de passe est fait uniquement en code python.\nIl vous est garanti que les mots de passe ne sont pas enregistrés")

try:
    longueur = int(input("Longueur du mot de passe (ex: 12) : "))
    use_lower = input("Inclure des minuscules ? (o/n) : ")
    if use_lower == 'o':
        use_lower = True
    elif use_lower == 'n':
        use_lower = False
    else :
        time.sleep(0.5)
        print("Veuillez répondre pas (o)ui ou par (n)on. Ce tirage est considéré comme non.")
        use_lower = False
##########################################################
    use_upper = input("Inclure des majuscules ? (o/n) : ")
    if use_upper == 'o':
        use_upper = True
    elif use_upper == 'n':
        use_upper = False
    else :
        time.sleep(0.5)
        print("Veuillez répondre pas (o)ui ou par (n)on. Ce tirage est considéré comme non.")
        use_upper = False
##########################################################
    use_digits = input("Inclure des chiffres ? (o/n) : ")
    if use_digits == 'o':
        use_digits = True
    elif use_digits == 'n':
        use_digits = False
    else :
        time.sleep(0.5)
        print("Veuillez répondre pas (o)ui ou par (n)on. Ce tirage est considéré comme non.")
        use_lower = False
##########################################################
    use_symbols = input("Inclure des symboles ? (o/n) : ")
    if use_symbols == 'o':
        use_symbols = True
    elif use_symbols == 'n':
        use_symbols = False
    else :
        time.sleep(0.5)
        print("Veuillez répondre pas (o)ui ou par (n)on. Ce tirage est considéré comme non.")
        use_symbols = False

    password = generate_password(longueur, use_lower, use_upper, use_digits, use_symbols)
    print(f'Le mot de passe va être de {longueur} caractères et va contenir :')
    if use_upper == True :
        time.sleep(0.2)
        print('- Des majuscules')
    if use_lower == True :
        time.sleep(0.2)
        print('- Des minuscules')
    if use_digits == True :
        time.sleep(0.2)
        print('- Des nombres')
    if use_symbols == True :
        time.sleep(0.2)
        print('- Des symboles')
    print('\nMot de passe généré :')
    print(password)

except ValueError as e:
    print(f"Erreur : {e}")
time.sleep(999)