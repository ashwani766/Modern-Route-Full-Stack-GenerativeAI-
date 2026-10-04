from sklearn.preprocessing import OneHotEncoder
import numpy

document = ["my name is ashwani and i love ai" ]      

tokens = [sentence.lower().split() for sentence in document]
print(tokens)

all_words = [[word] for sentence in tokens for word in sentence]
print(all_words)

encoder = OneHotEncoder(sparse_output=False)
encoder.fit(all_words)
print("vocabulary:", encoder.categories_[0])

print("tokens",tokens)

for sentence in tokens:
    print(sentence)

for sentence in tokens:
    encoded_sentence = encoder.transform([[word] for word in sentence])
    print(sentence)
    print("encoded sentence: \n", encoded_sentence)