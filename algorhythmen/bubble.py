def bubbleSort( liste ):
   Anfang = 0
   Ende = len( liste )
   Ende -= 1
   while Ende - Anfang >= 1 :
      SZeiger = Anfang
      while SZeiger != Ende :
         if liste[SZeiger] > liste[SZeiger+1] :
            vertausche(liste, SZeiger, SZeiger+1)

         SZeiger += 1

      Ende -= 1

   return liste

def vertausche(liste,i,j):
   x = liste[i]
   liste[i] = liste[j]
   liste[j] = x

DieListe = [1,2,3,5,4]


print(bubbleSort(DieListe))
