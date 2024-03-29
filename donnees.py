import numpy as np
import csv

class Donnees:
    """
    Une classe des jeux des données importés
    
    Vous pouvez utiliser certains fonctions sur les Donnees pour ajouter et effacer certains
    variables et éléments.
       
    Attributs
    ---------
    donnees : iterable
                    les données importés de ce jeu des données. Si les données sont d'une fichiers
                    .csv  ils sont presentés comme une list des lists et les données sont d'une 
                    fichier .json ils sont presentés comme un dictionnaire des dictionnaires
    
    variables : iterable
                    les variables (les colonnes) de ce jeu des données i.e. le premier ligne

                    les variables (les colonnes) de ce jeu des données i.e. la première lign
                    des données
                    
        fichier : str
                    le format du fichier i.e. 'csv' ou 'json'
    
    Exemples
    --------
    >>> jd = Jeux_donnees('C:/documents/file1.csv')
    >>> donnees = jd.importer()
   
    """    
    def __init__(self, donnees,type_fichier):
        """<Constructeur>
        
        Parametres
        ----------
        donnees
            Les donnees du jeu de données.
        type_fichier : str
            Le format du fichier d'origin du jeux de donnees.
        
        Exemples
        --------
        >>> d1 = Donnees(['jour', 'numReg', 'incid_rea','dc'],['2000-08-29', '01', '44','12']],'csv')
        >>> d1.variables
        ['jour', 'nomReg', 'numReg', 'incid_rea','dc']
        >>> d1.donnees
        [['jour', 'numReg', 'incid_rea','dc'],['2000-08-29', '01', '44','12']]        
        
        """
        self.donnees = donnees
        self.type_fichier = type_fichier
        if self.type_fichier == 'csv':
            self.variables = self.donnees[0]
        elif self.type_fichier == 'json':
            self.variables = ['Calendrier', 'Academie']
        else:
            raise Exception("Un objet de la Classe Donnees doit venir d\'un fichier .csv ou .json")
     
    
    def jointure(self,donnee2):
        """
        Une fonction pour joindre 2 jeux des données.
        ATTENTION: Cette fonction est assez lent avec les jeux de données trop grandes
            donc il est recommandé que vous utiliser les autres fonctions avant de 
            faire un jointure pour reduire le taille de vos données

        Parametres
        ----------
        donnee2 : Donnees
            Le jeu des données qu'on veut joindre.

        Returns
        -------
        Donnees
            Le nouveaux jeu des données.
            
        Exemples
        --------
        >>> d1 = Jeux_donnees('C:/documents/file1.csv').importer()
        >>>d2 = Jeux_donnees('C:/documents/file2.csv').importer()
        >>>d1.donnees
        [['jour', 'numReg', 'incid_rea'],['2000-08-29', '01', 44]]
        >>> d2.donnees
        [['jour', 'numReg','dc'],['2000-08-29', '01',12]]
        >>>d3 = d1.jointure(d2)
        >>>d3.donnees
        [['jour', 'numReg', 'incid_rea','dc'],['2000-08-29', '01', 44, 12]]
        
        """
        if self.type_fichier == 'csv':
            if donnee2.type_fichier == 'csv':
                step=0
                data1 = self.donnees
                data2 = donnee2.donnees
                variables1 = tuple(data1[0])
                variables2 = tuple(data2[0])
                variables_partages = []
                for i in variables1:
                    est_partage = False
                    for j in variables2:
                        if i == j:
                            est_partage = True
                    if est_partage == True:
                        variables_partages.append(i)
                tuple_variables = ('jour','dep','Zone','numReg','nomReg','sexe','cl_age90','hosp','rea','rad','dc','nb','incid_hosp','incid_rea','incid_rad','incid_dc')
                new_variables = list(tuple_variables)
                new_data = [new_variables]
                for entry1 in data1[1:]:
                    step=step+1
                    new_entry=[]
                    for variable in new_variables:
                        new_entry.append(None)
                    for j in range(len(new_variables)):
                        for i in range(len(variables1)):
                            if variables1[i] == new_variables[j]:
                                new_entry[j]=entry1[i]
                    new_data.append(new_entry)
                step = 0 
                final_data = [new_variables]
                for join_entry in new_data[1:]:
                    step = step + 1
                    for entry2 in data2[1:]:
                        final_entry = tuple(join_entry)
                        final_entry = list(final_entry)
                        join = True
                        for var_par in variables_partages:
                            for j in range(len(variables2)):
                                if variables2[j] == var_par:
                                    for k in range(len(new_variables)):
                                        if new_variables[k] == var_par:
                                            if entry2[j] != join_entry[k]:
                                                join = False
                        if join == True:
                            for l in range(len(new_variables)):
                                for m in range(len(variables2)):
                                    if variables2[m] == new_variables[l]:
                                        final_entry[l]=entry2[m]            
                            final_data.append(final_entry)
                                    
                new_donnees = Donnees(final_data,'csv')
                final_variables = list(variables1)
                for var in variables2:
                    final_variables.append(var)
                new_donnees.selection_variables(final_variables)
                print("Finished")
                return new_donnees                          
            else:
                raise Exception("On ne peut que faire les jointures sur les fichiers. csv")
        else:
            raise Exception("On ne peut que faire les jointures sur les fichiers. csv")
    
    def fenetrage(self,date_debut='0000-00-00',date_fin='999999-999-999'):
        """
        Effacer les éléments d'un jeu des données qui ne sont pas entre les 
        dates données

        Parametres
        ----------
        date_debut : str, optional
            Le premier date de votre fenêtrage (inclus).
            Le date dait être du forme 'aaaa-mm-jj' e.g.'2020-08-01'.
            Si on ne donne pas un date début le programme suppose un 
            date de '0000-00-00'.
        date_fin : str, optional
            Le final date de votre fenêtrage (inclus).
            Le date dait être du forme 'aaaa-mm-jj' e.g.'2020-08-01'.
            Si on ne donne pas un date fin le programme suppose un 
            date de '999999-999-999'.

        Returns
        -------
        Donnees
            Le nouveau jeu de données

        Exemples
        -------
        >>> d1 = Jeux_donnees('C:/documents/file1.csv').importer()
        >>> d1.fenetrage('2020-03-29','2020-04-29')
        
        >>> d2 = Jeux_donnees('C:/documents/file2.csv').importer()
        >>> d2.fenetrage('2021-01-01') 
        #cela va effacer tous les éléments de d2 qui s'est passé avant le 2021-01-01
        
        >>> d3 = Jeux_donnees('C:/documents/file3.csv').importer()
        >>> d3.fenetrage(date_fin='2020-08-29') 
        #cela va effacer tous les éléments de d3 qui s'est passé après le 2020-08-29
        

        """
        data = tuple(self.donnees)
        data = list(data)
        date_debut = date_debut.split('-')
        date_fin = date_fin.split('-')
        variables = self.variables
        i=0
        for var in variables:
            if var == 'jour':
                col_jour = i
            i = i+1
            
        for entry in data[1:]:
            date = entry[col_jour].split('-')
            if int(date[0]) < int(date_debut[0]):
                data.remove(entry)
            elif int(date[0]) == int(date_debut[0]):
                if int(date[1]) < int(date_debut[1]):
                    data.remove(entry)
                elif int(date[1]) == int(date_debut[1]):
                    if int(date[2]) < int (date_debut[2]):
                        data.remove(entry)
            if int(date[0]) > int(date_fin[0]):
                data.remove(entry)
            elif int(date[0]) == int(date_fin[0]):
                if int(date[1]) > int(date_fin[1]):
                    data.remove(entry)
                elif int(date[1]) == int(date_fin[1]):
                    if int(date[2]) > int (date_fin[2]):
                        data.remove(entry)
        return Donnees(data,"csv")                
    
    
    def selection_variables(self,variables):
        """
        Choisir et effacer les variables (les colonnes) d'un jeu des données

        Parametres
        ----------
        variables : iterable(str)
            Une liste des variables que vous voulez garder dans le jeu de données.

        Returns
        -------
        Donnees.
            Une nouvelle jeu de données avec les variables souhaités
    
        Exemples
        --------
        >>> d1 = Jeux_donnees('C:/documents/file1.csv').importer()
        >>> d1.variables
        ['jour', 'nomReg', 'numReg', 'incid_rea','dc']
        >>> d1.selection_variables(['jour','numReg','incid_rea'])
        >>> d1.variables
        ['jour', 'numReg', 'incid_rea']

        """
        colnums=[]
        all_variables = self.variables
        data = []
        
        for i in range(len(all_variables)):
            if all_variables[i] in variables:
                colnums.append(i)
                
        for entry in self.donnees:
            liste = []
            for ele in sorted(colnums):
                liste.append(entry[ele])
            data.append(liste)    
        return Donnees(data,"csv")
                
        
    def aggregation_spatial(self,dep_numReg_Zone,liste_nums):
        """
        Ne garder que les éléments d'un jeu des données qui sont d'une liste des régions ou 
        départements données

        Parametres
        ----------
        dep_numReg_Zone : str: 'numReg' / 'dep' / 'Zone'
            Si vous voulez faire l'aggregation spatial sur les régions il faut entrer 'numreg'
            sinon, si vous voulez utiliser les départements il faut entrer 'dep'
            et pour les zones academiques il faut entrer 'Zone.
        liste_nums : iterable(str)
            Une liste des numéros des régions/départements que vous voulez garder
            ATTENTION: les numéros doit être du format str e.g ['01','02','03'].

        Returns
        -------
        None.
        
        Exemples
        --------
        >>> d1 = Jeux_donnees('C:/documents/file1.csv').importer()
        >>> d1.donnees
        [['jour', 'numReg', 'incid_rea'],['2000-08-29', '01', 44],['2000-08-29', '02', 6]]
        >>> d1.aggregation_spatial('reg',['02'])
        >>> d1.donnees
        [['jour', 'numReg', 'incid_rea'],['2000-08-29', '02', 6]]

        """
        data = tuple(self.donnees)
        data = list(data)
        if dep_numReg_Zone not in ['reg','numReg','dep','Zone','zone']:
            raise Exception('On ne peut que faire l\'aggregation spatial sur les variables \'numReg\', \'dep\' ou \'Zone\'')
        else:
            if dep_numReg_Zone == 'reg':
                dep_numReg_Zone = 'numReg'
            elif dep_numReg_Zone == 'zone':
                dep_numReg_Zone = 'Zone'
            colnum = None
            for var in range(len(self.variables)):
                if self.variables[var] == dep_numReg_Zone:
                    colnum = var
            if colnum == None:
                raise Exception('Variable ' + dep_numReg_Zone + ' non-trouvée')
            for entry in data[1:]:
                if entry[colnum] not in liste_nums:
                    data.remove(entry)
        return Donnees(data,"csv")            
                    
    def pendant_vacance(self,vacance,donnees_vacances):
        """
        Effacer les éléments d'un jeu des données qui ne sont pas pendant une
        vacance scolaire donnée.
        ATTENTION: si le date du fin de la vacance choisi n'est pas connu pour une zone academique,
            cette vacance est ignoré.
        
        Parametres
        ----------
        vacance : str
            le nom de la vacance.
        donnees_vacances : Donnees
            Un jeu des données d'un .json fichier qui contient les vacances et les zone scolaire
            des departements.

        Returns
        -------
        Donnees 
            Le nouveau jeu de données
        
        Exemples
        --------
        >>> d1 = Jeux_donnees('C:/documents/file1.csv').importer()
        >>> donnees_vacances = Jeux_donnees('C:/documents/file_vacances.json').importer
        >>> d1.pendant_vacance('Vacances de Printemps', donnees_vacances)
        
        """
        
        data_vacances = donnees_vacances.donnees
        data = tuple(self.donnees)
        data = list(data)
        variables = self.variables
        col_jour = None
        col_dep = None
        null_entry = False
        
        for i in range(len(variables)):
            if variables[i] == 'jour':
                col_jour = i
                print ('col_jour =' + str(col_jour))
            elif variables[i] == 'dep':
                col_dep = i
                print ('col_dep =' + str(col_dep))
        if col_jour == None:
            raise Exception('Variable \'jour\' non-trouvée')
        elif col_dep == None:
            raise Exception('Variable \'dep\' non-trouvée')
        for entry in data[1:]:
            remove = True
            date = entry[col_jour].split('-')
            for zones in data_vacances['Academie']:
                if entry[col_dep] == zones['Code_Dpt']:
                    zone = zones['Zone']
                    for vac in data_vacances['Calendrier']:
                        if vac['Zone'] == zone:
                            if vac['Description'] == vacance:
                                date_fin = vac['Fin']
                                if date_fin == None:
                                    date_fin = [date_fin]
                                else:
                                    date_fin = date_fin.split('-')
                                date_debut = vac['Debut'].split('-')
                                if date[0] in [date_debut[0],date_fin[0]]:
                                    if date_fin == [None]:
                                        null_entry = True
                                    else:
                                         if date_debut[0] == date_fin[0]: #les années sont les mêmes
                                             if date_debut[1] == date_fin[1]: #les mois sont le même
                                                 if int(date[2]) in range(int(date_debut[2]),int(date_fin[2])):
                                                     remove = False
                                             else: #mois differents
                                                 if int(date[1]) in range(int(date_debut[1])+1,int(date_fin[1])):
                                                     remove = False
                                                 elif int(date[1]) == int(date_debut[1]):
                                                     if int(date[2]) in range(int(date_debut[2]),32):
                                                         remove = False
                                                 elif int(date[1]) == int(date_fin[1]):
                                                     if int(date[2]) in range(0,int(date_debut[2])+1):
                                                         remove = False
                                         else: #années differents
                                             if int(date[0]) == int(date_debut[0]):
                                                 if int(date[1]) in range(int(date_debut[1])+1,13):
                                                     remove = False
                                                 elif int(date[1]) == int(date_debut[1]):
                                                     if int(date[2]) in range(int(date_debut[2]),32):
                                                         remove = False
                                             elif int(date[0]) == int(date_fin[0]):            
                                                 if int(date[1]) in range(0,int(date_fin[1])):
                                                     remove = False
                                                 elif int(date[1]) == int(date_fin[1]):
                                                     if int(date[2]) in range(0,int(date_debut[2])+1):
                                                         remove = False       
            if remove == True:
                data.remove(entry)                           
        if null_entry == True:
            print('Note: Au moins un entry pourrait avoir été enlevé parce que le date du fin de ce vacance n\'est pas connu' +
                  ' dans une zone academique')
        return Donnees(data,"csv")           
               
    def ajouter_zones_acad(self,donnees_zones):
        """
        Ajouter une nouvelle colonne au jeu de données Zone qui est les zones academiques
        ATTENTION: Il faut savoir la code du departement de vos données pour afficher les
                  zones academiques
        

        Parameters
        ----------
        donnees_zones : Donnees
            Un jeu des données d'un .json fichier qui contient les zones scolaires 
            des departements.

        Returns
        -------
        Donnees.
            Le nouveau jeu de données

        Exemples
        --------
        >>> d1 = Jeux_donnees('C:/documents/file1.csv').importer()
        >>> d1.donnees
        [['jour', 'dep', 'incid_rea'],['2000-08-29', '01', 44],['2000-08-29', '02', 6]]        
        >>> zones = Jeux_donnees('C:/documents/file_zones.json').importer()
        >>> d1.ajouter_zones_acad(zones)
        >>> d1.donnees
        [['jour', 'dep', 'incid_rea', 'Zone'],['2000-08-29', '02', 6, 'Zone A']]

        """
        data_zones = donnees_zones.donnees
        data = tuple(self.donnees)
        data = list(data)
        variables = tuple(self.variables)
        variables = list(variables)
        col_dep = None
        data[0].append('Zone')
        
        for i in range(len(variables)):
            if variables[i] == 'dep':
                col_dep = i
        if col_dep == None:
            raise Exception('Variable \'dep\' non-trouvée')
        for entry in data[1:]:
            for zones in data_zones['Academie']:
                if entry[col_dep] == zones['Code_Dpt']:
                    zone = zones['Zone']
                    entry.append(zone)
        return Donnees(data, "csv")
    def choisir_sexe(self,femme_homme):
        """
        Enlever les lignes des resultats par sexe (2 = femmes, 1 = hommes, 0 = hommes et femmes).
        Il faut entrer le sexe que l'on veut garder

        Parameters
        ----------
        femme_homme : int
            Le sexe qu'on veut garder (2 = Femmes, 1 = Hommes, 0 = Hommes et Femmes).

        Returns
        -------
        Donnees
            Le nouveau jeu de données

        """
        data = tuple(self.donnees)
        data = list(data)
        if femme_homme in ["femme","Femme","F","f","2"]:
            femme_homme = 2
        elif femme_homme in ["homme","Homme","H","h","1"]:
            femme_homme = 1
        elif femme_homme in ["H/F","h/f","tous","0"]:
            femme_homme = 0
        colnum = None
        for var in range(len(self.donnees[0])):
            if self.variables[var] == "sexe":
                colnum = var
        if colnum == None:
            raise Exception('Varaible \'sexe\' non-trouvée')
        i=1
        for entry in data[1:]:
            if entry[colnum] != femme_homme:
                data.remove(entry)
            print("ligne: " + str(i))
            i=i+1
        return Donnees(data,"csv")    
               
    def fenetrage_numpy(self,var_qual, dep_numReg_Zone,date_debut="00-00-0000",date_fin="99-99-99999"):
        """
        Retourner un array numpy des values d'un variable qualitative entre deux dates données pour chaque departement,
        region ou zone academique

        Parameters
        ----------
        var_qual : str
            Le variable qualitative l'on considère.
        dep_numReg_Zone : str : 'numReg' / 'dep' / 'Zone'
            Si vous voulez faire l'aggregation spatial sur les régions il faut entrer 'numreg'
            sinon, si vous voulez utiliser les départements il faut entrer 'dep'
            et pour les zones academiques il faut entrer 'Zone.
        date_debut : str, optional
            Le premier date de votre fenêtrage (inclus).
            Le date dait être du forme 'aaaa-mm-jj' e.g.'2020-08-01'.
            Si on ne donne pas un date début le programme suppose un 
            date de '0000-00-00'.
        date_fin : str, optional
            Le final date de votre fenêtrage (inclus).
            Le date dait être du forme 'aaaa-mm-jj' e.g.'2020-08-01'.
            Si on ne donne pas un date fin le programme suppose un 
            date de '999999-999-999'.

        Returns
        -------
        Donnees
            Le nouveau jeu de données.

        """
        data = self.fenetrage(date_debut,date_fin)
        data = data.selection_variables(["jour",dep_numReg_Zone ,var_qual])
        variables = data.variables
        data = data.donnees[1:]
        for i in range(len(variables)):
            if variables[i]== 'jour':
                col_jour = i
            elif variables[i] == dep_numReg_Zone:
                col_dep = i
            elif variables[i] == var_qual:
                col_var = i
        liste_jours = []
        liste_deps = []
        for element in data:
            jour = element[col_jour]
            dep = element[col_dep]
            if jour not in liste_jours:
                liste_jours.append(jour)
            if dep not in liste_deps:
                liste_deps.append(dep)
        array_numpy = []
        for dep in liste_deps:
            new_ligne = []
            for entry in data:
                for jour in liste_jours:
                    if entry[col_jour] == jour:
                        if entry[col_dep] == dep:
                            new_ligne.append(entry[col_var])
            array_numpy.append(new_ligne)                
        return np.array(array_numpy)
            
    def exporter(self,lien_fichier, delimiter = ";"):
        """
        Exporter un jeu de données comme une fichier csv

        Parameters
        ----------
        lien_fichier : str
            le lien du fichier qui contient ce jeu de données
                    il faut séparer ce lien avec les / par exemple 'C:/documents/nom_fichier.csv'
        delimiter : str, optional
            Le seperateur du fichier csv. Par défaut, cela soit ";".

        Returns
        -------
        None.
        
        Exemples
        --------
        data1.exporter("C:/Users/Documents/.csv")

        """
        if self.type_fichier == "json":
            raise Exception("On ne peut qu'exporter les données du format csv")
        with open(lien_fichier, 'w', newline='') as csvfile:
            covidwriter = csv.writer(csvfile, delimiter=delimiter,quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for ligne in self.donnees:
                covidwriter.writerow(ligne)
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
