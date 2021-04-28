#               R E K U R S I O N

# - Prinzip: "Teile und Herrsche"
# - Abbruchbedingung
# - Eine Berechnungsvorschrift (Formel)

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nErgebnisse:")
tri_recursion(6)

# Als Rekursion wird ein prinzipiell unendlicher Vorgang, der sich selbst als Teil enthält oder mithilfe von sich selbst definierbar ist,
# bezeichnet. Üblicherweise sind rekursive Vorgänge relativ kurz beschreibbar, bzw. können durch eine relativ kurze Anweisung ausgelöst werden.

## Beispiel:

def summe(zahl):
    if zahl == 0:
        return 0
    else:
        return zahl + summe(zahl-1)
