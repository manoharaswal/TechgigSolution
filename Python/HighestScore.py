def main():
    ls = []
    n = int(input().strip())
    for i in range(0,n):
        ls.append(int(input().strip()))
        
    print(max(ls))

main()
