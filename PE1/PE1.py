def count_unique_words(statement):
    exclude_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}
    
    cleaned_statement = "".join(char if char.isalnum() or char.isspace() else " " for char in statement)
    words = cleaned_statement.split()
    
    word_frequencies = {}
    
    for word in words:
        normalized_word = word.lower()
        if normalized_word not in exclude_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    
    total_count = sum(word_frequencies.values())
    
    lowercase_words = sorted((w, c) for w, c in word_frequencies.items() if w.islower())
    uppercase_words = sorted((w, c) for w, c in word_frequencies.items() if not w.islower())
    
    for word, count in lowercase_words:
        print(f"{word.ljust(10)} - {count}")
    for word, count in uppercase_words:
        print(f"{word.ljust(10)} - {count}")
    
    print(f"\nTotal words filtered: {total_count}")

input_text = input("Enter a string statement:\n")
count_unique_words(input_text)


