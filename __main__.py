
import jeux_donnees as jd

data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data1.csv').importer()
data2= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data2.csv').importer()
data3= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data3.csv').importer()
data4= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data4.csv').importer()
data5= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data5.csv').importer()
holidays = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/test2.json').importer()


data1.donnees[0]
data2.donnees[0]
data3.donnees[0]
data4.donnees[0]
data5.donnees[0]

data4.aggregation_spatial('depp', ['36','01'])
data2.aggregation_spatial('reg', ['01','28'])

data1.selection_variables(['jour','incid_rea'])

jointure = data4.jointure(data5)

holidays = holidays.donnees['Calendrier']

for entry in holidays:
    if entry['Description'] != None:
        holidays.remove(entry)
        

data3.pendant_vacance('Vacances de NoÃ«l',holidays)



data1.fenetrage("2020-03-19","2020-03-26")
data2.fenetrage("2020-03-19","2020-03-26")

test = data1.jointure(data2)

data = tuple(test.donnees)
data = list(data)
for entry in data[1:]:
    if entry[2] != "84":
        data.remove(entry)