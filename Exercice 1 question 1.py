mytable = [54,64,28,96,16]
valeurMin = mytable[0]
sauvegarde=0



sauvegarde=mytable[0] #sauvegarde la premiere valeur 
mytable[0]= mytable[1] # mets la deuxieme valeur a la place de la premiere 
mytable[1]=sauvegarde # mets la valeur sauvegarder ( la premiere ) a la place de la deuxieme 
print:mytable

input()