"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730485068"


def input_word() -> str:
    """prompting for input word"""
    word = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters. ")
        # return word
        exit()


def input_letter() -> str:
    """prompting for input character"""
    char = input("Enter a single character: ")
    if len(char) == 1:
        return char
    else:
        print("Error: Character must be a single character. ")
        # return char
        exit()


def contains_char(word: str, letter: str) -> None:
    """contain char"""
    print("Searching for " + letter + " in " + word)
    char_count = 0
    if letter == word[0]:
        print(letter + " found at index " + str(0))
        char_count += 1
    if letter == word[1]:
        print(letter + " found at index " + str(1))
        char_count += 1
    if letter == word[2]:
        print(letter + " found at index " + str(2))
        char_count += 1
    if letter == word[3]:
        print(letter + " found at index " + str(3))
        char_count += 1
    if letter == word[4]:
        print(letter + " found at index " + str(4))
        char_count += 1
    print(str(char_count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """main func"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()

# input_word()
# input_letter()
# contains_char(word="kitty", letter="z")
# contains_char(word=input_word(), letter=input_letter())
