def main():
    n = int(input().strip())
    marks = dict.fromkeys(input().strip().split())
    marks = list(marks)
    marks.sort(reverse=True)
    print(marks[1])

main()
