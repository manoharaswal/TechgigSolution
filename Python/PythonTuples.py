def main():
    n = int(input().strip())
    el = input().strip()
    tup = tuple(map(int,el.split()))
    x = int(input().strip())
    out = 0
    for i in range(n):
        if tup[i] == x:
            out += 1
            
    print(out, end='')

main()
