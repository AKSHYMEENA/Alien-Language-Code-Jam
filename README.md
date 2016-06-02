# Alien-Language-Code-Jam
Solution to the alien language puzzle from [google code jam qualification round 2009](https://code.google.com/codejam/contest/90101/dashboard)

##The problem
After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

##Solution theory
The script searches through the alien language (whilst comparing them to the message) and removes the words that are not possible translations from the search so as to eliminate redundant checking of words. 

Then the final count of the remaining words in the language is the number of possible translations.

##Usage
To use the solution: run the python script from a terminal passing it the name of the input file followed by the desired name of the output file.   

```
$ /User python alien.py C-small-practice.in small-output.out
```
