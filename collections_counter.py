import re
import requests
import collections


def print_frequency(counter, n=10):
    pos = 0
    for word, count in counter.most_common(n):
        pos += 1
        print("{0} - {1}: {2}".format(pos, word, count))


shakespeare_url = 'http://www.gutenberg.org/cache/epub/100/pg100.txt'
req = requests.get(shakespeare_url)
content = req.content

content = re.sub('\s+', ' ', content)  # condense all whitespace
content = re.sub('[^A-Za-z]+ ', '', content)  # remove non-alpha chars
words = content.split()

word_counter = collections.Counter(words)
letter_counter = collections.Counter(content.replace(' ', ''))

print('Top 10 most frequent words (Shakespeare complete works)')
print_frequency(word_counter)

print('Top 10 most frequent letter (useful in criptology): ')
print_frequency(letter_counter)
