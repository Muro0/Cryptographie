# Clé utilisée pour le déchiffrement
cle = "CLE"

# Texte chiffré à déchiffrer (lettres majuscules + espaces uniquement)
code = "bonjour"

# On met la clé en majuscules pour éviter les erreurs
cle = cle.upper()

# Fonction qui déchiffre un message codé avec Vigenère
def vigenere_dechiffrer(code, cle):
    texte = ""  # Chaîne qui va contenir le texte déchiffré
    i = 0       # Index pour suivre la position dans la clé

    for c in code:
        if c.isalpha():  # Si c'est une lettre
            l = ord(c.upper()) - 65                  # Position de la lettre dans l'alphabet (A=0)
            k = ord(cle[i % len(cle)]) - 65          # Décalage selon la lettre de la clé
            r = (l - k + 26) % 26                    # Calcul du décalage inverse (décryptage)
            texte += chr(r + 65)                     # On convertit en lettre majuscule
            i += 1                                   # On avance dans la clé
        elif c == " ":  # Si c'est un espace, on le garde
            texte += " "
        # Les autres caractères (ponctuation, chiffres, etc.) sont ignorés

    return texte

# On appelle la fonction et on affiche le résultat
texte_en_clair = vigenere_dechiffrer(code, cle)
print("Texte déchiffré :", texte_en_clair)
