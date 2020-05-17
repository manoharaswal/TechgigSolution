def main():
    name = []
    Q = int(input().strip())
    for i in range(0, Q):
        name.append(input().strip())
        
    name.sort()
    
    for i in name:
        print(i)

main()
