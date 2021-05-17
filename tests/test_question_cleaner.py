
from grand_py_app.utils.question_cleaner import QuestionCleaner


class TestQuestionCleaner:

    cleaner = QuestionCleaner()

    def test_remove_punctuations(self):
        question = """Hey!How are you doing?(Parenthesis)-[Array];{Curly brackets}:"This is a test",'clearly'.<>/@#$%^&*_~"""
        assert self.cleaner.remove_punctuations(question) == """Hey How are you doing  Parenthesis   Array   Curly brackets   This is a test   clearly              """

    def test_remove_stop_words(self):
        question = "Salut bot tu vas bien ? Parle moi de la Tour Eiffel stp ?!"
        assert self.cleaner.remove_stop_words(question) == "     ?     tour eiffel  ?! "

    def test_remove_all(self):
        question = "Salut bot, tu vas bien ? Parle moi de la Tour Eiffel stp ?!"
        assert self.cleaner.remove_all(question) == "tour eiffel"
