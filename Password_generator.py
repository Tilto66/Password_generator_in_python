import random
import string
import time
import secrets

def generate_password(longueur=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    """Génère un mot de passe sécurisé avec les critères spécifiés."""
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
    
    # Utilisation de secrets pour plus de sécurité
    password = ''.join(secrets.choice(characters) for _ in range(longueur))
    return password

def get_yes_no(prompt):
    """Demande une réponse oui/non de manière robuste."""
    while True:
        reponse = input(prompt).strip().lower()
        if reponse in ['o', 'oui', 'y', 'yes']:
            return True
        elif reponse in ['n', 'non', 'no']:
            return False
        else:
            print("Reponse invalide. Veuillez repondre par 'o' (oui) ou 'n' (non).")

def evaluer_force(password):
    """Évalue la force d'un mot de passe."""
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
        return "Faible", "rouge"
    elif score <= 4:
        return "Moyen", "jaune"
    else:
        return "Fort", "vert"

def afficher_titre():
    """Affiche le titre du programme."""
    print("\n" + "="*60)
    print("GENERATEUR DE MOTS DE PASSE SECURISE".center(60))
    print("="*60)
    print("Vos mots de passe ne sont jamais enregistres ou transmis.")
    print("="*60 + "\n")

def main():
    afficher_titre()
    
    try:
        # Demande de la longueur
        while True:
            longueur_input = input("Longueur du mot de passe (min. 8, recommande 16+) : ").strip()
            try:
                longueur = int(longueur_input)
                if longueur < 4:
                    print("La longueur doit etre d'au moins 4 caracteres.")
                elif longueur < 8:
                    print("Attention : moins de 8 caracteres est considere comme faible.")
                    if get_yes_no("Continuer quand meme ? (o/n) : "):
                        break
                else:
                    break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        
        print()
        
        # Demande des types de caractères
        use_lower = get_yes_no("Inclure des minuscules (a-z) ? (o/n) : ")
        use_upper = get_yes_no("Inclure des majuscules (A-Z) ? (o/n) : ")
        use_digits = get_yes_no("Inclure des chiffres (0-9) ? (o/n) : ")
        use_symbols = get_yes_no("Inclure des symboles (!@#$...) ? (o/n) : ")
        
        # Vérification qu'au moins un type est sélectionné
        if not any([use_lower, use_upper, use_digits, use_symbols]):
            print("\nErreur : Vous devez selectionner au moins un type de caracteres !")
            return
        
        # Génération du mot de passe
        print("\n" + "-"*60)
        print("Generation en cours", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        
        password = generate_password(longueur, use_lower, use_upper, use_digits, use_symbols)
        
        # Affichage des paramètres
        print("\nParametres du mot de passe :")
        print(f"   - Longueur : {longueur} caracteres")
        if use_lower:
            print("   - Minuscules (a-z)")
        if use_upper:
            print("   - Majuscules (A-Z)")
        if use_digits:
            print("   - Chiffres (0-9)")
        if use_symbols:
            print("   - Symboles (!@#$...)")
        
        # Évaluation de la force
        force, couleur = evaluer_force(password)
        print(f"\nForce du mot de passe : {force}")
        
        # Affichage du mot de passe
        print("\n" + "="*60)
        print("VOTRE MOT DE PASSE :")
        print("="*60)
        print(f"\n   {password}\n")
        print("="*60)
        
        # Option pour générer un autre mot de passe
        print()
        if get_yes_no("Generer un autre mot de passe ? (o/n) : "):
            print("\n" * 2)
            main()
        else:
            print("\nMerci d'avoir utilise le generateur de mots de passe !")
            print("Conseil : Utilisez un gestionnaire de mots de passe pour stocker vos mots de passe en toute securite.\n")
    
    except KeyboardInterrupt:
        print("\n\nProgramme interrompu par l'utilisateur.")
    except Exception as e:
        print(f"\nErreur inattendue : {e}")

if __name__ == "__main__":
    main()
    time.sleep(3)
