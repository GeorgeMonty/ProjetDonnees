import csv
import json
import donnees as dn

class Jeux_donnees:
    """
    Une classe pour importer les jeux de donnees des fichiers .csv et .json
       
    Attributs
    ---------
    lien_fichier : str
                    le lien du fichier qui contient ce jeu de données
                    il faut séparer ce lien avec les / par exemple 'C:/documents/nom_fichier.csv'
    
    __type_fichier : str
                    le format du fichier i.e. 'csv' ou 'json'
    
    Exemples
    --------
    >>> jd = Jeux_donnees('C:/documents/file1.csv')
    >>> donnees = jd.importer()
   
    """
    
    def __init__(self,lien_fichier):
        """<Constructeur>
        Création d'un nouvelle jeu de données
        

        Parametres
        ----------
        lien_fichier : str
                    le lien du fichier qui contient ce jeu de données
                    il faut séparer ce lien avec les / par exemple 'C:/documents/nom_fichier.csv'

        Exemples
        -------
        >>> jd = Jeux_donnees('C:/documents/file1.csv')

        """
        self.lien_fichier = lien_fichier
        self.__type_fichier = lien_fichier.split('.')[-1]
        
        
    def importer(self):
        """
        Importer les donnees de ce jeux de donnees comme au forme de classe Donnees.
        
        On ne peut que importer les fichiers .csv et .json
        Les fichiers .csv sont presentés comme une list des lists et les fichiers 
        .json un dictionnaire des dictionnaires
        
        Parametres
        ----------
        None
        
        Returns
        -------
        Donnees
            Les donnees de ce jeu de donnees.
            
        Exemples
        --------
        >>> jd = Jeux_donnees('C:/documents/file1.csv')
        >>> donnees = jd.importer()
        
        >>> jd2 = Jeux_donnees('C:/documents/file2.json')
        >>> donnees2 = jd2.importer()
        
        >>> jd3 = Jeux_donnees('C:/documents/file3.txt')
        >>> donnees3 = jd3.importer()
        Exception: Type de fichier inconnu
        
        """
        path = self.lien_fichier.split('/')
        filename = path[-1]
        
        folder=''
        for i in range(len(path)-1):
            folder = folder + path[i] + '/'
            
        if self.__type_fichier == 'csv':
            data = []
            
            with open(folder + filename, encoding='ISO-8859-1') as csvfile :
                covidreader = csv.reader(csvfile, delimiter=';')
                for row in covidreader :
                    data.append(row)
            #renommer le variable reg à numReg
            variables = data[0]
            for i in range(len(variables)):
                if variables[i] == 'reg':
                    variables[i] = 'numReg'
                #les variables jour, numreg et dep sont str, les autres doit être int
                #on inclure variable dep à cause des departements 2A et 2B
                #on inclure numReg aussi pour rendre plus intuitif le fonction d'aggregation spatial
                if variables[i] == 'jour':
                    pass
                elif variables[i] == 'nomReg':
                    pass
                elif variables[i] == 'dep':
                    pass
                elif variables[i] == 'numReg':
                    pass
                else:
                    for entry in data[1:]:
                        entry[i] = int(entry[i])
                
            return dn.Donnees(data,'csv')
        
        elif self.__type_fichier == 'json':
            with open(folder + filename) as json_file :
                data = json.load(json_file)
            return dn.Donnees(data, 'json')
        
        else:
            raise Exception("Type de fichier inconnu")
