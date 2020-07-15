from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy 
import pandas 
import nltk
import collections
import json
import string
import re
import sys
from nltk.corpus import twitter_samples as tw
from nltk import cluster
from nltk.cluster import cosine_distance
from collections import Counter
import matplotlib.pyplot as plt

numpy.set_printoptions(threshold=sys.maxsize)

def preprocesTweets(bigTweets):
	# Creating stopStrings
	# English stopwords defined by the NLTK package.
	stopStrings = nltk.corpus.stopwords.words('english')
	# adding empty string to list of stopStrings
	stopStrings = stopStrings + list("")
	# adding other useless words in the list
	stopStrings = stopStrings + list("ah")

	#reading list of internet jargons
	jargonsJSON = open('interSlangs.json', 'r').read()
	jargons = json.loads(jargonsJSON)
	#adding jargons in lowercase to stopstrings
	for jargon in jargons:
		stopStrings.append(jargon.lower())

	proceTweets = []
	for tweet in range(0,len(bigtweets)):
		#removing digits
		bigtweets[tweet] = re.sub(r'\d+', '', bigtweets[tweet])
		#removing newlines
		bigtweets[tweet] = re.sub(r'\n+', ' ', bigtweets[tweet])
		#removing @
		bigtweets[tweet] = re.sub(r'@', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'£', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'❌😱', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'…', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'👍', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'😂', '', bigtweets[tweet])
		bigtweets[tweet] = re.sub(r'😁', '', bigtweets[tweet])

		#removing punctuations
		for char in string.punctuation:
			bigtweets[tweet] = bigtweets[tweet].replace(char, '');
		#making everything lowercase
		bigtweets[tweet] = bigtweets[tweet].lower()
		#splitting tweets by space		
		proceTweets.append(bigtweets[tweet].split(" "))

	#for each tweet
	for tweet in range(0, len(proceTweets)):
		for item in stopStrings:
			proceTweets[tweet] = list(filter(lambda a: a != item, proceTweets[tweet]))
				#removing http links
		for word in range(0, len(proceTweets[tweet])):
			if ("http" in proceTweets[tweet][word]):
				proceTweets[tweet].pop(word)
				break;

	return proceTweets

## LOADING DATA
alltweets = tw.strings('tweets.20150430-223406.json')

#removing small tweets (less than 140 chars) because they might be too meaningless to classify 
bigtweets = []
for tweet in alltweets:
	if len(tweet) > 140:
		bigtweets.append(tweet)	

### PREPROSSESSING
tweets = []
#saving without the preprocessing
unchangedTweets = []
unchangedTweets = bigtweets.copy()
tweets = preprocesTweets(bigtweets)

## Now each tweet is a list of strings, I have to transform it into bag of words to use cosine similarity
#I generate the vocabulary for the BoW
vocab = []
for tweet in tweets:
	vocab = vocab + tweet

vocab= list(dict.fromkeys(vocab))

#generating the vectors for each text
tweetsBoW = [None] * len(tweets)
for tweet in range(0, len(tweets)):    
	tweetsBoW[tweet] = numpy.zeros(len(vocab))
	for w in tweets[tweet]:            
		for i,word in enumerate(vocab):                
			if word == w:                     
				tweetsBoW[tweet][i] += 1                            

#clustering
nClusters = 10
kmeans = cluster.KMeansClusterer(nClusters,  cosine_distance, avoid_empty_clusters=True,conv_test=1e-4)  
clusters = kmeans.cluster(tweetsBoW, True, trace=True) 

#printing each tweet as well as the cluster they were assigned to
for doc, cls in zip(unchangedTweets, clusters):
    print(cls,doc)

#plotting clusters number of elements for analysis
labels = list(range(0,nClusters))
values = list(Counter(clusters).values())
y_pos = numpy.arange(len(labels))
plt.bar(y_pos,values, color = (0.5,0.1,0.5,0.6))
plt.title('Number of clusters in total = '+str(nClusters))
plt.xlabel('Clusters')
plt.ylabel('Number of tweets')
plt.ylim(0,400)
plt.xticks(y_pos, labels)
plt.show()

