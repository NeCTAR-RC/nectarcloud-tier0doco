# Twitter Scraper User Guide

## Description

Twitter Scraper is a tool developed by Intersect for use in collecting data directly from the Twitter Stream API based on a variety of parameters, including hashtags and phrases, users, location and language, and outputs matching tweets to a comma separated values (.csv) spreadsheet for analysis.

## Target Audience

Twitter Scraper is available for use by any researcher with an account at an Australian research institution that subscribes to the [Australian Access Federation][aaf] (see the [full list of AAF subscribers][subscribers]). Researchers who want to incorporate data from Twitter into their research are encouraged to use Twitter Scraper as a powerful, though relatively easy, service which can be run on the [NeCTAR Research Cloud][nectarRC]. NeCTAR offer VMs to researchers for free for a trial period, or longer periods under a merit allocation scheme. Twitter Scraper itself is completely free for researchers.

## How to Launch

Twitter Scraper is deployed through [Launchpod], a web utility for configuring and deploying virtual machines (VMs) onto the NeCTAR Research Cloud. Launchpod allows for users with little or no experience with cloud computing to configure and deploy Twitter Scraper easily and quickly. Before deploying Twitter Scraper, please refer to the [documentation][launchpod-doc] for deploying VMs using Launchpod.

If you intend to log into Twitter Scraper via SSH, for example to modify the harvester settings after it has been deployed, you must specify an SSH keypair in Launchpod. Please follow the instructions in the [Launchpod user guide][launchpod-doc] or at [NeCTAR Research Cloud][nectarrc] on how to do so.

### Obtaining Twitter access credentials

**Important:** *The steps to obtain your Twitter access tokens and consumer API keys only need to be done once. If you intend to deploy more Twitter Scrapers, you should use the same access tokens and credentials. You can always log into the Twitter Applications Development site to get access tokens you've already generated, or you can keep them in a safe place for later use.*

Twitter Scraper uses your Twitter account to monitor the constant stream of tweets and find those matching your specified search terms. Before you can use Twitter Scraper, you need to create an ‘application’ within Twitter, and then obtain the Consumer Key and the Consumer Secret from this application, as well as your Access Token and Access Token Secret.

First, navigate to the [Twitter Applications Development][apps.twitter] site and log in with your Twitter credentials. From here you will create the ‘application’. This page is typically used by developers to register apps that they have created and which people can download. Most of the information is actually irrelevant for Twitter Scraper, but it needs to be entered in order to create the access credentials that Twitter Scraper needs. As of mid-2015, you need to have a mobile phone number associated with your Twitter account to register an application. If you don't have a mobile number, go to your Twitter profile and enter one.

Click Create New App and provide a name (such as ‘Twitter Scraper’) and a brief description (such as ‘this is an app to harvest tweets’). You also need to provide a URL. It does not have to be a real website, but it does have to begin with `http://`. A dummy URL like `http://www.example.com` is sufficient. Scroll to the end of the page and select 'Yes, I agree to the Developer Agreement'. Finally, click 'Create your Twitter Application'.

Once your app has been created, navigate to the ‘Keys and Access Tokens’ tab of the app settings. This page will display two of the four settings you need, the Consumer Key (API Key) and the Consumer Secret (API Secret). You can copy these straight out of Twitter and into a note or document for use later, or put them directly into the relevant fields in Launchpod.

![screenshot_consumerKey][screenshot_consumerKey]

To generate the other two credentials, scroll to the bottom of the same page and under 'Your Access Token' click the button 'Create my access token'. The page will reload, and the Access Token and the Access Token Secret will be displayed at the end. Make sure when copying the Access Token that you copy the whole line including the 9-digit number at the front, which is the same as your owner ID. The Launchpod Twitter Scraper will not function without this.

![screenshot_accessToken][screenshot_accessToken]

Now that you have all of the access credentials needed to deploy Twitter Scraper, you can begin configuring the tweet harvesting parameters.

### Specifying Harvest Parameters

Twitter Scraper search parameters need to be configured prior to the deployment of the server. Once it is deployed, you cannot change the search settings without logging in to the VM via SSH. Harvest parameters are split into two categories: [Matching Options](#matching-options), what Twitter Scraper will search for; and [Output Options](#output-options), how Twitter Scraper will format and configure the output CSV file.

#### Matching options

##### Phrases

This is where you will enter the search terms and hashtags that Twitter Scraper will monitor the Twitter stream for. You can set search phrases in a number of ways. To search for an individual word, enter a single word and hit return. If you want to search for tweets that contain multiple words in any order, enter each word and hit return. If you want to search for an exact phrase, enclose the phrase in double quotes before hitting return. The example below will return any tweet that contains the word ‘Launchpod’, in addition to any tweet that contains both the words ‘Intersect’ and ‘Australia’, in addition to any tweet that contains the exact phrase ‘Twitter Scraper’.

![screenshot_include_1][screenshot_include_1]

In other words, each search term is separated by an implicit OR operation, and every word inside a search term (such as ‘Intersect Australia’ above) is separated by an implicit AND operation. Lastly, any phrase in double quotes will match only those tweets that contain that exact phrase. You can also mix multiple words and exact phrases in a single search term, such as the search term below, which will return only tweets that contain the exact phrase ‘Twitter Scraper’ as well as both words ‘Intersect’ and ‘Australia’.

![screenshot_include_2][screenshot_include_2]

##### Exclude Phrases

This field is used to block the persistence of tweets that match the pattern. Exclusion overrules inclusion, meaning that even if a tweet matches every inclusion parameter, if it matches a single exclusion parameter, it will not be included in the output. The excluded phrases field works exactly like the phrases field in the interpretation of terms.

##### Users

You may also specify particular users you want to include in your search using the users field. If you leave this blank, the effect will be that all users are included in the harvest. If you have just one username entered, only tweets from that user will be included in the output. If you need to include a large list of usernames, you can paste a list of usernames separated by commas.

If you specify both a set of users and a set of phrases for your harvest parameters, both criteria must be satisfied for a tweet to be harvested. In otherwords, only tweets by users specified in your Users *and* which satisfy your phrase search will be harvested. You may specify a set of users, or just a single user, without specifying search phrases, in which case all tweets by those users will be harvested.

##### Location

Checking the ‘Set Location Bounds’ will open a map window in which you can define a bounding box. Only tweets that are geocoded as originating from inside that box will be included in the output. Tweets that originated from outside the bounding box will not be harvested, nor will tweets that are not geocoded. Remember that users can switch off geocoding, and many do for privacy reasons.

##### Languages

You can use the Languages field to restrict your search to tweets in that language. You can also select multiple languages. The effect of selecting no language here is analogous to selecting no users; any tweet will match irrespective of its language value. Tweets are identified as being in a particular language automatically by machine detection, and this may not work perfectly.

#### Output Options

##### Output Fields

The output fields allows you to customise the spreadsheet output containing the tweets. By default, all elements are included, but you can uncheck any of the checkboxes if you do not want to include a particular tweet attribute in your output.

##### Treat Hashtags Independently

This setting modified the behaviour of Twitter Scraper when tweets contain multiple hashtags. Hashtags are parsed out of the content of the tweet body and sent to a separate column of the spreadsheet output. If this box is left unchecked, a tweet containing more than one tweet will occur once in the spreadsheet, and both hashtags will be written to the hashtag column. If this box is checked, then the tweet will be repeated in the output spreadsheet, once for each hashtag, and the hashtag column will contain only one hashtag. This may be useful if you intend to process the output of the scraper using hashtags. If you only intend to analyse the tweet body, you may want to leave this box unchecked so as not to have repeats of the tweet.

##### De-Identify

This checkbox allows you to de-identify the tweets captured by the scraper, which can be useful for research ethics and privacy concerns. When this box is checked, the username column of the output will be replaced by a string so that you cannot identify the user. However, since the same username will be replaced by the same string each time, meaning you are still able to track particular users’ tweets. Note that selecting the de-identify checkbox does not obscure usernames within the body text of tweets.

##### Period

The period refers to the time interval between each time Twitter Scraper writes the data out to a spreadsheet. The output works by filling a cached buffer of tweets as they emerge in the Twitter stream and are captured by the scraper. The buffer can fit a few dozen tweets. When the buffer fills, the content is appended to a spreadsheet. When the period ends and the next period begins (that is, the next hour if you select ‘hourly’), then a new spreadsheet will be commenced. If you select ‘none’ as the period, then every matching tweet will be written to the same spreadsheet. If your scrape settings are broad and capture a lot of tweets, the spreadsheet can blow out in size very quickly. Depending on how many tweets you expect to match your search settings, you may want to set the period to daily, or even hourly, to manage the size of the output spreadsheet.

After you have configured Twitter Scraper, you can now deploy it by clicking ‘Deploy’. The process should only take around three minutes, after which you will be sent an email letting you know that your Twitter Scraper instance has been deployed. This email will also let you know how you can access the data.

## Accessing Data

Twitter Scraper allows for two methods of accessing the data that it generates: over http using a browser, or by logging in to the VM using SSH. Access the machine via SSH also enables you to undertake further configuration and advanced usage, such as modifying the harvest settings, restarting the harvester or configuring additional harvests.

### How to Access Data via Web

While Twitter Scraper is operational, it will continue to extract tweets from the Twitter Stream and, every time its buffer fills, write those tweets to the csv file. A link to the location of the spreadsheet, consisting of the IP address of the machine and a directory, such as `{IP address}/1`, will be included in the email that Launchpod sends you. Clicking this link will take you to a web view of a directory on the VM containing a spreadsheet (or more) of Twitter Scraper's output data. If you selected a time period, then you will see one spreadsheet corresponding to each of that period that has begun since the VM was deployed. 

![screenshot_output][screenshot_output]

Due to the way Twitter Scraper is deployed, there are no easy ways to see if it is working, until tweets begin to appear in the spreadsheet, which, depending on the harvest settings, could be a long time. That is, if you specific very specific search terms, you might be waiting a long time for the buffer to fill and for the tweets to be written to the spreadsheet, and in the meantime, you have no way of knowing whether the lack of output is due to an error or a lack of matching tweets. There is a log file which can be accessed by navigating to the IP of the machine (sent to your email) followed by `/logs`. If the scraper is working, this log file will display lines like:

`2015-04-15 00:05:41,925 INFO  (LoggerTweetProcessor.java:42) - [1] Processed 10 tweets`

If the log file shows an error or java exception instead, then you may have configured the machine incorrectly. You should delete the instance and try again, paying particular attention to the Twitter API Access Tokens and Consumer Keys. Alternatively, you can log into the machine using SSH and [troubleshoot](#troubleshooting) the problem.

### How to Access Data via SSH

Launchpod enables you to access the VM directly via SSH in order to modify the [configuration](#configuration-guide) file 

## Configuration Guide

The options selected within Launchpod are used to populate Twitter Scraper's configuration file. Advanced users may log into the VM using their ssh key and modify the configuration file after deploying via Launchpod. The config file is located at `/home/devel/twitterScraper-{version}/config.ini`. 

If the config file is modified, the harvester must be restarted before any changes take effect. Restart the harvester using the command `sudo supervisorctl restart twitter_scraper`. It is a good idea to change the ouput path if you change the harvester settings, since Twitter Scraper will overwrite an existing output spreadsheet if its output will have the same name.

Here is a sample configuration file:

```
[main]
; The [main] section contains the access tokens and consumer keys for the Twitter application.
; These are created and obtained from http://apps.twitter.com. Each is required in order for
; Twitter Scraper to work

consumerKey =
consumerSecret =
token =
tokenSecret =

; The following section is an example. Additional sections can be added with [2], [3], and so forth. 
; Each section must have a unique outDir and at least one of: phrase, location or user, in order for
; Twitter Scraper to function.

[1]

; At least one of phrase, user or location is mandatory. 
; Multiple phrase, exclude, user, location and language are accepted on unique lines. That is,
; no more than one property per line.

phrase = 
; Not case-sensitive. Will match substring. Multiple lines beginning with 'phrase =' will persist 
; all tweets that match any phrase. Multiple words in one phrase property will persist tweets that
; contain all words in that property in any order. A phrase property in quotation marks will only match 
; tweets that contain that exact phrase.
;
; Example:
; phrase = Phrase1
; phrase = Phrase2
; will match tweets that contain either Phrase1 or Phrase2.
;
; phrase = Phrase1 Phrase2
; will match tweets that contain both Phrase1 and Phrase2.
;
; phrase = "Phrase1 Phrase2"
; will match tweets that contain the exact string "Phrase1 Phrase2"
;
; As phrases will match a substring, searching for hashtags need not include the hash character. Example:
; phrase = hashtag
; will return tweets containing the string hashtag and #hashtag, whereas
; phrase = #hashtag
; will not necessarily return tweets containing the string hashtag (unless they are matched by another
; property)

exclude = 
; Works exactly like the phrase property, but instead of persisting its matches, exclude blocks them from 
; persisting. Tweets that match a phrase property will out persist if they also match an exclude property.
; Exclude cannot be the only matching property.

user =
; Not case-sensitive. Will not match substring. Each user property must be a Twitter username.
; Must not be preceded with @, or it will not match the desired user. 
; user = foo will match all tweets by user @foo.

location = S,W,N,E
; The location property can be used to match tweets that are geotagged and fall inside a specified rectangle.
; The location property takes exactly four arguments, each a number between -180 and +180. The arguments 
; correspond to the south-most extent, the west-most, the north-most and the east-most, and they must occur 
; in that exact order.
; Given that many users do not geotag their tweets due to privacy concerns, setting this option may
; severely limit the number of tweets harvested.

language =
; The language property can be used to restrict the output to tweets in a particular language as determined
; by Twitter's language detection system. Languages are represented by their 2-digit identifier. The list
; of supported languages is 

; If distinct matching properties are used in conjunction with one another, each matching option serves to 
; restrict the others.
;
; Example:
; user = foo
; phrase = bar
; will only match tweets by the user '@foo' that contain the string 'bar', rather than all tweets by user 
; '@foo' and all tweets containing 'bar' 

outPeriod = [hourly|daily|weekly|monthly] 
; Period to which a single output csv file will correspond to. If this property is not included in the config
; file, all tweets will be appended to a single csv spreadsheet.

outField = (createdAt|hashTags|urls|language|text|username|coordinates|place|retweetCount|isRetweet|originalUsername)
; The outfield property configures the elements of each tweet that are output to the csv file, and the order of
; the columns.

outDir = /home/devel/twitterScraper-1.0.39/output/1
; The outDir property is the path to the directory in which the harvested tweets will be written to a csv file.
; The actual name of the csv file will depend on the section number in the config file and the outPeriod.
```

## Contact

If you are having trouble launching Twitter Scraper, please [contact Intersect](mailto:help@intersect.org.au?subject=Assistance with Twitter Scraper), or your university’s [eResearch Analyst][eras].

## Support

## Code Repository

The code repository is not currently publicly released. Twitter Scraper is currently only available through [Launchpod].

## Known Issues

- Twitter Scraper has no way of warning or alerting errors to the user. This may make it difficult to troubleshoot problems. 
- Twitter Scraper uses the Twitter Stream API to harvest tweets in realtime. It does not use the Search API which is for finding statuses that have already been posted to Twitter. This means that Twitter Scraper is unable to harvest historical tweets.
- If a tweet is deleted by a user from their timeline, an instruction to disregard the status is sent via the Stream API. Due to the way Twitter Scraper outputs tweets, by appending them to a csv text file, the instruction to disregard a tweet cannot be honoured. This means that tweets that have harvested and then deleted by the originating user will still appear in the output.

## Troubleshooting

Symptom|Possible Problem|Solution
:---|:---|:---
Launchpod failed to deply|Some availability zones may experience problems launching machines|Try again using another availability zone


[screenshot_consumerKey]: images/twitterDOCID88_consumerKey.png "Consumer Key"
[screenshot_accessToken]: images/twitterDOCID88_accessToken.png "Access Token"
[screenshot_include_1]: images/twitterDOCID88_include_1.png "Included phrases"
[screenshot_include_2]: images/twitterDOCID88_include_2.png "Included phrases"
[screenshot_output]: images/twitterDOCID88_output.png "Sample output"
[aaf]: http://aaf.edu.au
[subscribers]: http://aaf.edu.au/subscribe/subscribers/
[nectarRC]: http://cloud.nectar.org.au/
[launchpod-doc]: ../Launchpod-doc
[launchpod]: http://launchpod.intersect.org.au
[apps.twitter]: https://apps.twitter.com
[eras]: http://intersect.org.au/content/eresearch-analysts
