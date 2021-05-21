from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.random import RandomSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
nltk.download('punkt')


class TextSummarizer:

    stemmer = None
    summarizer_model = None

    def __init__(self, url: str, summarizer_type: str):
        self.url: str = url
        self.summarizer_type: str = summarizer_type
        self.language: str = "english"
        self.sentences_count: int = 10
        self.set_stemmer()
        self.set_summarizer_model()

    def set_stemmer(self):
        self.stemmer = Stemmer(self.language)

    def get_stemmer(self):
        return self.stemmer

    def set_summarizer_model(self):
        if self.summarizer_type == 'random':
            self.summarizer_model = RandomSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'luhn':
            self.summarizer_model = LuhnSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'lsa':
            self.summarizer_model = LsaSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'edmundson':
            self.summarizer_model = EdmundsonSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'lexrank':
            self.summarizer_model = LexRankSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'textrank':
            self.summarizer_model = TextRankSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'sumbasic':
            self.summarizer_model = SumBasicSummarizer(self.get_stemmer())
        elif self.summarizer_type == 'kl':
            self.summarizer_model = KLSummarizer(self.get_stemmer())
        self.summarizer_model.stop_words = get_stop_words(self.language)

    def get_document(self):
        return HtmlParser.from_url(self.url, Tokenizer(self.language)).document

    def get_summary(self):
        summary = ""
        sentences = self.summarizer_model(self.get_document(), self.sentences_count)

        for sentence in sentences:
            summary += sentence.__str__()
        return summary
