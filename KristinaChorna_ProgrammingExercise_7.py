# Kristina Chorna
# Programming Exercise 7
# The goal of this program is to prompt the user to enter a paragraph and display the individual sentences and their count.

import re


def split_into_sentences(paragraph):
    # Split the paragraph into individual sentences using regular expressions.
    sentence_pattern = r'(?<!\w\.\w\.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z0-9])'

    sentences = re.split(sentence_pattern, paragraph.strip())
    return [s.strip() for s in sentences if s.strip()] 


def display_sentences_and_count(sentences):
    # Prints each sentence on a new line and displays the total count.
    print("\nSentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}: {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")


def main():
    # prompt user to input a paragraph
    paragraph = input("Enter a paragraph: ")
    sentences = split_into_sentences(paragraph)
    display_sentences_and_count(sentences)


if __name__ == "__main__":
    main()
