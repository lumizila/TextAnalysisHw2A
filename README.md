# TextAnalysisHw2A

# This is the report of the Text Analysis class' "Assignment 2A"

This assignment was to develop a program satisfying the following requirements:
- Using 100 or more documents
- Using K-means method
- Using the method of document similarity estimation achieved better results in Assignment 1.  

Report
Content
  ### 1. Summary of the dataset
  
  For this assignment I decided to use the twitter_samples dataset from the NLTK.corpus. (More about it can be seen at http://www.nltk.org/howto/twitter.html )
  The twitter_samples data is actually divided into 3 files, so I chose "tweets.20150430-223406.json" because it is the one with the biggest number of tweets.
  I considered one tweet to be one "document" to be analyzed. 
  
  #### 1.1 Preprocessing 
    
   The original "tweets.20150430-223406.json" file comes with 20,000 tweets. However, many of them are very short which would make them hard to cluster. 
   Therefore I decided to exclude the tweets smaller than 140 characthers, which left me with 857 tweets. 
    
   Next I removed newlines (in exchange for spaces), numbers, punctuations, urls and some emojis from the texts.  
    
   I created a list of "stopWords" using NLTK stopwords for english as well as common internet jargons that you can find in the file "interSlangs.json", which were scraped from https://www.netlingo.com/acronyms.php  
    
   Next I split the tweets in words, and moved all the words that match one of the words in the "stopWords" list. Everything left was transformed to lowercase. 
  
  ### 2. The measure used to estimate document similarity
     
   For measuring document similarity was Cosine Similarity since this was the method that gave the best results on Homework 1.
   (for reference: https://github.com/lumizila/TextAnalysisHomework ) 
    
  ### 3. Comparing the clustering results with different parameter k
  
  I ran the code with 3 different values for k: 5, 10, 15
  And my results of the clustering as well as their evaluation for each k are discussed on the topics below. 
  
  ### 3.1 Describing the contents of the clusters.
  
  As mentioned before, I considered each tweet to be one document, so each cluster will contain multiple tweets. 
 
  ### For K = 5
    
The distribution of the tweets over the clusters can be seen below:
    
  ![GitHub Logo](/K5.png)

For K = 5 it is possible to see that no cluster had a very low number of tweets (always more than 50). The cluster 2 had the lowest number of tweets (82), some of the tweets for cluster 2 were:
     
     2 @bbcnickrobinson you personally &amp; @BBC  @BBCNews have severely diminished credibility. Running scared from Tory funding threats, no cajones
     2 @gazzamagic78 labour voted in favour of more damaging tory cuts at last budget &amp; are now condemning those cuts - disgracefully hypocritical!
     2 RT @SocEconB: Public R&amp;D spending in Britain is lowest in G8. Hits long-term growth &amp; productivity. A #Tory #LongTermEconomicPlan http://t.…
     2 RT @Stana_Katic: Women of #Castle havin a laugh.
        @btwprod @lizbeth4beauty @monixdecastro @prgirl31 Meg June Lillie Mel Irena &amp; Tory. http:/…
     2 RT @Sol_00: @ScotlandTonight @bbcqt That it shows what Labour has become. They'd rather a Tory government than work with SNP &amp; other progre…

The cluster with the biggest number of elements was cluster 0 with 342 elements. Some of the tweets included in this cluster were: 
    
    0 RT @Ed_Miliband: The Tories have drawn up plans to take thousands of pounds from millions of families. Child benefit &amp; tax credits are on t…
    0 RT @Ed_Miliband: The Tories have drawn up plans to take thousands of pounds from millions of families. Child benefit &amp; tax credits are on t…
    0 RT @Ed_Miliband: The Tories have drawn up plans to take thousands of pounds from millions of families. Child benefit &amp; tax credits are on t…
    0 RT @agendaitv: .@DouglasCarswell - Last year in European &amp; local elections the polls underestimated UKIP. Had us second or third #TheAgenda
    0 RT @andrewspoooner: So you've mentioned the Tory press - you always do - why not practice some impartiality &amp; mention others' responses? ht…
    0 RT @AngusMacNeilSNP: Again Nicola Sturgeon a truly amazing political &amp; honest personal connection with audience ..#Impressed  Join SNP at h…
    0 RT @MichaelH14: Ed Miliband : it wasn't the spending on teachers &amp; nurses in Britain that crashed the global economy. 'Bout time someone sa…
    0 RT @Stephen_Mold: RT CCHQPress ".Ed_Miliband can only be PM propped up by SNP - would mean more borrowing, more taxes, more debt &amp; you’d pa…

  ### For K = 10
  
The distribution of the tweets over the clusters can be seen below:

  ![GitHub Logo](/K10.png)
    
For K = 10 it is possible to see that cluster 5 had extremely low number of elements (3), while cluster 2 had a very big number of tweets(242).

The tweets in cluster 5 were:
  
    5 #SNP supporters/voters won't be tricked by Ed's "threat". He's lied to us before. He'll do whatever in his best interests pre &amp; post #GE15.
    5 @QueenOfNaw @Historywoman @spsammy @scepticalscot @softmutt @iainjwatson Gave SNP the "Yes" high ground, let it last two years, &amp; F.P. Post
    5 RT @WelshConserv: We've come a long way in 5yrs. Don't let EdM &amp; SNP drag us back to square one. Let's keep going #SecureTheRecovery https:…
    
Some of the tweets in cluster 2 were:

    2 RT @KevinJPringle: .@Ed_Miliband's distancing from @theSNP wholly under pressure from Tories - he went way too far &amp; has given Labour in Sc…
    2 @Craig4CardiffN Tories not done enough to stop dodging 3200+ on benefit fraud &amp; just 300 on tax avoidance loses more https://t.co/GFdAJcLKul
    2 RT @macplus4: And. Miliband stumbled. Much bigger issues to discuss - NHS, mental health, foodbanks, homelessness, usual cuts to women &amp; ch…
    2 RT @Jacqueline_Gold: Remember Miliband was one of Gordon Brown's advisers! Can't trust a word he says. Labour had 13 yrs in power &amp; crashed…
    2 RT @lucymanning: Ed Miliband stumbles off the stage. A punning gift for his political opponents &amp; headline writers  https://t.co/8PAm2E6okN
    2 RT @LouiseMensch: my fellow Tory tweeps, if you see somebody saying they are voting #Conservative pls take a moment to thank them &amp; follow …

  ### For K = 15
 
The distribution of the tweets over the clusters can be seen below:

  ![GitHub Logo](/K15.png)
  
For K = 15 it is possible to see that cluster 5 had extremely low number of elements (4), while cluster 9 and cluster 3 had a very big number of tweets(230, 158 respectively). 

Some tweets from cluster 5:

    5 RT @mondoreally: Voting Tory/UKIP ? Please unfollow &amp; let me know why so I can unfollow you.You're not my type.It's not me it's you &amp; your …
    5 RT @mondoreally: Voting Tory/UKIP ? Please unfollow &amp; let me know why so I can unfollow you.You're not my type.It's not me it's you &amp; your …
    5 #AnimalWelfare Hustings tonight in Bristol via @lushcampaigns @LeagueACS @AnimalAid Tory,UKIP &amp; Libdems didnt attend! http://t.co/X54eEjNPHT
    5 @mondoreally: Voting Tory/UKIP ? Please unfollow &amp; let me know why so I can unfollow you.You're not my type.It's not me it's you &amp; your …

Some tweets from cluster 9:
  
    9 RT @KevinJPringle: .@Ed_Miliband's distancing from @theSNP wholly under pressure from Tories - he went way too far &amp; has given Labour in Sc…
    9 RT @AngusMacNeilSNP: Again Nicola Sturgeon a truly amazing political &amp; honest personal connection with audience ..#Impressed  Join SNP at h…
    9 @Craig4CardiffN Tories not done enough to stop dodging 3200+ on benefit fraud &amp; just 300 on tax avoidance loses more https://t.co/GFdAJcLKul
    9 RT @macplus4: And. Miliband stumbled. Much bigger issues to discuss - NHS, mental health, foodbanks, homelessness, usual cuts to women &amp; ch…
    9 RT @lucymanning: Ed Miliband stumbles off the stage. A punning gift for his political opponents &amp; headline writers  https://t.co/8PAm2E6okN

Some tweets from cluster 3:
    
    3 Couldn't watch the leaders Q&amp;As tonight as I was at a scholarship dinner, but at said dinner I argued Labour doesn't need nor want the SNP
    3 RT @JimForScotland: Labour has called SNP bluff. The SNP must now be clear: are they willing to prevent or bring down a Labour government &amp;…
    3 RT @WelshConserv: We've come a long way in 5yrs. Don't let EdM &amp; SNP drag us back to square one. Let's keep going #SecureTheRecovery https:…
    3 Sky News have been pushing the "Labour deal with SNP" line for weeks &amp; now admit Lab can go it alone &amp; dare SNP to vote them out #zing
    3 RT @west_views: The BBC's Glen Campbell just can't disguise his dislike of Nicola &amp; the #SNP.
    We need a national broadcaster instead of a W…

  ### 3.2 Evaluating the clustering results.
  
  It is evident that with more clusters it is possible to group tweets that are more and more similar. However, this might create an effect in which small clusters are comprised mostly of retweets, such as seen in cluster 5 from K = 15. There must be a balance between the original number of tweets and the number of clusters. In any way I believe that when K = 15 the groupings were better, from analysing the bar graph. That is because many clusters in K = 15 had a similar number of tweets in them (clusters 1, 13, 4, 14, 0, 10, 6, 2, 7). Two clusters (9 and 3) in K = 15 still had a large number of tweets in them suggesting that maybe it would be better to increase K. When K = 5 there was no cluster with a very low number of elements, however it seems like bigger cluster have elements that are too different from each other (besides the retweets) such is the case with cluster 0. On the other hand cluster 2 from K = 5 had a very nice collection of tweets in it, as you can see from the examples, many different tweets contained the word "Tory" and many were talking about the economy. 
  
  ### 4. Consideration 
  
  Many of the big tweets found are retweets (They are indicated by RT in the beggining of the tweet), which I believe can make the clustering of tweets easier since in retweets the text content in the same as the original tweet. For a future work I would like to remove all the retweets and work only with original tweets. 
  
  ### 5. Source Code  (on GitHub)
  See source code at https://github.com/lumizila/TextAnalysisHw2A
