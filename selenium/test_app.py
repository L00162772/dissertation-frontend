import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('http://frontend.atu-dissertation.com')
        assert self.driver.title.startswith("React App - ")

