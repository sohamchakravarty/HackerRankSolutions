if __name__ == '__main__':
    for _ in range(input()):
        N = input()
        
        if N % 2 == 0:
            print(3 if (N // 2) % 2 == 0 else 4)
        else:
            print(2)