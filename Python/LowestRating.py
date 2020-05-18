def main():
    n = int(input().strip())
    name = []
    rate = []
    for i in range(n):
        name.append(input().strip())
        rate.append(int(input().strip()))
                                            
    minRate = min(rate)
                                                    
    out = []
    for i in range(len(rate)):
    if rate[i] == minRate:
        out.append(name[i])

    out.sort()
    for i in out:
        print(i)
    print(end='\n')

main()
