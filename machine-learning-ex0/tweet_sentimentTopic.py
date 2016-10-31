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
    lines(tweet_file)
    #tweets = listTweet(tweet_file)
    #dictionnary = createDictionnary()
    #result = (ScoreTweet(tweets, dictionnary))
    #afficheList(result)
    #print sumList(result)
    #print json.loads(tweet_file_list[0])["statuses"][3]["text"]
    #print afficheList(tweets)




    
def createDictionnary():
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
		# print scores.items()  Print every (term, score) pair in the dictionary
	return scores

def listTweet(tweet_file):
    tweet_file_list = json.loads(tweet_file.readlines()[0])
    tweet_result = []
    for i in range(len(tweet_file_list)):
		if tweet_file_list["statuses"][i].keys() != [u'delete']:
			tweet_result.append(tweet_file_list["statuses"][i]["text"])
		else:
			tweet_result.append("")
		i+=1
    return tweet_result
		
def ScoreTweet(tweets, dictionnary):
	score = []
	expression = dictionnary.keys()
	for j in range(len(tweets)):
		score.append(0)	
		for i in range(len(expression)):
			if " "+unicode(expression[i]+" ", 'utf8') in tweets[j]:
				score[j] += dictionnary[expression[i]]
	return score

def afficheList(list):
	for i in range(len(list)):
		print list[i]

def sumList(list):
	score = 0
	for i in range(len(list)):
		score += list[i]
	return score
		
if __name__ == '__main__':
    main()

