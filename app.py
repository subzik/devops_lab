
print("press ENTER & insert word 'amsterdam' or 'alaska'")


def word1(n):
    r1 = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')
    r2 = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')
    r3 = ('z', 'x', 'c', 'b', 'n', 'm')

    words = str(input("please insert the word: "))
    words = set(words)
    if words.intersection(r1) and words.intersection(r2)\
            or words.intersection(r1) and words.intersection(r3):
        return False
    elif words.intersection(r2) and words.intersection(r3):
        return False
    else:
        return True


if __name__ == "__main__":
    w1 = str(input())
    print(word1(w1))
