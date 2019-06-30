
#print("press ENTER & insert word 'amsterdam' or 'alaska'")


def word1(words):
    r1 = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')
    r2 = ('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')
    r3 = ('z', 'x', 'c', 'b', 'n', 'm')

    #words = str(input("please, insert the word: "))
    b = str(words)

    n = set(words)
    if n.intersection(r1) and n.intersection(r2) or n.intersection(r1) and n.intersection(r3):
        return False
    elif n.intersection(r2) and n.intersection(r3):
        return False
    else:
        return True


if __name__ == "__main__":
    words = input("Input word: ")
    print(word1(words))

