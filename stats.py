def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    counts = {}

    for char in text: 
        if char in counts: 
            counts[char] += 1
        else: 
            counts[char] = 1 
    
    return counts

def sort_on(item):
    return item["num"]

def sort_char_counts(counts):
    sorted_list = []

    for char, count in counts.items():
        if char.isalpha():
            sorted_list.append ({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
