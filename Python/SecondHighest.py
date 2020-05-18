def main():
    dict = {}
    out = []
    n = int(input().strip())
    for i in range(n):
        name = input().strip()
        height = int(input().strip())
        dict[name] = height
    
    sortedHeight = sorted(dict.values(), reverse=True)
    maxValue = sortedHeight[0]
    maxValue2 = 0
    
    for i in sortedHeight:
        if i != maxValue:
            maxValue2 = i
            break
        
    for key,val in dict.items():
        if val == maxValue2:
            out.append(key)

    out.sort()
    for i in range(len(out)):
        if i < len(out) - 1:
            print(out[i])
        else:
            print(out[i], end='')
                                                                                                                                                                        main()
