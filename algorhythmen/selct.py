def selectionSort( liste ):
   Ende = len( liste )
   for Anfang in range( Ende - 1 ):
       Bestes = Anfang
       for SZeiger in range( Anfang , Ende ):
           if liste[SZeiger] < liste[Bestes] :
               Bestes = SZeiger

       if Bestes != Anfang :
           vertausche(liste,Anfang, Bestes)

   return liste



def vertausche(liste,i,j):
   x = liste[i]
   liste[i] = liste[j]
   liste[j] = x

DieListe = [7,2,9]
print(selectionSort(DieListe))
