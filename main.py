def characterreport(dict):
    def sort_on(dict):
        return dict["num"]

    dictlist = []
    # First, convert the dictionary to a list of dictionaries, filtering for letters only
    for char, count in dict.items():
        if char.isalpha():
            new_dict = {"char": char, "num": count}
            dictlist.append (new_dict)
    # Then, sort the list of dictionaries by the count
    dictlist.sort(reverse=True, key=sort_on)
    # Then, for each dictionary in the list, print the character and the count
    for dict in dictlist:
        print(f"The '{dict["char"]}' character was found '{dict["num"]}' times")
    return None

def countcharacters(text):
    characterbook = {}
    characters = text.lower()
    for character in characters:
        if character in characterbook:
             characterbook[character] += 1
        else:
            characterbook[character] = 1
    return characterbook

def countwords(text):
    words = text.split()
    return len(words)

def get_book_text(book):
    with open(book) as f:
        return f.read()

def main():
    bookpath = "books/frankenstein.txt"
    text = get_book_text(bookpath)
    wordcount = countwords(text)
    charactercount = countcharacters(text)
    print(f"--- Begin report of {bookpath} ---")
    print("")
    print(f"{wordcount} words found in the document")
    characterreport(charactercount)
    print("--- End report ---")

main()