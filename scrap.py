from bs4 import BeautifulSoup
import requests
import csv
import json
import re
import xml.etree.ElementTree as ET

categories = ['politics', 'economy', 'international', 'culture']
article_types = ['report', 'analysis']

csv_file = open('cms_scrape.csv', 'w', newline='', encoding='utf-8')
articles_data = []

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['category', 'headline', 'summary', 'video_link', 'author', 'date'])

BASE_URL = 'https://thepressproject.gr/category/'

#source = requests.get('https://thepressproject.gr/article_type/report/').text
for category in categories:
    URL = f"{BASE_URL}{category}/"
    source = requests.get(URL).text
    print(URL)
    soup = BeautifulSoup(source, 'lxml')

    for article in soup.find_all('article'):
        headline = article.h3.a.text
        print('Title', headline)

        summary = article.find('div', class_='entry-content').p.text if article.find('div', class_='entry-content').p else 'Venceremos' #
        print('Summary', summary)

        #author_span = article.find('label', class_='tpp-author').span
        #author = author_span.text if author_span else 'TPP'

        author_span = article.find('label', class_='tpp-author')
        author = author_span.span.text if author_span else 'TPP'  # Assign 'TPP' if author_span is None

        print('Author:', author)

        publication_date_tag = article.find('div', class_='archive-info')
        publication_date_text = publication_date_tag.text.strip() if publication_date_tag else 'No date'

        # Define a regular expression pattern to match the date format
        date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'

        # Find all occurrences of the date pattern in the publication date text
        date_matches = re.findall(date_pattern, publication_date_text)

        # If there are matches, take the first one
        if date_matches:
            publication_date = date_matches[0]
        else:
            publication_date = None

        print("Publication Date:", publication_date)


        try:
            vid_src = article.find('iframe', class_='youtube-player')['src']

            vid_id = vid_src.split('/')[4]
            vid_id = vid_id.split('?')[0]

            yt_link = f'https://youtube.com/watch?v={vid_id}'
        except Exception as e:
            yt_link = None

        print(yt_link)

        # Append article data to the list
        articles_data.append({
            'category': category,
            'headline': headline,
            'summary': summary,
            'author': author,
            'publication_date': publication_date,
            'youtube_link': yt_link
        })

        print()

        csv_writer.writerow([category, headline, summary, yt_link, author, publication_date])

csv_file.close()

with open('cms_scrape.json', 'w') as json_file:
    json.dump(articles_data, json_file, indent=4)

NEW_URL = "https://thepressproject.gr/radio_show/radio-venceremos/"
source = requests.get(NEW_URL).text
print(NEW_URL)
soup = BeautifulSoup(source, 'lxml')

links = []

for article in soup.find_all('h3', class_='art-title'):
    headline = article.a.text
    link = article.a['href']
    print('Radio:', headline)
    print('Link:', link)
    links.append(link)

print("List of links:", links)

# Iterate through each URL and extract Mixcloud links

root = ET.Element("MixcloudLinks")

# Initialize mixcloud_links outside the loop to accumulate all links
mixcloud_links = []

# Iterate through each URL and extract Mixcloud links
for link in links:
    print("Parsing:", link)
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')

    # Find all <iframe> elements with class 'mixcloud-player'
    iframe = soup.find('div', id='maintext').find('iframe')
    
    if iframe:
        # Extract the 'src' attribute, which contains the Mixcloud link
        mixcloud_link = iframe['src']
        mixcloud_links.append(mixcloud_link)

# Create a subelement for each Mixcloud link under the root element
for mixcloud_link in mixcloud_links:
    link_element = ET.SubElement(root, "Link")
    link_element.text = mixcloud_link + "\n"  # Add newline character after each link

# Create an XML tree from the root element
tree = ET.ElementTree(root)

# Write the XML tree to a file
tree.write("mixcloud_links.xml")


