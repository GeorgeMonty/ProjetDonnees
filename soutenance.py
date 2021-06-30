import jeux_donnees as jd
import statistique as st
import kmeans as km
import graphique as gr
import table as tb

data1= jd.Jeux_donnees('C:/Users/georg/OneDrive/Documents/GitHub/ProjetDonnees/Bases_de_donnees'+
                       '/covid-hospit-incid-reg-2021-03-03-17h20.csv').importer()
data1.variables

data1.donnees[:5]


data2= data1.selection_variables(['jour','nomReg','incid_rea'])
data2.donnees[:5]

data3 = data1.aggregation_spatial('numReg', ['53','11'])
data3.donnees[:5]

data4 = data3.fenetrage("2020-08-29","2020-12-31")
data4.donnees[:5]
data4.donnees[-4:]

data4.exporter('C:/Users/georg/OneDrive/Documents/data4_csv')

data5 = data1.fenetrage_numpy('incid_rea', 'numReg','2020-08-29','2020-08-31')
data5[:5]
