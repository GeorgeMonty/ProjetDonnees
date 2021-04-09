import csv
import json

class Jeux_donnees:
    
    
    def __init__(self,lien_fichier):
        self.lien_fichier = lien_fichier
        self.__type_fichier = lien_fichier.split('.')[-1]
        
        
    def importer(self):
        path = self.lien_fichier.split('\\')
        filename = path[-1]
        
        folder=''
        for i in range(len(path)-1):
            folder = folder + path[i] + '\\'
            
        if self.__type_fichier == 'csv':
            data = []
            
            with open(folder + filename, encoding='ISO-8859-1') as csvfile :
                covidreader = csv.reader(csvfile, delimiter=';')
                for row in covidreader :
                    data.append(row)
            return data
        
        elif self.__type_fichier == 'json':
            with open(folder + filename) as json_file :
                data = json.load(json_file)
            return data
        
        else:
            raise Exception("Type de fichier inconnu")
        
        
    def jointure(self,jeux2,variable_jointure):
        
        if self.__type_fichier == 'csv':
            data1 = self.importer()
            data2 = jeux2.importer()
            variables1 = data1[0]
            variables2 = data2[0]
            new_variables = variables1
            
            #creer une liste des nouvelles variables du jeu de données
            for i in variables2:
                is_new = True
                for j in new_variables:
                    if i == j:
                        is_new = False
                if is_new:
                    new_variables.append(i)
            ######################################################################################################
            colnum1 = None
            for col in range(len(variables1)):
                if variables1[col] == variable_jointure:
                    colnum1 = col
                    break
            if colnum1 == None:
                raise Exception("Le variable de jointure n'est pas présent dans un/tout les jeux de données")
                  
            
        elif self.__type_fichier == 'json':
            return ("json files not coded yet")
        
        else:
            raise Exception("Type de fichier inconnu")
        

