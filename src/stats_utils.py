import statistics
def analyser_ventes(transactions):
    """
    Analyse une liste de montants de transactions (ventes).
    Filtre les valeurs invalides, calcule les indicateurs statistiques
    cles et detecte les transactions anormalement elevees (> 2x moyenne).
    """
    ventes_valides = []


    for vente in transactions:
        if vente > 0:
            ventes_valides.append(vente)

    # Si aucune transaction n'est valide = retourne résultats à 0
    if len(ventes_valides) == 0:
        return {
            "nombre_transactions": 0,
            "somme_totale": 0,
            "moyenne": 0,
            "mediane": 0,
            "ecart_type": 0,
            "minimum": 0,
            "maximum": 0,
            "anomalies": []
        }

    # Nombre total de transactions valides
    nombre_transactions = len(ventes_valides)

    # Somme totale des ventes
    somme_totale = sum(ventes_valides)

    # Moyenne
    moyenne = somme_totale / nombre_transactions

    # Médiane
    mediane = statistics.median(ventes_valides)

    # Écart-type
    ecart_type = statistics.pstdev(ventes_valides)

    # Valeur minimale et maximale
    minimum = min(ventes_valides)
    maximum = max(ventes_valides)

    # Détection des anomalies
    anomalies = []

    for vente in ventes_valides:
        if vente > 2 * moyenne:
            anomalies.append(vente)

    # Résultats
    resultats = {
        "nombre_transactions": nombre_transactions,
        "somme_totale": somme_totale,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "minimum": minimum,
        "maximum": maximum,
        "anomalies": anomalies
    }

    return resultats


def calculer_marge_erreur(liste_nombres):
    """
    Calcule la marge d'erreur (etendue) d'une liste de nombres :
    la difference entre la valeur maximale et la valeur minimale.
    """
    if not liste_nombres:
        return 0
    return max(liste_nombres) - min(liste_nombres)

# Test
transactions_test = [
    50,
    100,
    -10,
    80,
    0,     
    120,
    -25,
    90,
    1000   # Potentielle anomalie
]

resultats = analyser_ventes(transactions_test)


print("=== Analyse des ventes ===")
print("Nombre de transactions valides :", resultats["nombre_transactions"])
print("Somme totale :", resultats["somme_totale"], "€")
print("Moyenne :", round(resultats["moyenne"], 2), "€")
print("Médiane :", round(resultats["mediane"], 2), "€")
print("Écart-type :", round(resultats["ecart_type"], 2), "€")
print("Minimum :", resultats["minimum"], "€")
print("Maximum :", resultats["maximum"], "€")
print("Anomalies :", resultats["anomalies"])
print("Marge d'erreur (etendue) :", calculer_marge_erreur(transactions_test), "€")