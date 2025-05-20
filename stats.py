


def get_num_words(content):
    num_words = len(content.split())
    # print(f"{num_words} words found in the document")
    return num_words


def get_num_chars(content):
    result = {}
    for char in content:
        char = char.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result




def format_content(content, total_words):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    content = get_num_chars(content)
    sorted_content = dict(sorted(content.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_content.items():
        print(f"{key}: {value}")



