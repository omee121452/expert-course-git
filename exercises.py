'''
Complete the following exercises with your team!
Then create a new branch with your name.
Add, commit, and push your commit to origin on this new branch.
Finally, create a pull request.
'''

def fizzbuzz(num):
    '''
    Write a function that prints the numbers from 1 to 100. But for multiples of three
    print "Fizz" instead of the number and for the multiples of five print "Buzz". For
    numbers which are multiples of both three and five print "FizzBuzz".
    '''
    for i in range(num):
        if i % 5==0 and i % 3==0: 
            print('FizzBuzz') 
        elif i % 3==0:
            print('Fizz')
        elif i % 5==0:
            print('Buzz') 
        else:
            print(i)

#fizzbuzz(100)

def is_palindrome(str):
    '''
    Write a function that checks if a given string is a palindrome (i.e. reads the same
    forwards and backwards). For example, "racecar" is a palindrome.
    '''
    
    return False

def is_anagram(str1, str2):
    '''
    Write a function that checks if two given strings are anagrams (i.e. contain the same
    letters but in a different order). For example, "listen" and "silent" are anagrams.
    '''
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

def count_vowels(str):
    '''
    Write a program that takes a string as input and counts the number of vowels
    (a, e, i, o, u, A, E, I, O, U) in the string.
    '''
    vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    amountOfVowels = 0 
    for i in str:
        for x in vowels:
            if i == x:
                amountOfVowels +=1
    return amountOfVowels



def reverse_list(lst):
    '''
    Write a function that takes a list as input and returns a new list with the elements
    reversed. For example, [1, 2, 3] should become [3, 2, 1].
    '''
    rvrsdLst=[]
    for i in lst:
        rvrsdLst.append(lst[-i])
    return rvrsdLst

if __name__ == '__main__':
    # test and run your functions here
    fizzbuzz(100)
    # print(is_palindrome('racecar'))
    # print(is_palindrome('not a palindrome'))
    print(is_anagram('listen', 'silent'))
    print(is_anagram('not an anagram', 'anagram'))
    print(count_vowels('there are vowels in HERE'))
    print(reverse_list([1, 2, 3, 4, 5]))
   