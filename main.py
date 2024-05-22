import string
import random

def occurrence_table(words):
    occurrence_dict = {}
    for word in words:
        for i in range(len(word) - 1):
            current_letter = word[i]
            next_letter = word[i + 1]
            if current_letter not in occurrence_dict:
                occurrence_dict[current_letter] = {}
            if next_letter not in occurrence_dict[current_letter]:
                occurrence_dict[current_letter][next_letter] = 1
            else:
                occurrence_dict[current_letter][next_letter] += 1
    return occurrence_dict

def build_probability_table(occurrence_dict):
    probability_table = {}
    for current_letter, next_letters in occurrence_dict.items():
        total_occurrences = sum(next_letters.values())
        probability_table[current_letter] = {next_letter: count / total_occurrences
                                             for next_letter, count in next_letters.items()}
    return probability_table

def generate_word(probability_table, max_length=10):
    word = random.choice(list(probability_table.keys()))
    while len(word) < max_length:
        current_letter = word[-1]
        if current_letter in probability_table:
            next_letter = random.choices(
                list(probability_table[current_letter].keys()),
                list(probability_table[current_letter].values())
            )[0]
            word += next_letter
        else:
            break
    return word

# Lecture du fichier mot.txt
with open('mot.txt', 'r', encoding='utf-8') as file:
    words = file.read().splitlines()

occurrence_dict = occurrence_table(words)
probability_table = build_probability_table(occurrence_dict)

# Génération de plusieurs mots pour observer la diversité
generated_words = [generate_word(probability_table) for _ in range(4)]
print("Generated words:", generated_words)
