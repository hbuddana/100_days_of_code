from bs4 import BeautifulSoup
import requests

# Send a request to the Hacker News webpage
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

# Parse the webpage content
soup = BeautifulSoup(yc_webpage, "html.parser")

# Lists to store titles, links, and upvotes
titles = []
links = []
upvotes = []

# Find all articles and their subtexts
articles = soup.find_all(name="span", class_="titleline")
subtexts = soup.find_all(name="td", class_="subtext")

# Loop through articles to populate the lists
for i in range(len(articles)):
    # Extract the title and link
    title = articles[i].find("a").getText()
    link = articles[i].find("a")["href"]
    
    # Extract the upvotes (handle missing scores)
    upvote_span = subtexts[i].find(name="span", class_="score")
    upvote = upvote_span.getText().split()[0] if upvote_span else "0"  # Extract only the number part
    
    # Append to respective lists
    titles.append(title)
    links.append(link)
    upvotes.append(int(upvote))  # Convert to integer for further processing

# Print the lists
print("Titles:", titles)
print("Links:", links)
print("Upvotes:", upvotes)



