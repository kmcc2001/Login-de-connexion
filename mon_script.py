Id = input("login : ")

if Id == "Bébert" or Id == "Alfred":
    remaining_attempts = 3
    
    while remaining_attempts > 0:
        mdp = input("mot de passe : ")
        
        if Id == "Bébert" and mdp == "bb123":
            print("Bienvenue !")
            break
        elif Id == "Alfred" and mdp == "aa123":
            print("Bienvenue !")
            break
        else:
            remaining_attempts -= 1
            print(f"Mot de passe incorrect. Il vous reste {remaining_attempts} tentative(s).")
    
    if remaining_attempts == 0:
        print("Nombre de tentatives dépassé. Veuillez réessayer plus tard.")
else:
    print("Utilisateur non reconnu, au revoir...")
