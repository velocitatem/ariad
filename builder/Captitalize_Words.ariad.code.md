capitalize_words.py
---
```python
def capitalize_words(sentence):
    """Capitalizes the first letter of every word."""
    return ' '.join(word.capitalize() for word in sentence.split())

def lowercase_rest(sentence):
    """Ensures all other letters in each word are lowercase."""
    # Since the capitalize method used in capitalize_words already makes 
    # all other letters lowercase, this step might seem redundant.
    # But for the sake of following the project definition:
    return ' '.join(word.lower().capitalize() for word in sentence.split())

def TextProcessingPipeline(sentence):
    """Runs the text processing pipeline on the input sentence."""
    # Initially capitalize words
    partiallyCapitalized = capitalize_words(sentence)
    # Then ensure all other letters are lowercase - though they already are from step 1
    formattedSentence = lowercase_rest(partiallyCapitalized)
    return formattedSentence

# Example usage
if __name__ == "__main__":
    input_sentence = "this is an example sentence."
    formatted_sentence = TextProcessingPipeline(input_sentence)
    print(formatted_sentence)
```

This script defines functions based on the operations described in the YAML project definition. The `capitalize_words` function takes care of capitalizing the first letter of every word in the sentence, while `lowercase_rest` is intended to ensure that all other letters are lowercase. Given that the `capitalize_words` function inherently makes all other letters lowercase, the `lowercase_rest` function might seem redundant but is implemented to stick strictly to the procedure outlined in the YAML. The `TextProcessingPipeline` function ties these steps together and demonstrates how you could apply this text formatting pipeline on any input sentence, as showcased in the example usage.