# -*- coding: utf-8 -*-
file  =open("capitulos.txt","a+");
tofile=open("capitulos_orden.txt","a+");

for line in reversed(file.readlines()):
   tofile.write(line)
file.close()
tofile.close()

