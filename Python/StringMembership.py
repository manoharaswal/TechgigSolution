def main():
    string = input().strip()
    ch = input().strip()
    if (string.find(ch) != -1):
        print("True", end='')
    else:
        print("False", end='')

main()
