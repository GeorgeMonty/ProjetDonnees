import csv
import json
import donnees as dn

class Jeux_donnees:
    
    
    def __init__(self,lien_fichier):
        self.lien_fichier = lien_fichier
        self.__type_fichier = lien_fichier.split('.')[-1]
        
        
    def importer(self):
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
                if variables[i] == 'jour':
                    pass
                elif variables[i] == 'nomReg':
                    pass
                elif variables[i] == 'dep':
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
        
        
