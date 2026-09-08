


def puissance(a,b):
    print("Le type de la premiere valeur est : ",type(a))
    print("Le type de la deuxieme valeur est : ",type(b))
    if not type(a) is int :
          raise TypeError("Only integers are allowed")
    if not type(b) is int :
          raise TypeError("Only integers are allowed")

    if a < 0:
          raise ValueError("Opération indéfinie pour un nombre négatif")
    resultat = a**b
    return resultat

