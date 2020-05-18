def main():
    n = int(input().strip())
    tup = tuple(map(int,input().strip().split()))
    print(hash(tup))

main()
