
from grand_py_app.utils.constants import COMMON_WORDS, GREETINGS, PUNCTUATIONS


class QuestionCleaner:

    def __remove_punctuations(self, question):
        question_cleaned = ""
        for char in question:
            if char in PUNCTUATIONS:
                question_cleaned += " "
            else:
                question_cleaned += char
        return question_cleaned

    def __remove_stop_words(self, question):
        question_cleaned = ""
        for word in question.split():
            if word.lower() in COMMON_WORDS or word.lower() in GREETINGS:
                question_cleaned += " "
            else:
                question_cleaned += word.lower() + " "
        return question_cleaned

    def __remove_all(self, question):
        question_cleaned = self.__remove_punctuations(question)
        question_cleaned = self.__remove_stop_words(question_cleaned)
        return question_cleaned.strip()

    def address_for_url(self, question):
        question_cleaned = self.__remove_all(question)
        question_splited = question_cleaned.split() # ['55', 'rue', 'faubourg', 'saint', 'honoré', 'paris']
        return "+".join(question_splited) # '55+rue+faubourg+saint+honoré+paris'
