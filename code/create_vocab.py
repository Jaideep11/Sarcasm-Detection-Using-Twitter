# Create bag of words dictionary for unigram features
import codecs
import re
sarcasm_file=codecs.open(r"C:/Users/Jaideep Jagani/Desktop/University/semester 6 books and lectures/Information Retrieval (IR)/Sarcasm-Detection-Twitter-master/data/sarcasm_tweets.txt", encoding='utf-8')
nonsarcasm_file=codecs.open(r"C:/Users/Jaideep Jagani/Desktop/University/semester 6 books and lectures/Information Retrieval (IR)/Sarcasm-Detection-Twitter-master/data/nonsarcasm_tweets.txt", encoding='utf-8')

s=set()
for val in sarcasm_file:
    # remove emoticons
    pattern=r'[\U0001f600-\U0001f650]'
    # remove pattern
    re.sub(pattern,'',val)
    l=val.split()
    for word in l:
        word=word.lower()
        s.add(word)

for val in nonsarcasm_file:
    # remove emoticons
    pattern=r'[\U0001f600-\U0001f650]'
    # remove pattern
    re.sub(pattern,'',val)
    l=val.split()
    for word in l:
        word=word.lower()
        s.add(word)
# print(s)
# print(len(s))

dic={}
word_index=11
for q in s:
    dic[word_index]= q
    word_index+=1


vocab_file=codecs.open(r"C:/Users/Jaideep Jagani/Desktop/University/semester 6 books and lectures/Information Retrieval (IR)/Sarcasm-Detection-Twitter-master/data/vocab.txt",'w',encoding='utf-8')
for val in dic:
    vocab_file.write(str(val)+':'+dic[val]+'\n')