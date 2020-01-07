from bok_choy.page_object import PageObject


class PollsIndexPage(PageObject):
    url = 'http://demo.app:8000/polls/'

    def is_browser_on_page(self):
        return self.q(css='.questions').is_present()

    def click_question(self, question):
        self.q(css='#{} a'.format(question)).click()
        PollsDetailPage(self.browser).wait_for_page()


class PollsDetailPage(PageObject):
    url = None

    def is_browser_on_page(self):
        return self.q(css='input#vote').is_present()

    def select_choice(self, choice):
        self.q(css='#{}'.format(choice)).click()

    def vote(self):
        self.q(css='input#vote').click()
        PollsResultPage(self.browser).wait_for_page()

    def vote_a_question(self, choice):
        self.select_choice(choice)
        self.vote()

    @property
    def title(self):
        return self.q(css='h1').text[0]

    @property
    def vote_error(self):
        return self.q(css='#error strong').text[0]


class PollsResultPage(PageObject):
    url = None

    def is_browser_on_page(self):
        return self.q(css='#vote_again').is_present()

    def vote_again(self):
        self.q(css='#vote_again').click()
        PollsDetailPage(self.browser).wait_for_page()
