import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib",'pandas','nltk'])
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.corpus import stopwords
from collections import Counter


nltk.download("stopwords")

data=open('paragraphs.txt')
data=data.read()
data


stop_words = set(stopwords.words("english"))
cleaning_data = data.replace(",", "").replace(".", "").replace('(',"").replace('[',"").replace('-','').replace(';','').strip()
cleaning_data

words = cleaning_data.split()

cleaning_words = [word for word in words if word.lower() not in stop_words]

count_words = Counter(cleaning_words)

print("Most Common Words:")
for word, count in count_words.most_common():
    print(word, ": ", count)

most_words = count_words.most_common(20)
labels, values = zip(*most_words)


plt.figure(figsize=(7,7))
plt.bar(labels, values, color='green',edgecolor='black')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top 20 Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()