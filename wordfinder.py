"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """creates list of words from included file"""
    def __init__(self,url):
        self.fileinfo = open(f"{url}","r")
        self.words = self.fileinfo.read().split()
        print(str(len(self.words))+ " words read")

    def random(self):
        """selects random word from initialized list """
        return random.choice(self.words)

words = WordFinder("words.txt")

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, words):


        return [w.strip() for w in words
                if w.strip() and not w.startswith("#")]
