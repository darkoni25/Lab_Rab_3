random_string = "Цей рядок використовується для прикладу операції зрізу"
substring = random_string[11:14] 
print(substring)
word = "програмування"
letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print("Однакові літери:")
for letter, count in letter_count.items():
    if count > 1:
        print(letter)
sentence = "Навчання — це процес, довгий та складний, але результативний, оскільки кожен крок наближає до нових знань і майстерності."
words = sentence.split()
count_n_words = 0
for word in words:
      if word.lower().startswith('н'):
          count_n_words += 1
print(f"Кількість слів, що починаються з літери 'н': {count_n_words}")