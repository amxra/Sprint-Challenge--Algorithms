'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    def count_th(word):
    # if initial word is less than 2 words, return 0
    # because it won't be possible for the word
    #  to be "th"
    if len(word) < 2:
        return 0
    # If first two indexes contain 'th", add one to the count - skip over the first index and compare next two adjacent indexes
    elif word[:2] =='th':
        return count_th(word[1:]) + 1
     # If first two indexes dont contain 'th', just skip over the first index and compare next two adjacent indexes
    else:
        return count_th(word[1:])        
print(count_th('theostht'))
