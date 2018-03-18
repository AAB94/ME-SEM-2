with open("month.txt") as f:
    for s in f.readline().split(','):
        if len(s) != 1:
            print(s," -> " , len(s))
