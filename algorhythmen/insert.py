def hallo(liste):
   Ende = len( liste )
   for i in range(1,Ende):

       SZeiger = liste[i]
       while i > 0 and liste[i-1] > SZeiger:
            liste[i] = liste[i-1]
            i = i-1
            liste[i] = SZeiger


   return liste


DieListe = [5,2,1]
print(hallo(DieListe))
