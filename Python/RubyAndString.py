def checkCharfreq(string):
    freq = {}
    for c in string:
        freq[c] = string.count(c)
    return freq

def main():
    string = input().strip()
    out = checkCharfreq(string)
    l = 0
    for key,val in out.items():
        if l < len(out) - 1:
            print("({}, '{}') ".format(val,key), end='')
        else:
            print("({}, '{}') ".format(val,key))
        l += 1

main()
