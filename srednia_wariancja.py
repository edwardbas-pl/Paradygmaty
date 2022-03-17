#!/bin/python3

def srednia_wariancja( lista ):
    avg =  0
    sum =  0
    wariancja = 0
    for x in lista:
        sum = sum + x
    avg = sum / len(lista)
    print(avg)
    sum = 0
    for w in lista:
        sum = sum + (( w - avg ) ** 2)  
    wariancja = sum / len(lista)

    return avg,wariancja
        

test = [ 3 , 3 , 3 , 3 ]

a,b = srednia_wariancja( test )

print( "srednia = " + str(a))
print( "wariancja = " + str(b))

