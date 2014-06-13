def GemStones(N):
    gems = set(raw_input())
    for i in range(N-1):
        rock = set(raw_input())
        gems = gems.intersection(rock)
    return len(gems)

if __name__=="__main__":
    print GemStones(input())
