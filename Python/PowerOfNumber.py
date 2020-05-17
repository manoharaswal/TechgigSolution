def main():
    num = input().strip()
    x,y,m = map(int, num.split())
    out = int((x**y) % m)
    print(out,end='')

main()
