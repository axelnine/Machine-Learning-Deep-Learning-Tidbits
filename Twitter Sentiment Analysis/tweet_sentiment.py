import json
import sys
import re

sent_scores = {}
def get_term_sentiment_dictionary(file):
    '''
    '''
    for line in file:
        term,sent_score = line.split("\t")
        sent_scores[term] = int(sent_score)
    
def get_tweets(file):
    '''
    '''
    for line in file:
        result = json.loads(line)
        str = result.get('text','NA')
        str = re.sub(r'@[A-Za-z0-9]+','',str)
        str = re.sub(r'^https?:\/\/.*[\r\n]*', '', str, flags=re.MULTILINE)
        list_of_words = re.compile('\w+').findall(str)
        #list_of_words = str.strip().split()
        get_score(list_of_words)
   
def get_score(list):
    '''
    '''
    final_score = 0
    for word in list: 
        if word in sent_scores.keys():
            final_score+=sent_scores[word]
        else:
            final_score+=0
    print(final_score)

def main():
    '''
    '''
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    get_term_sentiment_dictionary(sent_file)
    get_tweets(tweet_file)

if __name__ == '__main__':
    main()
