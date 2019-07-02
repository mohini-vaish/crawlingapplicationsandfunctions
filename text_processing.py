'''text = "hello there i love graphic designing ."
print(text.split())

text_1 = 'Graphic design is the craft of creating visual content to communicate messages. Applying visual hierarchy and' \
         ' page layout techniques, graphic designers use typography and pictures to meet users’ ' \
         'specific needs and focus on the logic of displaying elements in interactive designs to optimize the user experience.'

text_2 = 'Graphic design is the process of visual communication and problem-solving through the use of typography, photography,' \
         ' and illustration. The field is considered a subset of visual communication and communication design, but sometimes the term ' \
         '"graphic design" is used synonymously. Graphic designers create and combine symbols, images and text to form ' \
         'visual representations of ideas and messages. They use typography, visual arts, and page layout techniques to create visual compositions. '


# 1.remove stopwords
token_1 = text_1.lower().split()
token_2 = text_2.lower().split()

text_2 = text_2.replace(',', '')
text_2 = text_2.replace('.', '')
text_2 = text_2.replace(')', '')
text_2 = text_2.replace('(', '')
text_2 = text_2.replace(';', '')

# print(token_1)
stopwords = ['is', 'am', 'are', 'for', 'or', 'a', 'an', 'of', 'at', 'the', 'to', 'it', 'all', 'on', 'you', 'have','in',
             'has', 'use', 'and']
words_1 = []
for word in token_1:
    if word not in stopwords:
        words_1.append(word)
#print(words_1)

words_2 = []
for word in token_2:
    if word not in stopwords:
        words_2.append(word)
print(words_2)

import re
texte='Hey there this is python programmming. ram loves to study python andram scored 95 marks.'
print(re.findall('[a-z]\w+',texte))
print(re.findall('[A-Z|0-9]\w+',texte))

for i in range(len(words_1)):
    if words_1[i].endswith('ing'):
        print(words_1[i])

for i in range(len(words_1)):
    if words_1[i].endswith('ing'):
        words_1[i]=words_1[i].replace('ing','')

print(words_1)

'''
