def count_words_in_string(input: str) -> int:
    count = len(input.split())
    return count


def main():
    with open("books/frankenstein.txt") as f:
        data = f.read()
        count = count_words_in_string(data)
        print(count)


if __name__ == "__main__":
    main()
