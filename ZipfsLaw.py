import nltk
import requests
from collections import Counter, defaultdict
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def get_html(url):
    response = requests.get(url)
    return str(response.text.encode('utf-8', 'ignore'))

def print_list(L):
    for i in L:
        print(i)

def save_string(s, filename):
    with open(filename, 'w+') as outfile:
        outfile.write(s)

def load_string(filename):
    with open(filename, 'r') as infile:
        return infile.read()

# url = 'https://www.gutenberg.org/files/1342/1342-0.txt'
# text = get_html(url)
# save_string(text, 'pride_and_prejudice.txt')
text = load_string('dune.txt')
text = text.replace('\\r', '')
text = text.replace('\\n', '')
text = text.replace('\\t', '')
words = nltk.word_tokenize(text)
words = [word.lower() for word in words]
words_freq = sorted(Counter(words).items(), key=lambda x: x[1], reverse=False)
words_data = []
P_1 = re.compile(r'[a-z.\']+')
P_2 = re.compile(r'[a-z]{1}')
for word in words_freq:
    if len(word) == 1:
        m = P_2.match(word[0])
        if m:
            words_data.append([word[0], len(word[0]), word[1]])
    else:
        m = P_1.match(word[0])
        if m:
            words_data.append([word[0], len(word[0]), word[1]])

len_count_dict = defaultdict(int)
for word in words_data:
    if word[1] < 20:
        len_count_dict[word[1]] += word[2]

items = sorted(len_count_dict.items(), key=lambda x: x[0], reverse=False)

lens = [item[0] for item in items]
counts = [item[1] for item in items]

y_pos = np.arange(len(lens))

plt.bar(y_pos, counts, align='center', alpha=0.5)
plt.xticks(y_pos, lens)
plt.xlabel('Word Length')
plt.ylabel('Word Frequency')
plt.title('Zipf\'s Law of Abbreviation')
plt.show()