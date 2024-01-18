def analyser_mots_de_passe(mot_de_passe):
    nb_caracteres = 0
    nb_chiffres = 0
    nb_majuscules = 0
    nb_speciaux = 0

    for caractere in mot_de_passe:
        nb_caracteres += 1
        if caractere.isdigit():
            nb_chiffres += 1
        elif caractere.isupper():
            nb_majuscules += 1
        elif not caractere.isalnum():
            nb_speciaux += 1
    """
    print(f"Mot de passe: {mot_de_passe}")
    print(f"Nombre de caractères: {nb_caracteres}")
    print(f"Nombre de chiffres: {nb_chiffres}")
    print(f"Nombre de lettres majuscules: {nb_majuscules}")
    print(f"Nombre de caractères spéciaux: {nb_speciaux}")
    print()
    """
    if nb_speciaux < 1 or nb_majuscules < 1 or nb_chiffres < 1 or nb_caracteres < 5:
        print(f"Attetion ce mot de passe n'est pas sécurisé: {mot_de_passe}")
    
