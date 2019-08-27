##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

# resumen para el resto de puntos
#primero se selecciona sola primer columna y se ordena 
datos2 = [i[2] for i in datos]
datos3 = set(datos2)
#Extraer los meses sinconvertir a fecha
datos4 = sorted([i[5:7] for i in datos2])
#ordenarlos
datos5 = set(datos4)
# se genera lal lista yvariables
lista1 = []
for i in datos5:
  p = [i]
  d = 0
  #si se obtienen los mismos valores entonces
  for x in datos4:
    if x == i:
      d = d+1
  p= p+[d]
  # se ordenan
  lista1 = sorted(lista1+[p])
  # se imprime cada elemento
for ite in lista1:
  res = str(ite[0])+ ","+ str(ite[1])
  print(res)
