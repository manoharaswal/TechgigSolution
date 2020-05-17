def main():
    string = input().strip()
    string = string.replace(" ","")
    
    cap = min(string)
    string = string.lower()
    low = min(string)
    
    if low < cap.lower():
        print(low, end='')
    else:
        print(cap, end='')

main()
