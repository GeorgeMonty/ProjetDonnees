
import jeux_donnees as jd

data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data1.csv').importer()
data2= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data2.csv').importer()
data3= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data3.csv').importer()
data4= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data4.csv').importer()
data5= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/data5.csv').importer()
holidays = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/test2.json').importer()

testing = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees/VacancesScolaires.json').importer()

test = data1.selection_variables(["jour","numReg","incid_rea"])
test.exporter("C:/Users/georg/OneDrive/Documents/Projet données/code/test_export.csv")

imported = jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/test_export.csv').importer()

data1.variables
data2.variables
data3.variables
data4.variables
data5.variables

test = data4.aggregation_spatial('dep', ['36','01'])
data2.aggregation_spatial('reg', ['01','28'])

x=data1.selection_variables(['jour','incid_rea'])

jointure = data4.jointure(data5)

holidays = holidays.donnees['Calendrier']

for entry in holidays:
    if entry['Description'] != None:
        holidays.remove(entry)
        

test = data3.pendant_vacance('Vacances de NoÃ«l',holidays)



data3.fenetrage("2019-01-01","2024-12-31")
data4.fenetrage("2020-03-19","2020-03-26")

test = data3.jointure(data4)

data = tuple(test.donnees)
data = list(data)
for entry in data[1:]:
    if entry[2] != "84":
        data.remove(entry)
        
test = data3.ajouter_zones_acad(holidays)

data3.choisir_sexe(2)
data3 = data3.choisir_sexe('femme')

test = data3.fenetrage_numpy('hosp', 'dep','2020-08-29','2020-08-31')
