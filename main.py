def count_words_in_string(input: str) -> int:
    count = len(input.split())
    return count


def per_character_count(input: str) -> dict[str, int]:
    input = input.lower()
    tracker: dict[str, int] = {}

    for char in input:
        if char in tracker:
            tracker[char] += 1
        else:
            tracker[char] = 1

    return tracker


def main():
    with open("books/frankenstein.txt") as f:
        data = f.read()
        count = count_words_in_string(data)
        print(count)
        print(per_character_count(data))


if __name__ == "__main__":
    main()
