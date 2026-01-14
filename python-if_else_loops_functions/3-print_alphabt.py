#!/usr/bin/python3
print("".join(chr(i) for i in range(97, 113) if i != 101) + "".join(chr(i)
      for i in range(114, 123)), end="")
