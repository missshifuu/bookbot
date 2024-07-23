def main():
    book_path = "books/frankenstein.txt"
    text = getbooktext(book_path)
    countWord = countWords(text)
    
    distCharCount = countChar(text)

    sortNum = chars_dict_to_sorted_list(distCharCount)

    print(f"--- Begin report of {book_path} ---")
    print(f"{countWord} words found in the document")
    print()

    for item in sortNum:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def getbooktext(path):
    with open(path) as f:
        return f.read()

def countWords(text):
    words = text.split()
    print(words)
    return len(words)

def countChar(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




main()