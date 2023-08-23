class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if type(value) == int:
            self._page_count = value
        else:
            print("page_count must be an integer")