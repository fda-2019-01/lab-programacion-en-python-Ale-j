##
## Imprima la suma de la segunda columna.
## 
import glob as gl
archivo = gl.glob("data.csv")
data = open("data.csv", 'rt').readlines()
data = [line[:-1] for line in data]
data = [line.replace("\t", ",") for line in data]
data = [line.split(',') for line in data]
data1 = [i[1] for i in data]
b = 0
for i in data1:
  b = b + int(i)
print(b)
