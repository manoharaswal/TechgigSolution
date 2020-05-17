def main():
    ls = []
    n = int(input().strip())
    for i in range(n):
        data = input().strip().split()
        ls.append((int(data[1]) + int(data[2]) + int(data[3])) / 3)

    print("{:.2f}".format(min(ls)))

main()
