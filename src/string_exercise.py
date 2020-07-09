class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

        """
        Reverses order of characters in string input_str.
        """
        return None

    def is_english_vowel(self, char):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        
    all_vowels = 'aeiou'
    return char in all_vowels
    print(is_vowel('c'))
    print(is_vowel('e'))
        return None

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        length = 0
      
    for word in sentence.split(): 
        if(len(word) > length): 
            length = len(word) 
      
    return length  
      

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
         wordlen = []
    for n in text:
        wordlen.append((len(n), n))
    wordlen.sort()
    return wordlen[-1][1]
     