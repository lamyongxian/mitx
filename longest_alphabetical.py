#!/usr/bin/env python3

s = 'azcbobobegghakl'

abc ='abcdefghijklmnopqrstuvwxyz'
word = ''
longest_word = ''
prev_index = 0
for i,l in enumerate(s):    #loop through every letter
    
    alpha_index = abc.index(l)
    
    if alpha_index >= prev_index:
        word += l
    else:
        word = l
        
    if len(longest_word) < len(word):
        longest_word = word

    #print(prev_index, alpha_index, l, '"' + word + '"') #DEBUG PRINTOUT
    prev_index = alpha_index
        
print('Longest substring in alphabetical order is:', longest_word)