def main():
    x,y,M = map(int, input().strip().split())
    print((x ** y) % M)

main()
