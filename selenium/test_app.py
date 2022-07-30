import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('http://https://frontend.atu-dissertation.com')
        assert self.driver.title == "DelRayo.tech - Delrayo Tech"

    def test_title_blog(self):
        self.driver.get('http://https://frontend.atu-dissertation.com')
        print(self.driver.title)
