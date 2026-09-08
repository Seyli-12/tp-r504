


def puissance(a,b):
    resultat = 1 
     
    if not type(a) is int :
          raise TypeError("Only integers are allowed")
    if not type(b) is int :
          raise TypeError("Only integers are allowed")

    if a == 0 and b < 0 :
          raise ValueError("Opération indéfinie pour un nombre négatif")
    
    if b < 0 :
        for i in range(abs(b)): 
            resultat *= a
        return (1/resultat)
    for i in range(b):
        resultat*= a 
    return resultat

