def main():
    n = int(input().strip())
    name = input().strip()
    ls = list(map(int, name.split()))

    for i in range(len(ls)):
        if i < len(ls) - 1:
            print(ls[ls[i] - 1])
        else:
            print(ls[ls[i] - 1], end='')

main()
