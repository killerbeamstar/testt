import random
from colorama import init, Fore
init()

def kerstboom(takken, ballen):
    aantalbal = 0
    breedte = 5
    plus =2
    tak1 = []
    for _ in range (0, takken):
        breedte = breedte + plus
        plus = plus + 2
    for _ in range(0 , breedte):
        tak1.append(" ")
    ster = int(breedte / 2)
    tak1[ster] = '*'
    print(Fore.YELLOW + ''.join(tak1))
    begin = ster - 1
    eind = ster + 1
    lengtetak = 3
    tak2 = tak1
    for test in range (0, takken):
        if (test == 0):
            lengtetak = lengtetak
        elif (test == 1):
            lengtetak = lengtetak + 2
        else:
            lengtetak = lengtetak + 1
        for _ in range ( 0, lengtetak ):
            tak2 = tak1
            if(begin < 0):
                break
            else:
                hoevaak = random.randint(0,5)
                for _ in range(0, hoevaak):
                    balsleutel = random.randint(begin, eind)
                    aantalbal = aantalbal + 1
                    tak1[balsleutel] = 'o'
                tak2[begin] = '*'
                tak2[eind] = '*'
                begin = begin - 1
                eind = eind + 1
            print(Fore.GREEN + ''.join(tak2))
        for _ in range(0 , 3):
            begin = begin + 1
            tak2[begin] = ' '
            eind = eind - 1
            tak1[eind] = ' '
    for _ in range(0 , 3):
        print(Fore.RED + " "*int(breedte / 2 - 2), "***")

def main():
    takken = int(input("Aantal takken voor de kerstboom: "))
    ballen = int(input("aantal kerstballen in de kerstboom: "))
    kerstboom(takken, ballen)
main()
