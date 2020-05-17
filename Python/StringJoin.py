def main():
    ls = []
    cat = input().strip()
    while True:
        try:
            ch = input().strip()
        except EOFError:
            break
        ls.append(ch)
    print(cat.join(ls),end='')

main()
