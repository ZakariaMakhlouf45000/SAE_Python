
# -----------------------------------------------------------------------------------------------------
# listes de fonctions à implémenter
# -----------------------------------------------------------------------------------------------------

def taux_reussite(resultat):
    """calcule le pourcentage de réussite correspondant au résultat

    Args:
        resultat (tuple): le résultat d'un collège pour une session (année)
        
    Returns:
        float:  le pourcentage de réussite (nb. admis / nb. présents ā la session)
    """
    if not resultat :
        return None
    return resultat[4] /  resultat[3] *100 

def meilleur(resultat1, resultat2):
    """vérifie si resultat1 est meilleur que resultat2 au sens des taux de réussites

    Args:
        resultat1 (tuple): un résultat d'un collège pour une session (année)
        resultat2 (tuple): un autre résultat d'un collège pour une session (année)

    Returns:
        bool:   True si le taux de réussite de resultat1 est supérieur ā celui de resultat2
    """
    if not resultat1 or not resultat2 :
        return None
   
    return taux_reussite(resultat1) > taux_reussite(resultat2) 

def meilleur_taux_reussite(liste_resultats):
    """recherche le meilleur taux de réussite dans une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le meilleur taux de rēussite
    """
    if liste_resultats == []:
        return None
    
    meilleurTaux = liste_resultats[0]

    for elem in liste_resultats:
        if meilleur(elem,meilleurTaux):
            meilleurTaux = elem
    return taux_reussite(meilleurTaux)

def pire_taux_reussite(liste_resultats):
    """recherche le pire taux de réussite parmi une liste de résultats

    Args:
        liste_resultats (list): une liste de resultats

    Returns:
        float: le pire taux de rēussite
    """
    if liste_resultats == []:
        return None
    
    pireTaux = liste_resultats[0]

    for elem in liste_resultats:
        if meilleur(pireTaux,elem):
            pireTaux = elem
    return taux_reussite(pireTaux)
    
def total_admis_presents(liste_resultats):
    """calcule le nombre total de candidats admis et de candidats présents aux épreuves du DNB parmi les résultats de la liste passée en paramètre

    Args:
        liste_resultats (list): une liste de résultats
    session , patronyme, departement, nombre_de_presents, nombre_total_d_admis
    Returns:
        tuple : un couple d'entiers contenant le nombre total de candidats admis et prēsents
    """
    nombre_totale = 0
    nompbre_present = 0
    for i in range(len(liste_resultats)):
        nombre_totale += liste_resultats[i][4]
        nompbre_present += liste_resultats[i][3]
    return (nombre_totale,nompbre_present)

def filtre_session(liste_resultats, session):
    """génère la sous-liste de liste_resultats, restreinte aux résultats de la session demandée

    Args:
        liste_resultats (list): une liste de résultats
        session (int): une session (année)

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats de la session demandēe
    """
    sous_liste = []
    for i in range(len(liste_resultats)):
        if liste_resultats[i][0] == session:
            sous_liste.append(liste_resultats[i])
    return sous_liste

def filtre_departement(liste_resultats, departement):
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département demandé

    Args:
        liste_resultats (list): une liste de résultats
        departement (int): un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du dēpartement demandé
    """
    sous_liste = []
    for i in range(len(liste_resultats)):
        if liste_resultats[i][2] == departement:
            sous_liste.append(liste_resultats[i])

    return sous_liste

def filtre_college(liste_resultats, nom, departement):
    """génère la sous-liste de liste_resultats, restreinte aux résultats du département donné et dont le nom du collège contient le nom passé en paramètre (en minuscule ou majuscule)

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (éventuellement incomplet)
        departement (int) : un numéro de département

    Returns:
        list: la sous-liste de liste_resultats, restreinte aux résultats du collège et du département recherchēs
    """
    sous_liste = []
    for i in range(len(liste_resultats)):
        nom_College = liste_resultats[i][1] 
        depart = liste_resultats[i][2]
        if depart == departement :
            if  nom.lower() in nom_College.lower()  :
                sous_liste.append(liste_resultats[i])
    return sous_liste

def taux_reussite_global(liste_resultats, session):
    """calcule le taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)
        session, patronyme, departement, nombre_de_presents, nombre_total_d_admis
    Returns:
        float: taux (pourcentage) de réussite au DNB sur l'ensemble des collèges pour une session donnēes
    """
    total_ad = 0
    total_present = 0

    for i in range(len(liste_resultats)):

        if liste_resultats[i][0] == session:
            total_ad += liste_resultats[i][4]
            total_present += liste_resultats[i][3]
        elif total_present == 0: 
            return None
     
    return total_ad / total_present * 100 

def moyenne_taux_reussite_college(liste_resultats, nom, departement):
    """calcule la moyenne des taux de réussite d'un collège sur l'ensemble des sessions

    Args:
        liste_resultats (list): une liste de résultats
        nom (str): un nom de collège (exact)
        departement (int) : un numéro de département
        
    Returns:
        float: moyenne des taux de rēussite d'un collège sur l'ensemble des sessions
    """
    total_ad = 0.0
    total_present = 0.0
    nombre_session = 0.0
    total_pourcentage = 0.0

    for i in range(len(liste_resultats)):
        nom_College = liste_resultats[i][1]
        dept = liste_resultats[i][2]
        if  nom in nom_College and dept == departement: 
            total_ad = liste_resultats[i][4]
            total_present = liste_resultats[i][3]
            total_pourcentage += (total_ad / total_present * 100)
            nombre_session += 1

        
    return total_pourcentage / nombre_session
           
liste2 = [(2020, 'ALBERT SIDOISNE', 28, 134, 118),
          (2020, 'ANATOLE FRANCE', 28, 63, 47),
          (2020, 'DE NERMONT - CHATEAUDUN', 28, 74, 60),
          (2020, 'DE NERMONT - NOGENT', 28, 28, 27),
          (2020, 'EMILE ZOLA', 28, 103, 88),
          (2020, 'GILBERT COURTOIS', 28, 22, 18),
          (2020, 'MATHURIN REGNIER', 28, 152, 118),
          (2021, 'DE BEAUMONT LES AUTELS', 28, 37, 34),
          (2021, 'DE NERMONT - CHATEAUDUN', 28, 71, 60),
          (2021, 'EMILE ZOLA', 28, 96, 85),
          (2021, 'GILBERT COURTOIS', 28, 24, 15),
          (2021, 'JEAN MONNET', 28, 97, 91),
          (2021, 'LA PAJOTTERIE', 28, 91, 72),
          (2021, 'ND - LA LOUPE', 28, 12, 9),
          (2021, 'PIERRE BROSSOLETTE', 28, 93, 70),
          (2021, 'SULLY', 28, 14, 10),
          ]

def meilleur_college(liste_resultats, session):
    """recherche le collège ayant obtenu le meilleur taux de réussite pour une session donnée

    Args:
        liste_resultats (list): une liste de résultats
        session (int) : une session (année)

    Returns:
        tuple: couple contenant le nom du collège et le dēpartement
    """
    meilleurTaux = 0
    meilleurNom = None
    meilleurDep = None

    for i in range(len(liste_resultats)):
        res = liste_resultats[i]
        if res[0] == session:
            nom = res[1]
            depart = res[2]
            tauxDeReussite = taux_reussite(res)
            if tauxDeReussite > meilleurTaux:
                meilleurTaux = tauxDeReussite
                meilleurNom  = nom
                meilleurDep  = depart
    if meilleurNom is None :
        return None
    return meilleurNom , meilleurDep
print(meilleur_college(liste2,2021))

def liste_sessions(liste_resultats):
    """retourne la liste des sessions (années) dont au moins un résultat est reporté dans la liste de résultats.
    ATTENTION : la liste renvoyée doit être sans doublons et triée par ordre chronologique des sessions 

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        list: une liste de session (int) triēe et sans doublons
    """
    liste_session = []
    for i in range(len(liste_resultats))  :
        if liste_resultats[i][0] not in liste_session :
            liste_session.append(liste_resultats[i][0])
    liste_session.sort()
    return liste_session

def plus_longe_periode_amelioration(liste_resultats):
    """recherche la plus longue periode d'amélioration du taux de réussite global au DNB

    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        tuple: un couple contenant la session (année) de début de la période et la session de fin de la pēriode
    """
    pass

def est_bien_triee(liste_resultats):
    """vérifie qu'une liste de résultats est bien triée dans l'ordre chronologique des sessions puis dans l'ordre croissant des départements puis dans l'ordre alphabétique des noms de collèges
    
    Args:
        liste_resultats (list): une liste de résultats

    Returns:
        bool: True si la liste est bien triēe et False sinon
    """
    pass


def fusionner_resultats(liste_resultats1, liste_resultats2):
    """Fusionne deux listes de résultats triées sans doublons en une liste triée sans doublon
    sachant qu'un même résultat peut être présent dans les deux listes

    Args:
        liste_resultat1 (list): la première liste de résultats
        liste_resultat2 (list): la seconde liste de résultats

    Returns:
        list: la liste triée sans doublon comportant tous les rēsultats de liste_resultats1 et liste_resultats2
    """
    pass


def charger_resultats(nom_fichier):
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des rēsultats contenus dans le fichier
    """
    pass
