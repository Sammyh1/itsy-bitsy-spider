import re
import requests

exclusion_list = []

locations_to_target = ['Birmingham', 'Brighton', 'Bristol Ashton Gate', 'Bristol Central', 'Camberley', 'Cambridge',
                       'Canterbury', 'Cardiff', 'Cheadle and Wilmslow', 'Chelmsford', 'Cheltenham', 'Chester',
                       'Colchester', 'Derby', 'Dundee', 'Edinburgh', 'Gloucester', 'Guildford', 'High Wycombe', 'Hull',
                       'Leeds', 'Liverpool Edge Lane', 'Liverpool North', 'Liverpool South', 'Luton', 'Macclesfield',
                       'Milton Keynes', 'Morecambe', 'Norwich', 'Nottingham', 'Oxford', 'Peterborough', 'Poole',
                       'Portsmouth', 'Reading', 'Sheffield Bramall Lane', 'Sheffield Hillsborough', 'Sheffield Parkway',
                       'Sheffield West Bar', 'Slough', 'Southend', 'Stockport', 'Stockton', 'Stoke', 'Swindon',
                       'Tunbridge Wells', 'Warrington', 'West Molesey']


def Main():
    for location in locations_to_target:
        goog_url = "https://www.google.co.uk/search?q=storage+"
        goog_url += location
        visit_google_url(goog_url, location)


def visit_google_url(url, location):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
    google_page = requests.get(url, headers=headers).content
    sort_of_link = re.compile(r'<a class="rllt__action-button _Jrh" href="([^"]*)')
    iterator = sort_of_link.finditer(str(google_page))
    big_yellow = re.compile(r'bigyellow')
    new_list = [location]
    for match in iterator:
        new_list.append(str(match.group(1)))

    try:
        if not big_yellow.search(new_list[1]):
            print(new_list)

    except:
        pass


'''
start at <a class="rllt__action-button _Jrh">

end when you hit data-ved=







def old_create_google_url():
    search_term = input("Enter a search term")
    num = input("how many URLs do you want crawled?")
    search_term = search_term.split()
    goog_url = "https://www.google.co.uk/search?q="
    while len(search_term) > 1:
        goog_url += (search_term.pop(0) + "+")
    goog_url += (search_term[0] + "&num=%d" % (int(num)))
    return goog_url


def old_Main():
    goog_url = create_google_url()
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
    page_of_google_links = requests.get(goog_url, headers=headers).content
    print(page_of_google_links)
    sort_of_link = re.compile(r'<h3 class="r"><a href="([^"]*)')
    google_ads_format = re.compile(r'googlesyndication')
    iterator = sort_of_link.finditer(str(page_of_google_links))
    final_list = []
    for index, match in enumerate(iterator):
        print("Checking site number: " + str(index + 1) + ', ' + match.group(1))
        try:
            site_to_be_checked = requests.get(match.group(1)).content

            if google_ads_format.search(str(site_to_be_checked)):
                final_list.append(match.group(1))
        except:
            print("Whoops, couldn't find that page")

    print(final_list)

'''
Main()
