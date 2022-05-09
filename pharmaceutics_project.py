# -*- coding: utf-8 -*-
"""
Created on Fri May  6 11:00:34 2022

@author: waelc
"""
#STOCK======================================================
def AjouterMedicament(Stock):
    nom=str(input('entrez le nom du medicament : '))  
    nomfournisseur=str(input('entrez le fournisseur du medicament : '))
    Id=int(input('entrez le Id du medicament : '))
    Prix=float(input('entrez le prix du medicament : '))
    Stock.append([nom,nomfournisseur,Id,Prix])
    print(Stock)



def SupprimerMedicament(Stock):
    print('entrez le Id du medicament a supprimer : ')
    while True:
        try:
            Idasupprimer=int(input())
            break
        except:
            print('id invalide ! \n')
    for i in range(len(Stock)-1):
        if Idasupprimer!=Stock[i][2]:
            print('ce medicament nest pas dans le stock \n')
        else:
            Stock.pop(i)
    print(Stock)

def ModifierMedicament(Stock):
    print('entrez le Id du medicament a modifier : ')
    while True:
        try:
            idamodifier=int(input())
            break
        except:
            print('id invalide')
    for i in range (len(Stock)):
        if idamodifier==Stock[i][2]:
            while True:
                try:
                    nom=str(input('entrez le nom du medicament : '))
                    break
                except:
                    print('le nom nest pas valide')
            while True:
                try:
                    nomfournisseur=str(input('entrez le fournisseur du medicament : '))
                    break
                except:
                    print('le nom du fournisseur nest pas valide')
            while True:
                 try:
                     Prix=float(input('entrez le prix du medicament : '))
                     break
                 except:
                     print('le prix nest pas valide')
            Stock[i]=[[nom,nomfournisseur,idamodifier,Prix]]
        else:
            print('le id nexiste pas \n')
            ModifierMedicament(Stock)

def RechercherMedicament(Stock):
    #recursivité
    h=0
    print('entrez le Identifiant du medicament souhaite : ')
    while True:
        try:
            idarechercher=int(input())
            break
        except:
            print('id invalide')
    for i in range(len(Stock)):
        if idarechercher==Stock[i][2]:
            print(Stock[i])
            h=1
            break
    if h==1:
        return Stock[i]
    else:
        print('identifiant errone ! veuillez reessayez ')
        RechercherMedicament(Stock)
#FIN STOCK==================================================================
            
#Fournisseur================================================================    

def AjouterFournisseur(Fournisseurs):
    print('donner le nom du fournisseur')
    
    nomfournisseur=str(input())
    addrfournisseur=str(input())
    specfournisseur=str(input())
    numfournisseur=int(input())
            
    Fournisseurs+=[[nomfournisseur,addrfournisseur,specfournisseur,numfournisseur]]
    print('Fournisseurs : ',Fournisseurs)

def SupprimerFournisseur(Fournisseur):
    x=0
    while x!=1:
        print('Entrez le nom du fournisseur a supprimer : ')
        nomasupp=str(input())
        for i in range(len(Fournisseur)):
            if nomasupp==Fournisseur[i][0]:
                Fournisseur.pop(i)
                x=1
            else:
                print('fournisseur introuvable ')
    print(Fournisseur)
def ModifierFournisseur(Fournisseur):
    print('entrez le nom du fournisseur a modifier : ')
    x=0
    while x!=1:
        nomamodif=str(input())
        for i in range(len(Fournisseur)):
            if nomamodif==Fournisseur[i][0]:
                nouvnom=str(input('entrez le nouveau Nom : '))
                nouvaddr=str(input('entrez la nouvelle addresse : '))
                nouvnum=int(input('entrez le nouveau numero de tel : '))
                Fournisseur[i][0]=nouvnom
                Fournisseur[i][1]=nouvaddr
                Fournisseur[i][3]=nouvnum
                x=1
            else:
                print('Fournisseur introuvable')          
    print(Fournisseur)
#================================================================
    
#Utilisateurs=================================================================
def AjouterUtilisateur(utilisateurs):
    nomutil=''
    mdputil=''
    print('Entrez un nom dutilisateur')
    nomutil=str(input())
           
           
    while len(mdputil)<4:
        try:
            mdputil=str(input('veuillez entrez votre mot de passe : \n'))
            break
        except:
            print('mot de passe invalide \n')
    print('appuyez sur 1 pour ajouter un employe \n')
    print('appuyez sur 2 pour ajouter un Admin \n')
    choix1=int(input())
    if choix1==1:
        utilisateurs.append({'username':nomutil,'password':mdputil,'Type':'Employee'})
    elif choix1==2:
        utilisateurs.append({'username':nomutil,'password':mdputil,'Type':'Admin'})
    else:
        print('choix invalide')
def SupprimerUtilisateur(Utilisateurs):
    print('Entrez le nom que vous souhaitez supprimer :')
    y=0
    while True:
        try:
            nomutilsupp=str(input())
            break
        except:
            print('nom invalide , veuillez reessayer !')
    for x in Utilisateurs:
       if nomutilsupp==x['username']:
           Utilisateurs.remove(x)
           print('Utilisateur supprime !')
           y=1
    if y==0:
        print('utilisateur introuvable')
        SupprimerUtilisateur(Utilisateurs)
        
def ModifierUtilisateur(Utilisateurs):
    y=0
    print('Entrez le Nom du utilisateur a modifier : ')
    while True:
        try:
            nomutilmodif=str(input())
            break 
        except:
            print('nom invalide , veuillez reessayer !')
    for x in Utilisateurs:
       if nomutilmodif==x['username']:
           nouvnomutil=''
           nouvmdputil=''
           print('Entrez un nouveau nom dutilisateur')
           while True:
               try:
                   nouvnomutil=str(input())
                   break
               except:
                   print('nom invalide , veuillez reessayer')
           while len(nouvmdputil)<4:
               try:
                   nouvmdputil=str(input('veuillez entrez un mot de passe qui excede 4 caracteres : \n'))
                   break
               except:
                   print('mot de passe invalide \n')
           print('appuyez sur 1 pour employe \n')
           print('appuyez sur 2 pour Admin \n')
           choix1=int(input())
           if choix1==1:
               x['username']=nouvnomutil
               x['password']=nouvmdputil
               x['Type']='Employee'
               print('Utilisateur modifie !')
           elif choix1==2:
               x['username']=nouvnomutil
               x['password']=nouvmdputil
               x['Type']='Admin'
               print('Utilisateur modifie !')
           else:
               print('choix invalide')
           y=1
    if y==0:
        print('utilisateur introuvable')
        ModifierUtilisateur(Utilisateurs)
        
        
        
        
def AfficherUtilisateur(Utilisateurs):
    print(Utilisateurs)

#=============================================================================


#Vente========================================================================
def AjouterVente(Ventes,vente,stock):
    codevente=int(input('entrez un code a la vente : '))
    totalar=0
    totalapr=0
    print('entrez le nombre de medicaments a ajouter : ')
    nbr=int(input())
    for i in range(nbr):
        x=int(input('entrez le id du medicament'))
        for y in range(len(stock)):
            if x==stock[y][2]:
                print('quelle quantitee de ',stock[y][0],'?')
                qte=int(input())
                totalindividuel=qte*stock[y][3]
                cpstock=stock[y]
                cpstock+=[qte,totalindividuel]
                vente.append(cpstock)
                totalar+=totalindividuel
    print('medicaments ajoutes avec succes')
    remise=RemiseVente()
    totalapr=totalar-totalar*remise
    vente.append(codevente)
    Ventes.append(vente)                            
    print(vente,'et le total apres remise est : ',totalapr)






def ModifierVente(ventes):
    print('entrez le code de la vente a modifier :')
    codeamodifier=int(input())
    print('entrez le nombre de medicaments a modifier :')
    nbr=int(input())
    for i in range(nbr):
        for y in range(len(ventes)):
            if codeamodifier==ventes[y][-1]:
                nouvqte=int(input('entrez la nouvelle qtite du medicament '))
                ventes[y][0][4]=nouvqte
    print('modification effectuee')        
        
        





def AfficherVente(ventes):
    for i in range(len(ventes)):
        print('la vente numero ',i, ' : ')
        print(ventes[i])





def RemiseVente():
    remise=0
    while remise not in range(1,100):
        print('veuillez entrez la remise souhaite : ')
        remise=int(input())
    print('une remise de ',remise,'% a ete emise')
    return remise*0.01

#===============================================================================

#MENUS=========================================================================


def MenuStock():
    print('appuyez sur 1 pour ajouter un medicament')
    print('appuyez sur 2 pour Supprimer un medicament')
    print('appuyez sur 3 pour modifier un medicament')
    print('appuyez sur 4 pour rechercher un medicament')
    print('appuyez sur 5 pour afficher la liste de medicaments ')
    print('appuyez sur 6 pour quitter')
    option=int(input('entrez votre choix : '))
    if option==1:
        AjouterMedicament(listeStock)
        MenuStock()
    elif option==2:
        SupprimerMedicament(listeStock)
        MenuStock()
    elif option==3:
        ModifierMedicament(listeStock)
        MenuStock()
    elif option==4:
        RechercherMedicament(listeStock)
        MenuStock()
    elif option==5:
        print(listeStock)
        MenuStock()
    elif option==6:
        MenuGeneral()
    else:
        print('vous avez entrez un nombre faux !')
        MenuStock()
        
def MenuFournisseur():
    print('appuyez sur 1 pour ajouter un Fournisseur')
    print('appuyez sur 2 pour Supprimer un Fournisseur')
    print('appuyez sur 3 pour modifier un Fournisseur')
    print('appuyez sur 4 pour quitter ')
    option=int(input('entrez votre choix : '))
    if option==1:
        AjouterFournisseur(listeFournisseurs)
        MenuFournisseur()
    elif option==2:
        SupprimerFournisseur(listeFournisseurs)
        MenuFournisseur()
    elif option==3:
        ModifierFournisseur(listeFournisseurs)
        MenuFournisseur()
    elif option==4:
        MenuGeneral()
    else:
        print('vous avez entrez un nombre faux !')
        MenuFournisseur()
    
def MenuUtilisateur():    
    print('appuyez sur 1 pour ajouter un utilisateur')
    print('appuyez sur 2 pour supprimer un utilisateur')
    print('appuyez sur 3 pour modifier un utilisateur')
    print('appuyez sur 4 pour afficher la liste des utilisateurs')
    print('appuyez sur 5 pour quitter')
    option=int(input('entrez votre choix : '))
    if option==1:
        AjouterUtilisateur(listeUtilisateurs)
        MenuUtilisateur()
    elif option==2:
        SupprimerFournisseur(listeUtilisateurs)
        MenuUtilisateur()
    elif option==3:
        ModifierFournisseur(listeUtilisateurs)
        MenuUtilisateur()
    elif option==4:
        AfficherUtilisateur(listeUtilisateurs)
        MenuUtilisateur()
    elif option==5:
        MenuGeneral()
    else:
        print('vous avez entrez un nombre faux !')
        MenuUtilisateur()

def MenuVentes():
    print('appuyez sur 1 pour ajouter une Vente')
    print('appuyez sur 2 pour modifier une Vente')
    print('appuyez sur 3 pour afficher la liste des Ventes')
    print('appuyez sur 4 pour quitter')
    option=int(input('entrez votre choix : '))
    if option==1:
        AjouterVente(listeDeVentes,listeVenteunit,listeStock)
        MenuVentes()
    elif option==2:
        ModifierVente(listeDeVentes)
        MenuVentes()
    elif option==3:
        AfficherVente(listeDeVentes)
        MenuVentes()
    elif option==4:
        MenuGeneral()
    else:
        print('vous avez entrez un nombre faux !')
        MenuVentes()

def MenuGeneral():
    print('Bienvenu dans le service pharmacetique !')
    print('appuyez sur 1-pour accedez au menu Gestion de Stock')
    print('2- pour la gestion des fournisseurs')
    print('3- pour la gestion des utilisateurs')
    print('4- pour la gestion de vente')
    choix=int(input('entrez votre choix : '))
    if choix==1:
        MenuStock()
    elif choix==2:
        MenuFournisseur()
    elif choix==3:
        MenuUtilisateur()
    elif choix==4:
        MenuVentes()
    else:
        print('vous avez entrez un nombre faux !')
        MenuGeneral()
        








listeDeVentes=[]
listeVenteunit=[]
listeUtilisateurs=[]
listeFournisseurs=[]
listeStock=[]
username1='wow'
password1='wow'
while username1!='admin':
    username1=str(input('entrez le nom d utilisateur'))
while password1!='admin':
    password1=str(input('entrez le mot de passe'))
MenuGeneral()
