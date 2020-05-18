def main():
    In = list(map(int, input().strip().split()))
    In.sort(reverse=True)
    print(In[0] + In[1])

main()
