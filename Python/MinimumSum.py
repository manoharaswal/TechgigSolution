def main():
    List = list(map(int, input().strip().split()))
    List.sort()
    print(List[0] + List[1])

main()
