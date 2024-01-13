def main():
    text = read_file("books/frankenstein.txt")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words(text)} words found in the document\n")
    chars = [(char, count)
             for (char, count) in chars_dict(text).items()
             if char.isalpha()]
    chars.sort(key=lambda char: char[1], reverse=True)
    for (char, count) in chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


def read_file(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()


def num_words(text: str) -> int:
    return len(text.split())


def chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars.keys():
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


if __name__ == "__main__":
    main()
