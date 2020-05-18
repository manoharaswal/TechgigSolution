def main():
    out = ""
    while True:
        try:
            string = input().strip()
        except EOFError:
            break;
        out = out + string 
    print(out, end='')

main()
