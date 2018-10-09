import json
import sys
import re

instance = {}
count = 0

def get_term_frequency(file):
    '''
    '''
    global count
    for line in file:
        
        result = json.loads(line)

        #Get text
        str = result.get('text','NA')

        #Remove mentions & hyperlinks
        str = re.sub(r'@[A-Za-z0-9]+','',str)
        str = re.sub(r'^https?:\/\/.*[\r\n]*', '', str, flags=re.MULTILINE)
        list_of_words = re.compile('\w+').findall(str)
        
        #Get counts
        for word in list_of_words:
            instance[word] = instance.get(word,0) + 1
            count = count + 1

def print_frequency():
    for key,value in instance.items():
        if(value/count>0.003):
	        print("%s %0.9f" % (key, value/count))
        
def main():
    '''
    '''
    tweet_file = open(sys.argv[1])
    get_term_frequency(tweet_file)
    print_frequency()

main()
