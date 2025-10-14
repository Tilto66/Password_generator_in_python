import random
import string
import time
import secrets

def generate_password(longueur=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    """Generates a secure password with specified criteria."""
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
        return None
    
    # Using secrets for better security
    password = ''.join(secrets.choice(characters) for _ in range(longueur))
    return password

def get_yes_no(prompt):
    """Asks for a yes/no answer robustly."""
    while True:
        reponse = input(prompt).strip().lower()
        if reponse in ['o', 'oui', 'y', 'yes']:
            return True
        elif reponse in ['n', 'non', 'no']:
            return False
        else:
            print("  Invalid answer. Please answer with 'y' (yes) or 'n' (no).")

def evaluer_force(password):
    """Evaluates password strength."""
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score <= 2:
        return " Weak", "red"
    elif score <= 4:
        return " Medium", "yellow"
    else:
        return " Strong", "green"

def afficher_titre():
    """Displays the program title."""
    print("\n" + "="*60)
    print("  SECURE PASSWORD GENERATOR  ".center(60))
    print("="*60)
    print("Your passwords are never saved or transmitted.")
    print("="*60 + "\n")

def main():
    afficher_titre()
    
    try:
        # Demande de la longueur
        while True:
            longueur_input = input(" Password length (min. 8, recommended 16+): ").strip()
            try:
                longueur = int(longueur_input)
                if longueur < 4:
                    print("  Length must be at least 4 characters.")
                elif longueur < 8:
                    print("  Warning: Less than 8 characters is considered weak.")
                    if get_yes_no("Continue anyway? (y/n): "):
                        break
                else:
                    break
            except ValueError:
                print(" Please enter a valid number.")
        
        print()
        
        # Demande des types de caractères
        use_lower = get_yes_no(" Include lowercase letters (a-z)? (y/n): ")
        use_upper = get_yes_no(" Include uppercase letters (A-Z)? (y/n): ")
        use_digits = get_yes_no(" Include digits (0-9)? (y/n): ")
        use_symbols = get_yes_no(" Include symbols (!@#$...)? (y/n): ")
        
        # Vérification qu'au moins un type est sélectionné
        if not any([use_lower, use_upper, use_digits, use_symbols]):
            print("\n Error: You must select at least one character type!")
            return
        
        # Génération du mot de passe
        print("\n" + "-"*60)
        print("  Generating", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        
        password = generate_password(longueur, use_lower, use_upper, use_digits, use_symbols)
        
        # Affichage des paramètres
        print("\n Password parameters:")
        print(f"   • Length: {longueur} characters")
        if use_lower:
            print("   • Lowercase letters (a-z)")
        if use_upper:
            print("   • Uppercase letters (A-Z)")
        if use_digits:
            print("   • Digits (0-9)")
        if use_symbols:
            print("   • Symbols (!@#$...)")
        
        # Évaluation de la force
        force, couleur = evaluer_force(password)
        print(f"\n Password strength: {force}")
        
        # Affichage du mot de passe
        print("\n" + "="*60)
        print(" YOUR PASSWORD:")
        print("="*60)
        print(f"\n   {password}\n")
        print("="*60)
        
        # Option pour générer un autre mot de passe
        print()
        if get_yes_no(" Generate another password? (y/n): "):
            print("\n" * 2)
            main()
        else:
            print("\n Thank you for using the password generator!")
            print(" Tip: Use a password manager to store your passwords securely.\n")
    
    except KeyboardInterrupt:
        print("\n\n  Program interrupted by user.")
    except Exception as e:
        print(f"\n Unexpected error: {e}")

if __name__ == "__main__":
    main()
    time.sleep(300)
