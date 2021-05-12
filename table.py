from tabulate import tabulate
from statistique import Statistique

class Table :
    """Permet de créer des tableaux
    
    Attributes
    ----------
    liste_stat : une liste contenant des listes de statistiques
        les listes de statistiques viennent de la classe Statistique
    
    Example
    -------
    >>> liste_stat=[["Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne", "Centre-Val de Loire", "Corse", "Grand-Est", "Guadeloupe", "Guyane", "Hauts-de-France", "Ile-de-France", "La Réunion", "Martinique", "Mayotte", "Normandie", "Nouvelle-Aquitaine", "Occitanie", "Pays de la Loire", "Provence-Alpes-Côte d'Azur"],[12,10,13.2,12.8,9,7,6.7,5.9,13,12,12,10.3,10.4,9.3,14,16,10.6,12.5]]
    >>> table1 = Table(liste_stat)
    >>> table1.creer_table()
    >>> table1.afficher_table()    
    
    """
    def __init__(self,liste_stat):
        self.liste_stat=liste_stat
        
    def creer_table(self):
        self.nb_colonnes = len(self.liste_stat)
        self.nb_lignes=len(self.liste_stat[0])
        interieur_table=[]
        for j in range(self.nb_lignes):
            listetable = [self.liste_stat[i][j] for i in range(self.nb_colonnes)]
            interieur_table.append(listetable)
        self.tableàretourner = tabulate(interieur_table,tablefmt='fancy_grid')

    def afficher_table(self):
        print(self.tableàretourner)

