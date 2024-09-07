def main():
    path_to_file = "books/frankenstein.txt"
    contents = get_book_contents(path_to_file)
    words_count = get_words_count(contents)
    characters = count_characters(contents)

    print_report(path_to_file, words_count, characters)

def get_book_contents(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_words_count(contents):
    words = contents.split()
    return len(words)

def count_characters(contents):
    characters_dict = {}

    for c in contents:
        lowered_c = c.lower()
        if lowered_c not in characters_dict:
            characters_dict[lowered_c] = 1
        else:
            characters_dict[lowered_c] += 1

    return characters_dict

def print_report(path_to_file, words_count, characters_dict):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_count} words found in the document\n")

    rd = convert_dict_to_list(characters_dict)
    rd.sort(reverse=True, key=sort_on)

    for item in rd:
        char = item["char"]

        if char.isalpha():
            count = item["num"]
            print(f"The '{char}' character was found {count} times")

    print(f"--- End report of {path_to_file} ---")

def convert_dict_to_list(dict):
    result_list = []

    for k in dict:
        d = {
                "char": k,
                "num" : dict[k]
        }

        result_list.append(d)

    return result_list

def sort_on(dict):
    return dict["num"]

main()

