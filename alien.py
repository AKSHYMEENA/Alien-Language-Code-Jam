# Solution to the alien language puzzle from code jam qualification round 2009
# pass command line parameters of input file name and output file name
# By Zack Akil 24/05/2016 

import sys

# problem logic

def alien( langi , word , langWordLen):
   lang = langi[:];
   output = 0
   for x in range(0,langWordLen): #for each letter in a word
     for y in range(len(lang)-1,-1,-1): #for each word in the language
        deleteFlag = False
        for z in range(0,len(word[x])): #compare each letter of word to letter in word from the language 
           if(lang[y][x]==word[x][z]):
             deleteFlag = True
             break 
        if(deleteFlag == False): # remove word from language list for checking     
           del lang[y]
   return len(lang)

# file reading/writing logic

if len(sys.argv) >=3:
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
else:
  inputFile = input('Enter input file name: ')
  outputFile = input('Enter output file name: ')

f = open(inputFile, 'r')

data = f.read().split()

wordLen = int(data[0])
langLen = int(data[1])
testLen = int(data[2])

alienLang = data[3:langLen+3]
words = data[langLen+3:testLen+langLen+3]
outputs = []

for i in xrange(0,testLen):
  testWord = words[i]
  realWord = []
  inOr = False
  subWord = ''
  for x in range(0,len(testWord)):
    if(testWord[x] == '('):
      inOr = True
    elif(testWord[x] == ')'):
      inOr = False
      realWord.extend([subWord])
      subWord = ''
    else:
      if(inOr == True):
        subWord += testWord[x]
      else:
        realWord.extend([testWord[x]])      

  output = alien( alienLang , realWord , wordLen)
  outputs.extend([output])

w = open(outputFile, 'w')
for x in xrange(0,testLen):
  w.write('Case #{}: {}'.format(x+1, outputs[x]))
  if x < testLen - 1:
     w.write('\n')
