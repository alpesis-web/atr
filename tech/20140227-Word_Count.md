Feb 27 2014 | python, word_count, map_reduce | Kelly Chan
# Word Count

word_count in python
```python
import sys
import string

def word_count():

    # 1) Tokenize a line of text into string tokens, by white space
    #    Example: "Hello, World!" will be converted into "Hello," and "World!"
    #
    # 2) Remove all punctuations
    #    Example: "Hello," and "World!" will be converted to "Hello" and "World"
    #
    # 3) Convert all words into lowercases
    #    Example: "Hello" and "World" will be converted to "hello" and "world"


    word_counts = {}

    for line in sys.stdin:
        data = line.strip().split(" ")
        # Your code here
        for word in data:
            word = word.translate(string.maketrans("",""),string.punctuation)
            word = word.lower()
            if word not in word_counts.keys():
                word_counts[word] = 1
            else:
                word_counts[word] += 1
            

    print word_counts

word_count()

```
