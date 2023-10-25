from .get_word_in_base import get_word_in_mainbase

class trans:
    def __init__(self, l_from, to):
        self.l_from = l_from
        self.to = to

    def trans(self, word):
        try:
            base = get_word_in_mainbase(self.l_from, self.to, word.lower())
            output = base[word.lower()]
            while(output[0] == " "):
                output = output[1:]
            return output
        except:
            return False
