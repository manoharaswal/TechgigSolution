def main():
    n = int(input().strip())
    power = list(map(int, input().strip().split()))
    out = 0
    for p in power:
        out += p
        
    print("{:.2f}".format(p))

main()
