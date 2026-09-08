


def puissance(a,b):
    resultat = 0 
    print("Le type de la premiere valeur est : ",type(a))
    print("Le type de la deuxieme valeur est : ",type(b))
    if not type(a) is int :
          raise TypeError("Only integers are allowed")
    if not type(b) is int :
          raise TypeError("Only integers are allowed")

    if a == 0 and b < 0 :
          raise ValueError("Opération indéfinie pour un nombre négatif")
    
    for i in range(b): 
        resultat += a
    return resultat

