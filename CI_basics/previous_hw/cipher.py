import sys

cipher = sys.argv[1]


def decode(cipher):
    if not cipher:
        return ""
    i = 0
    res = ''
    while i < len(cipher):
        if cipher[i:i+2] == "..":
            res = res[:-1]
            i += 2
        elif cipher[i] == ".":
            i += 1
        else:
            res += cipher[i]
            i += 1
    return res

if __name__ == "__main__":
    print(decode(cipher))
