# Research_Methods
Research Methods

## Do The Olympic Games raise or decrease the usage of the words gold, silver and bronze?

Summer Olympics
* Dates London Olympics 2012
* 27 July to 12 August 2012 
* Date Rio Olympics 2016
* August 5–21, 2016
* Date Tokyo olympics 2020
* 23 July to 8 August 2021.

Winter Olympics
* Dates Vancouver Olympics 2010
* Friday, 12 February - Sunday, 28 February
* Dates Sochi Olympics 2014
* Friday, 7 February - Sunday, 23 February
* Dates PyeongChang Olympics 2018
* 9 February 2018 -	25 February 2018



## Hypothesis
I think the usage of the words gold, silver and bronze will increase during the olympic games

## Sources
https://www.researchgate.net/profile/Lyman-Mlambo/publication/233359829_Estimation_of_Technical_Progress_in_Zimbabwe_Mining_Sector_1977-1997_An_Economic_Perspective/links/61b0b1db6cd00716cc411075/Estimation-of-Technical-Progress-in-Zimbabwe-Mining-Sector-1977-1997-An-Economic-Perspective.pdf#page=175

https://d1wqtxts1xzle7.cloudfront.net/30322782/Going_for_Gold-An_Olympic_Investment-libre.pdf?1390884172=&response-content-disposition=inline%3B+filename%3DGoing_for_Gold_An_Olympic_Investment.pdf&Expires=1678282099&Signature=bdr8j3CnHm0e5wV9dliULatE8wUWW2xewM22XoyZYsl8ReCZ38IehBgTs-hx9wK4pXbC0bL0yfUrLQlpaG9cnazUK9-4KbcjTMxBMGqIsKSXbTad80vaHEqy5yfEnGXjNMuCwjGCETkKZQG4JBby9Rhud4qSrrP87aEAtylfEM3gsWNyBRJ-AZsCBMROfAe3W0W7wujAt2pR1OOMq~bWdweIVKeCNRyWSJVq0b5XbPWk-rT2EMWJVGEn9u~E8T2E6Cx2KMAn9iivaRc0toYK9NO~vdOaEUinNqAYvn8dMPooe~7NJdAnnyaa3AZM-2KYoUWaUWHYAb~Q1M0KrAfwew__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA

### Commands used:

Uses word_finder.py to find the words over a given day.


ssh s4568966@karora.let.rug.nl 'zless ../../net/corpora/twitter2/Tweets/2012/{07/201207{29..31},08/201208{01..03}}:10.out.gz | ../../net/corpora/twitter2/tools/tweet2tab -i date text' | py word_finder.py