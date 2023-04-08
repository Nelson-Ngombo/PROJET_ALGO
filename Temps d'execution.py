
from reseau import * 
import time

start = time.time()


cdr1 = cdr("algo.txt")
cdr1._open()
facture1 = facture(cdr1.resultat)
facture1.definition()


statistique1 = statistique(cdr1.resultat)
statistique1.stat()



print(time.time() - start)

# temps d'éxecution : 1 ms
# La complexité est de O(n²) 
