
from unittest import TestCase

from functions.email import is_correct_email
#
# from tests.assertions import assertEqual, assertTrue, assertFalse
#
#
# assertTrue(is_correct_email("masteraalish@gmail.com"))
# assertTrue(is_correct_email("themonrealstudio@gmail.com"))
#
# assertFalse(is_correct_email("themonrea@lstudio@gmail.com"))
# assertFalse(is_correct_email("@gmail.com"))
# assertFalse(is_correct_email("aidana.yahoo.com”))
class EmailFunctionTestCase(TestCase):
    def test_returns_True_for_correct_email(self):
        self.assertTrue(is_correct_email("masteraalish@gmail.com"))

    def test_returns_True_for_correct_email(self):
        self.assertTrue(is_correct_email("themonrealstudio@gmail.com"))

    def test_returns_False_if_email_have_two_at_signs(self):
        self.assertFalse(is_correct_email("themonrea@lstudio@gmail.com"))

