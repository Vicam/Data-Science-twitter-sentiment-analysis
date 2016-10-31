import sys
import json
import urllib

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    tweets = listTweet(tweet_file)
    dictionnary = createDictionnary()
    result = (ScoreTweet(tweets, dictionnary))
    afficheList(result)
    




    
def createDictionnary():
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
		# print scores.items()  Print every (term, score) pair in the dictionary
	return scores

def listTweet(tweet_file):
    tweet_file_list = tweet_file.readlines()
    tweet_result = []
    for i in range(len(tweet_file_list)):
		if json.loads(tweet_file_list[i]).keys() != [u'delete']:
			tweet_result.append(json.loads(tweet_file_list[i])["text"])
		else:
			tweet_result.append("")
		i+=1
    return tweet_result
		
def afficheList(list):
	for i in range(len(list)):
		print list[i]
		
def ScoreTweet(tweets, dictionnary):
	score = []
	expression = dictionnary.keys()
	for j in range(len(tweets)):
		score.append(0)	
		for i in range(len(expression)):
			if " "+unicode(expression[i]+" ", 'utf8') in tweets[j]:
				score[j] += dictionnary[expression[i]]
	return score
		

if __name__ == '__main__':
    main()

