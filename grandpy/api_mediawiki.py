# https://pypi.org/project/pymediawiki/
from mediawiki import MediaWiki


class MediawikiApi:
    """A python wrapper and parser for the MediaWiki API.

    Example:
        wiki = MediawikiApi()
        result = wiki.search('paris')
        print(result)
    Return a string:
        Paris [pa.ʁi]  est la capitale de la France. [En savoir plus sur : https://fr.wikipedia.org/wiki/Paris]
    """

    def __init__(self):
        self.wikipedia = MediaWiki(url='https://fr.wikipedia.org/w/api.php')

    def search(self, address):
        response = self.wikipedia.search(address, results=1)

        page = self.wikipedia.page(response[0])
        wiki_url = 'https://fr.wikipedia.org/wiki/' + response[0]

        section = page.sections[0]
        resume = page.section(section).split("\n")

        if len(resume) == 1:
            resume = page.summary.split(".")
            return (".".join(resume[0:3]),wiki_url)
        else:
            return (resume[0:3],wiki_url)


if __name__ == "__main__":
    wiki = MediawikiApi()
    result = wiki.search('openclassrooms')
    print(result)
