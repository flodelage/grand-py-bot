
from grand_py_app.utils.constants import COMMON_WORDS, GREETINGS, PUNCTUATIONS


"""
Responsability: Clean up the user's question.
Remove any unnecessary words and/or characters in order to keep
only the desired place to find.
"""
class QuestionCleaner:

    def remove_punctuations(self, question):
        """
        Remove any punctuations from user's question
        """
        question_cleaned = ""
        for char in question:
            if char in PUNCTUATIONS:
                question_cleaned += " "
            else:
                question_cleaned += char
        return question_cleaned

    def remove_stop_words(self, question):
        """
        Remove any unnecessary words from user's question
        """
        question_cleaned = ""
        for word in question.split():
            if word.lower() in COMMON_WORDS or word.lower() in GREETINGS:
                question_cleaned += " "
            else:
                question_cleaned += word.lower() + " "
        return question_cleaned

    def remove_all(self, question):
        """
        Remove any unnecessary punctuations and/or words
        then trailing whitespaces from user's question
        """
        question_cleaned = self.remove_punctuations(question)
        question_cleaned = self.remove_stop_words(question_cleaned)
        return question_cleaned.strip()
