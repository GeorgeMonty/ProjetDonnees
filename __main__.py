
import jeux_donnees as jd

data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data1.csv').importer()
data2= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data2.csv').importer()
data3= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data3.csv').importer()
data4= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data4.csv').importer()
data5= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data5.csv').importer()


data1.selection_variables(['numReg','jour','incid_rea'])

jointure = data4.jointure(data5)

