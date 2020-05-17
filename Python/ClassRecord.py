def main():
    ls = [0,0,0,0,0]
    n = int(input().strip())
    for i in range(n):
        string = input().strip()
        data = string.split()
        for j in range(5):
            ls[j] = ls[j] + int(data[j + 1])
                                                                
    print("{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(ls[0]/n, ls[1]/n, ls[2]/n, ls[3]/n, ls[4]/n), end='')

main()
