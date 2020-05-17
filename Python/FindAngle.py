import math

def main():
    AB = int(input().strip())
    BC = int(input().strip())
    print(90 - int(round(math.degrees(math.atan(AB/BC)))), end='')

 main()
