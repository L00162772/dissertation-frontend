Skip to content
DEV Community
Search...

Log in
Create account

3

3

0

Cover image for Executing Selenium test with python(pytest) using GitHub Actions
DelRayo
DelRayo
Posted on Jan 13

Executing Selenium test with python(pytest) using GitHub Actions
#
github
#
sdet
#
python
#
selenium
DelRayo.tech
You can find the working project Here.

First we are going to create some example tests.
I'll be using selenium with python(pytest).

So for this example ill be creating 2 files one will be called conftest.py and the second one will be test_web01.py

conftest.py in GitHub
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver


@pytest.fixture()
def setup(request):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
    for option in options:
        chrome_options.add_argument(option)

    request.cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


    yield request.cls.driver
    request.cls.driver.close()
Now lets create the second file where the actual tests are.

test_web01.py in GitHub
import pytest


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_title(self):
        self.driver.get('https://www.delrayo.tech')
        assert self.driver.title == "DelRayo.tech - Delrayo Tech"

    def test_title_blog(self):
        self.driver.get('https://www.delrayo.tech/blog')
        print(self.driver.title)

For running with GithubActions we have to create the following file structure on the repo.

-.github
--workflows
---test01.yaml
test01.yaml in GitHub
# .github/workflows/test01.yaml
name: test01
on:
  workflow_dispatch:  
jobs:
  test01:
    runs-on: ubuntu-latest
    steps:
      - name: Check out this repo
        uses: actions/checkout@v2
     #Setup Python   
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install software
        run: sudo apt-get install -y chromium-browser
      - name: Install the necessary packages
        run: pip install requests webdriver-manager selenium pytest
      - name: Run the PytTest script
        run: pytest -rA
Now we just have to go to the actions section on github, select the workflow named test01 and click on the button run workflow.

GitHub Actions

You can configure this workflow to execute on different triggers modifying

on:
  workflow_dispatch:  

With any of these options.

Test Pass with GitHub Actions

You can find the working project Here.

Discussion (2)
Subscribe
pic
Add to the discussion
 
beliaevmaksim profile image
Maksim Beliaev
•
Jun 24

unfortunately, all links are broken


1
 like
Reply
 
delrayo profile image
DelRayo 
•
Jul 19 • Edited on Jul 19

Thanks for the comment.
The links are working now.


1
 like
Reply
Code of Conduct • Report abuse
Read next
dailydevtips1 profile image
Git basics: remove all local branches
Chris Bongers - Jul 12

dailydevtips1 profile image
Git basics: Changing your last commit message
Chris Bongers - Jul 19

yokwejuste profile image
How to build your own LinkedIn Profile Scraper in 2022
Steve Yonkeu - Jul 20

codenameone profile image
Understand the Root Cause of Regressions with Git Bisect
Shai Almog - Jul 19


DelRayo
Follow
WORK
SDET
JOINED
Dec 30, 2021
More from DelRayo
Swipe objects in Appium with C#
#csharp #appium #qa #sdet
Creating a Selenium grid with Docker Compose and run python tests.
#docker #selenium #sdet #python
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver


@pytest.fixture()
def setup(request):
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
    for option in options:
        chrome_options.add_argument(option)

    request.cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


    yield request.cls.driver
    request.cls.driver.close()
DEV Community — A constructive and inclusive social network for software developers. With you every step of your journey.

Built on Forem — the open source software that powers DEV and other inclusive communities.

Made with love and Ruby on Rails. DEV Community © 2016 - 2022.