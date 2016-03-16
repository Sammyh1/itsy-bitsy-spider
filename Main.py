import re
import requests

def create_google_url():
    search_term = input("Enter a search term")
    search_term = search_term.split()
    goog_url = "https://www.google.co.uk/search?q="
    while len(search_term) > 1:
        goog_url += (search_term.pop(0) + "+")
    goog_url += (search_term[0] + "&num=30")
    return goog_url


def Main():
    goog_url = create_google_url()
    page_of_google_links = requests.get(goog_url).content
    sort_of_link = re.compile(r'<a href="/url\?q=([^&]{,200})')
    google_ads_format = re.compile(r'googlesyndication')
    iterator = sort_of_link.finditer(str(page_of_google_links))
    final_list = []
    count = 0
    for match in iterator:
        print("Checking site number: " + str(count) +", " + match.group(1))
        count += 1
        site_to_be_checked = requests.get(match.group(1)).content
        if google_ads_format.search(str(site_to_be_checked)):
            final_list.append(match.group(1))

    print(final_list)

Main()