import statistics

def main():
    n = int(input().strip())
    List = list(map(int, input().strip().split()))
    print("{:.3f}".format(statistics.mean(List))) 
                  
main()
