def is_heterogram(s):
    s = s.replace(' ', "").lower()
    return len(set(s)) == len(s)


def is_isogram(s):
    s = [c for c in s.lower() if c.isalpha()]
    return len(set(s)) == len(s)


def is_pangram(s):
    s = set([c for c in s.lower() if c.isalpha()])
    return len(s) == 26


def main():
    test_cases = [("subdermatoglyphic", "The quick brown fox jumps over the lazy dog"), ("apple", "Hello, World")]

    for s1, s2 in test_cases:
        print(f"Testing with \"{s1}\" and \"{s2}\"")
        print(f"is_heterogram(\"{s1}\") = {is_heterogram(s1)}")
        print(f"is_isogram(\"{s1}\") = {is_isogram(s1)}")
        print(f"is_pangram(\"{s2}\") = {is_pangram(s2)}")
        print()


if __name__ == "__main__":
    main()

