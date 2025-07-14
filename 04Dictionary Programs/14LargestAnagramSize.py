def largest_anagram_subset_size(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    max_count = max([len(val) for val in anagram_dict.values()])
    return max_count

words = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']
print(largest_anagram_subset_size(words))