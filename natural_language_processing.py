import nltk

# Download necessary NLTK data
nltk.download('punkt')

# Function to tokenize sentences
def tokenize(text):
    return nltk.word_tokenize(text)