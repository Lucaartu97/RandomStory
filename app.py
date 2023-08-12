import random
quando = ['Alcuni anni fa', 'Ieri', 'La scorsa notte', 'Tanto tempo fa','Il 20 Gennaio']
chi = ['un coniglio', 'un elefante', 'un topo', 'una tartaruga','un gatto']
nome = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
città = ['Barcelona','India', 'Germany', 'Venezia', 'Inghilterra']
dove = ['cinema', 'università','seminario', 'scuola', 'lavanderia']
accaduto = ['farsi degli amici','mangiare hamburgher', 'cercare la chiave segreta', 'risolvere un mistero', 'scrivere un libro']
print(random.choice(quando) + ', ' + random.choice(chi) + ' di nome ' + random.choice(nome) + ' voleva andare in una nuova città, ' + random.choice(città) + ', partì e andò in una ' + random.choice(dove) + ' per ' + random.choice(accaduto))