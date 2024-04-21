def count_words_in_string(input: str) -> int:
    count = len(input.split())
    return count


def per_character_count(input: str) -> dict[str, int]:
    input = input.lower()
    tracker: dict[str, int] = {}

    for char in input:
        if char.isalpha():
            if char in tracker:
                tracker[char] += 1
            else:
                tracker[char] = 1

    return tracker


def sort_fn(dictionary: dict[str, int]) -> int:
    for value in dictionary.values():
        return value


def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        data = f.read()
        words_count = count_words_in_string(data)
        chars_count = per_character_count(data)

        print(f"*** Begin report for {book} ***")
        print(f"{words_count} words found in the document")

        sorter = []

        for entry, count in chars_count.items():
            sorter.append({entry: count})

        sorter.sort(reverse=True, key=sort_fn)
        for item in sorter:
            for key, val in item.items():
                print(f"'{key}' character was found {val} times")

        print(f"*** End report for {book} ***")


if __name__ == "__main__":
    main()
