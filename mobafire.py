import sys
import urllib.request
from html.parser import HTMLParser

BASE_URL = "http://www.mobafire.com"
BASE_URL_GAME_LOL = BASE_URL + "/league-of-legends/"
BASE_URL_GUIDE_LIST_POSTFIX = "-guide"


def get_champ_guide_url(champion):
    return BASE_URL_GAME_LOL + champion + BASE_URL_GUIDE_LIST_POSTFIX


def get_specific_guide_url(url):
    return BASE_URL + url


def get_page_html(url):
    data = "".join([chr(x) for x in urllib.request.urlopen(url).read()])
    return data


def get_attribute(attributes, name, default=""):
    for attrName, value in attributes:
        if attrName == name:
            return value
    return default


class mobafireParser(HTMLParser):
    guides = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            className = get_attribute(attrs, name="class")
            href = get_attribute(attrs, name="href")
            if "build-title" in className:
                self.guides.append(href)


def get_guides(championName):
    guideURL = get_champ_guide_url(championName)
    parser = mobafireParser()
    parser.guides = []
    parser.feed(get_page_html(guideURL))
    return [get_specific_guide_url(x) for x in parser.guides]


def get_top_guide(championName):
    return get_guides(championName)[0]


if __name__ == "__main__":
    championName = sys.argv[-1]
    print("Top guide:", get_top_guide(championName))
