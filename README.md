# Research_Methods
Research Methods

## Do The Olympic Games raise or decrease the usage of the words gold, silver and bronze?

I will research if the usage of the words gold, silver and bronze or decreases during the olympic games.
This can then be used for targeted adveritesment for precious metal exchanges or other buisnesses.



The dates used:
Summer Olympics
* Dates London Olympics 2012
* 27 July to 12 August 2012 
* Date Rio Olympics 2016
* August 5–21, 2016
* Date Tokyo olympics 2020
* 23 July to 8 August 2021.

Winter Olympics
* Dates Sochi Olympics 2014
* Friday, 7 February - Sunday, 23 February
* Dates PyeongChang Olympics 2018
* 9 February 2018 -	25 February 2018



## Hypothesis
I think the usage of the words gold, silver and bronze will increase during the olympic games

## Sources

https://www-tandfonline-com.proxy-ub.rug.nl/doi/full/10.1080/16184742.2020.1725091

https://link.springer.com/chapter/10.1057/978-1-137-52386-0_8

### How to repeat research:

1. Download this github repository
2. Open the .xlsx file, this file containes the result and the commands used to get the data.
3. An example of the command (This commands connects you to the karora server and gets the tweets as text input for the word_finder.py file): 
ssh s4568966@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2012/{07/201207{29..31},08/201208{01..03}}:10.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i date text' | py word_finder.py
4. When you enter this command you need to change the s nummer to your own.
5. You then need to fill in your password.
6. An then fill in your MFA.
7. Wait untill you see the results, this can take up more than an hour.

