def main():
    ls = []
    minRate = 11
    n = int(input().strip())
    for i in range(n):
        name = input().strip()
        rate = int(input().strip())
        if minRate > rate:
            if len(ls) == 0:
                ls.append(name)
            else:
                ls.insert(len(ls) - 1, name)
            minRate = rate
        elif minRate == rate:
            ls.append(name)
        
    ls.sort()
    for i in range(len(ls)):
        print(ls[i])
        
main()
