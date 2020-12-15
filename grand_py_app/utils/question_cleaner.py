
from .stop_words import common_words, welcome_words

class QuestionCleaner:
    def __init__(self, question):
        self.question = question

    def remove_punctuations(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        final_question = ""
        for char in self.question:
            if char not in punctuations:
                final_question += char
        return final_question

    def remove_stop_words(self):
        pass

    def remove_all(self):
        pass
