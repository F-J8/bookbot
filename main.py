def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(get_nr_words(text))
    print(get_nr_tchar(text))
    print(sort_dictionary(get_nr_tchar(text)))
    


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_nr_words(text):
    words = text.split()
    #print(words)
    return len(words)

def get_nr_tchar(text):
    dict_lowered = {}
    text_lower = text.lower()
    #alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
    chars=[]
    for i in text_lower:
        if i in chars:
            dict_lowered[i]+=1
        else:
            chars.append(i)
            dict_lowered[i]=1
    
    return dict_lowered

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    #dictionary.sort()
    list_dictionary = []

    for i in dictionary:
        if i.isalpha():
            list_dictionary.append({"character": i , "num" : dictionary.get(i)})

    list_dictionary.sort(reverse=True, key=sort_on)

    return list_dictionary



main()



