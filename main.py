from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Basic Idea:
# See what champions have been selected on team and enemy team
# Get lolaytics for list of counters to each champion on enemy team
# Get list of good synergy for each champion on our team
# Get winrate of our own played champions(?) don't know where to get this yet
# Then apply some formula to all of these and then return the best pick
# Later we could also use LOL API to get data in real time


# instantiate options
options = webdriver.ChromeOptions()

# run browser in headless mode
options.add_argument("--headless=new")

# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)
driver.implicitly_wait(0.5)
# load website
url = 'https://lolalytics.com/lol/reksai/build/'

# the url of a specific champ is https://lolalytics.com/lol /champion/build


# get the entire website content
driver.get(url)

# select elements by class name
root = driver.find_element(By.ID, 'root')
elements = driver.find_elements(By.CLASS_NAME, 'Wrapper_small__CiAB2')
print(root)
print(elements)
for text in elements:
    print(text)
