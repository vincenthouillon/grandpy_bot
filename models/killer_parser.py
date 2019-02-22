import json
import re


class KillerParser:
    """Cut the sentence into words to keep only the key words
    
    Example:
        sentence = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        kp = KillerParser()
        print(kp.keep_keywords(sentence))
    Result:
        ['openclassrooms']
    """

    def __init__(self):

        # self.sentence = sentence
        self.filename = 'models/stopwords_fr.json'
        self.filename2 = 'models/stopwords_perso.json'

    def _load_from_file(self, filename, filename2):
        """Reads and loads JSON files

        Arguments:
            filename {str} -- JSON file provided by OpenClassrooms
            filename2 {str} -- JSON 2 custom file containing other keywords
        """
        with open(filename, encoding='utf-8') as infile:
            stopwords = json.loads(infile.read())
        with open(filename2, encoding='utf-8') as infile2:
            stopwords_perso = json.loads(infile2.read())
            for words in stopwords_perso:
                stopwords.append(words)
        return stopwords

    def keep_keywords(self, sentence):
        """Extract the keywords from a sentence
        """
        keywords = list()
        phrase = sentence.lower()
        data = self._load_from_file(self.filename, self.filename2)
        words = re.split(r"\W", phrase)
        for word in words:
            if word not in data and word != '':
                keywords.append(word)
        return (" ".join(keywords))

if __name__ == "__main__":
    sentence = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    kp = KillerParser()
    print(kp.keep_keywords(sentence))
