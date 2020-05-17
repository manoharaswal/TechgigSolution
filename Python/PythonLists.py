def main():
    ls = []
    Q = int(input().strip())
    for i in range(0,Q):
        ty = input()
        if not ty.find('1'):
            ls.append(ty[ty.index(" ") + 1:])
        elif not ty.find('2'):
            if i < Q - 1:
                print(ls)
            else:
                print(ls, end = '')
                
main()
