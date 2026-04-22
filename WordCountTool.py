text = input("Enter the text:")

print(text)
print(text.split())

print("Total words : ", len(text.split()))

print("Total characters in text : ", len(text))

lines = text.split('\n')
print("Total lines:", len(lines))

# Word frequency (case-insensitive and ignoring basic punctuation)
clean_text = text.lower()
for char in ".,!?;:":
    clean_text = clean_text.replace(char, "")

words_clean = clean_text.split()
word_count = {}
for word in words_clean:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print word frequencies
print("\nWord Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")