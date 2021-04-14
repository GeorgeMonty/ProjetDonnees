# -*- coding: utf-8 -*-
import donnees as dn

test = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/donnees-hospitalieres-etablissements-covid19-2021-03-03-17h03.csv')
test3 = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/covid-hospit-incid-reg-2021-03-03-17h20.csv')

x=test.jointure(test3)




import donnees as dn
small = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/Book1.csv')
small2= dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/Book2.csv')

x=small.jointure(small2)
x
small.donnees[0]
small2.donnees[0]

import donnees as dn
essai = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/donnees-hospitalieres-classe-age-covid19-2021-03-03-17h03.csv')
essai2 = dn.Donnees('C:/Users/georg/OneDrive/Documents/Projet données/code/covid-hospit-incid-reg-2021-03-03-17h20.csv')

jointure = essai.jointure(essai2)
