import re
import codecs
import csv
filee = codecs.open(r"C:/Users/Jaideep Jagani/Desktop/University/semester 6 books and lectures/Information Retrieval (IR)/Sarcasm-Detection-Twitter-master/data/sarcasm_tweets_gaps.txt", encoding='utf-8')
count=[]
temp=[]
laughter_expression=[]
for l in filee:
    temp.append(l)
    count.append(len(re.findall(u'[\U0001f600-\U0001f650]', l)))
    expression1=re.compile(r'(\blols?z?o?\b)+?',re.I)
    expression2=re.compile(r'(\brofl\b)+?',re.I)
    expression3=re.compile(r'(\blmao\b)+?',re.I)
    laughter_expression.append(len(re.findall(expression1,l)) + len(re.findall(expression2,l)) + len(re.findall(expression3,l)))



with open(r"C:/Users/Jaideep Jagani/Desktop/University/semester 6 books and lectures/Information Retrieval (IR)/Sarcasm-Detection-Twitter-master/data/sarcasm_emoji.csv",'w') as csvfile:
    x=csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    x.writerow(['emoji_count','laughter_exp_count'])
    for i in range(len(temp)):
        x.writerow([count[i],laughter_expression[i]])

csvfile.close()

# column 1 will count emojis from tweets
# column 2 will count LOL, ROFL and LMAO, all of them
