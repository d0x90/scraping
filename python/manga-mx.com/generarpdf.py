import os
import sys
import commands

#path = sys.argv[1]

if len(sys.argv) > 1:
    path = sys.argv[1]
    for root, subdirs, files in os.walk(path):
        for file in os.listdir(root):
            filePath = os.path.join(root, file)
	    #print filePath
            if os.path.isdir(filePath) and file != 'logs':
		#Restandole 8 del path "nanatsu/"
		    pdfname = filePath[-(len(filePath)-8):]
		    print "cd \""+filePath+"\" && convert `ls -1v *.(jpg|png)` \""+pdfname+".pdf\""		 
		    os.system("cd \""+filePath+"\" && convert `ls -1v` \""+pdfname+".pdf\"")
		    print "PDF CREADO: \""+pdfname+"\""
		    os.system("cd \""+filePath+"\" && mv *.pdf \"PDF\"")
else:
    print 'Pase como parametro el nombre de la carpeta donde estan todos los mangas'
