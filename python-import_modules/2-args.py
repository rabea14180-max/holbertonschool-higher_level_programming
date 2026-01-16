#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    else:
        word = "argument" if n == 1 else "arguments"
        print("{} {}:".format(n, word))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
