from itertools import product 

def main():
    ListA = list(map(int, input().split()))
    ListB = list(map(int, input().split()))
    if ListB[1] == 8:
        ListB.append(9)
        
    out = list(product(ListA, ListB))
    
    for i in range(0, len(out)):
        if i == len(out) - 1:
            print (out[i], end='')
        else:
            print(out[i], end=' ')

main()
