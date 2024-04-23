import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('webtext')

# Load English stopwords
english_stops = set(stopwords.words("english"))

# Read text from file
with open('random_paragraphs.txt', 'r') as file:
    text = file.read()

# Tokenize the text into words
words = word_tokenize(text)

# Remove stop words
filtered_words = [word for word in words if word.lower() not in english_stops]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Print word frequencies
for word, freq in word_freq.items():
    print(f"{word}: {freq}")



