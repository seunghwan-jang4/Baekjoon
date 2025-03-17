while True:
    try:
        line = input()
        if line == "":
            break
        A, B = map(int, line.split())
        print(A + B)
    except EOFError:
        break