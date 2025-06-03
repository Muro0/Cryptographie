def cesar_chiffrer(texte, decalage):
    texte = texte.upper()
    res = ""
    for c in texte:
        if c.isalpha():
            res += chr((ord(c) - 65 + decalage) % 26 + 65)
        elif c == " ":
            res += " "  # On garde les espaces
    return res

# Fonction pour déchiffrer
def cesar_dechiffrer(texte, decalage):
    return cesar_chiffrer(texte, -decalage)

# Exemple d’utilisation
clair = "BONJOUR"
decalage = 3

chiffre = cesar_chiffrer(clair, decalage)
dechiffre = cesar_dechiffrer(chiffre, decalage)

# Affichage
print("Texte clair     :", clair)
print("Décalage        :", decalage)
print("Texte chiffré   :", chiffre)
print("Texte déchiffré :", dechiffre)
