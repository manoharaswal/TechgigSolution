def main():
    n = int(input().strip())
    List = list(map(int, input().strip().split()))
    out = 0
    for num in List:
        if num % 2 == 0:
            out += num
            
    print(out)

main()
