print("Hello, World!")
import fonctions as f

print(type(2))

while True :
     
     val1 = input("val a ?\n")
     if "." in val1 or "," in val1:
        raise ValueError("Pas de float autorisé !")
     val1 = int(val1)

     val2 = input("val b ?\n")
     if "." in val2 or "," in val2:
        raise ValueError("Pas de float autorisé !")
     val2 = int(val2)
    

     resultat = f.puissance(val1,val2)
     print(resultat)

