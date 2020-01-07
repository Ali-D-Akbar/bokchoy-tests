import unittest

from bok_choy.web_app_test import WebAppTest

from pages import PollsIndexPage, PollsDetailPage, PollsResultPage


class TestPolls(WebAppTest):
    def setUp(self):
        """
        Instantiate the page objects.
        """
        super(TestPolls, self).setUp()
        self.polls_index_page = PollsIndexPage(self.browser)
        self.polls_detail_page = PollsDetailPage(self.browser)
        self.polls_result_page = PollsResultPage(self.browser)

    def test_page_existence(self):
        """
        Make sure that the page is accessible.
        """
        import pdb
        pdb.set_trace()
        self.polls_index_page.visit()

    def test_detail_page(self):
        """
        Check if the detail page opens after clicking a question
        """
        self.polls_index_page.visit().click_question('question1')
        assert "What's up?" == self.polls_detail_page.title

    def test_result_page(self):
        """
        Check if the result page opens after voting a question
        """
        self.polls_index_page.visit().click_question('question1')
        self.polls_detail_page.vote_a_question('choice1')

    def test_vote_again(self):
        """
        Check vote_again option in results page
        """
        self.polls_index_page.visit().click_question('question1')
        self.polls_detail_page.vote_a_question('choice1')
        self.polls_result_page.vote_again()
        self.polls_detail_page.vote_a_question('choice2')

    def test_invalid_vote(self):
        """
        make sure that an error message is shown when no choice is selecteddadad
        """
        self.polls_index_page.visit().click_question('question1')
        self.polls_detail_page.q(css='input#vote').click()
        assert "You didn't select a choice." == self.polls_detail_page.vote_error


if __name__ == '__main__':
    unittest.main()
