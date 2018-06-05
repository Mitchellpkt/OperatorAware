# OperatorAware
## Urgency detection for emergency calls
2018.06.04
mitchellpkt@protonmail.com 2018.06.04

OperatorAware evaluates 911 calls in real-time to assess the nature and direness of the emergency being reported.

As the human operator collects information, OperatorAware converts the audio stream to text, and scans for keywords indicating critical situations (e.g. the word "gun" indicating that there is likely a weapon involved). As the call continues, OperatorAware updates the likelihood of a situation involving:
-  Weapons (e.g. inferred from use of words "gun" and "shot" by a caller)
-  Medical emergencies 
-  Vehicle accidents
-  etc

## Example
Caller reports: **"My neighbor shot my leg, It's bleeding everywhere! He didn't mean to fire the gun"** 

OperatorAware uses the words {"shot", "bleeding", "gun"} to identify that this is a **medical emergency involving a weapon.**

## Motivation
There have been multiple reported instances of emergency operators hanging up on 911 callers during crises. 

For example, one operator who stated "You could deal with it yourself. I’m not gonna deal with this, okay?” before hanging up on a caller that was performing CPR on a shooting victim ([Washington Post](https://www.washingtonpost.com/news/post-nation/wp/2015/07/29/deal-with-it-yourself-911-dispatcher-tells-panicked-caller-with-dying-friend/?utm_term=.eea24de1e5f3)). 

Another 911 dispatcher, infamous for ending a call with "Ain't nobody got time for this," hung up on reports of street racing and armerd robberies (different [Washington Post](https://www.washingtonpost.com/news/post-nation/wp/2018/04/19/911-dispatcher-jailed-houston-woman-hung-up-on-thousands-of-callers/?noredirect=on&utm_term=.b4bb2b6e8f37) article). In this case, later analysis showed that thousands of calls shorter than 20 seconds were attributed to her hanging up. She stated that she hung up because at those times she did not want to talk to anyone ([BBC](http://www.bbc.com/news/world-us-canada-43822504)).

While 911 callers may hang up at any time, in the vast majority of cases, **the 911 dispatcher should not be the party to terminate the call during a crisis.** If an operator is the party to end a call that has been ranked as likely-severe by the OperatorAware, this should trigger quality assurance review. The latter dispatcher mentioned above hung up on thousands of calls over multiple years. With OperatorAware, she would have come under close scrutiny by the end of her first week

## Use case scale
The [Washington Post](https://www.washingtonpost.com/news/post-nation/wp/2018/04/19/911-dispatcher-jailed-houston-woman-hung-up-on-thousands-of-callers/?noredirect=on&utm_term=.d2fbe079869a) notes: *[This single] consolidated center for 911 calls opened in 2003 and handles millions of calls every year, according to the Chronicle, or 9,000 a day. Two-thirds of those calls aren’t true emergencies*

*The rest involve people in dire need.*

## Training Data
The `Real911_Calls` directory contains several real 911 calls, [posted publicly](http://www.lapdonline.org/communications_division/content_basic_view/27361) by the LAPD:

-  medical emergency  
-  officer shot         
-  car accidents
-  attempted murder   
-  possible burglary
-  assault & battery
-  shots fired

The website [http://911callers.com/](http://911callers.com/) contains 89 calls to 911, including both emergency and non-emergency situations. It appears that all of the audio files are stored in the root directory, thus accessible by `wget 911callers.com/<callname>.swf`


