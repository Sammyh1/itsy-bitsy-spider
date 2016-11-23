import re
import requests

exclusion_list = []
list_of_sites = []
test_list = []
locations_to_target = ["Birmingham", "Leeds", "Sheffield", "Cornwall", "Bradford", "Manchester", "Co. Durham",
                       "Wiltshire", "Liverpool", "Bristol", "Kirklees", "Barnet", "Croydon", "Cheshire East",
                       "Coventry", "Ealing", "Leicester", "East Riding of Yorkshire", "Cheshire West and Chester",
                       "Wakefield", "Newham", "Enfield", "Bromley", "Lambeth", "Brent", "Wigan", "Wirral", "Sandwell",
                       "Nottingham", "Dudley", "Northumberland", "Wandsworth", "Shropshire", "Southwark", "Doncaster",
                       "Hillingdon", "Lewisham", "Redbridge", "Tower Hamlets", "Newcastle upon Tyne", "Stockport",
                       "Brighton & Hove", "Bolton", "Sunderland", "Medway", "Walsall", "Greenwich",
                       "South Gloucestershire", "Central Bedfordshire", "Sefton", "Haringey", "Waltham Forest",
                       "Hackney", "Hounslow", "Plymouth", "Milton Keynes", "Rotherham", "Hull", "Wolverhampton",
                       "Derby", "Stoke-on-Trent", "Southampton", "Havering", "Harrow", "Salford", "Westminster",
                       "Bexley", "Camden", "Barnsley", "Trafford", "Oldham", "Islington", "Northampton", "Tameside",
                       "Swindon", "Luton", "Rochdale", "Portsmouth", "Solihull", "North Somerset", "Calderdale",
                       "Warrington", "York", "Merton", "North Tyneside", "Barking and Dagenham", "Gateshead", "Sutton",
                       "Stockton-on-Tees", "Richmond upon Thames", "Bournemouth", "Peterborough", "Aylesbury Vale",
                       "Herefordshire", "Bury", "Bath and North East Somerset", "Colchester", "Basildon",
                       "Hammersmith and Fulham", "New Forest", "Southend-on-Sea", "St Helens", "Charnwood", "Wycombe",
                       "Huntingdonshire", "Basingstoke and Deane", "Kingston upon Thames", "Chelmsford",
                       "Telford and Wrekin", "North Lincolnshire", "Bedford", "Thurrock", "South Somerset", "Maidstone",
                       "Reading", "Wokingham", "Canterbury", "Oxford", "North East Lincolnshire",
                       "Kensington and Chelsea", "Harrogate", "Wealden", "West Berkshire", "Arun",
                       "South Cambridgeshire", "Dacorum", "King's Lynn and West Norfolk", "Poole", "Braintree",
                       "South Tyneside", "Windsor and Maidenhead", "Knowsley", "Blackburn with Darwen", "Guildford",
                       "St Albans", "Slough", "Mid Sussex", "Cherwell", "East Hertfordshire", "Reigate and Banstead",
                       "Swale", "Lancaster", "Preston", "Tendring", "Warwick", "Thanet", "Blackpool", "Middlesbrough",
                       "Isle of Wight", "South Kesteven", "Norwich", "East Devon", "East Lindsey", "South Oxfordshire",
                       "Horsham", "Ipswich", "Breckland", "Redcar and Cleveland", "Torbay", "Elmbridge", "Stafford",
                       "North Hertfordshire", "South Norfolk", "Cambridge", "Epping Forest", "Eastleigh", "Teignbridge",
                       "Exeter", "Gloucester", "Newcastle-under-Lyme", "Vale of White Horse", "Broadland", "Halton",
                       "Nuneaton and Bedworth", "Tonbridge and Malling", "Suffolk Coastal", "Ashford", "Amber Valley",
                       "Ashfield", "Waverley", "Havant", "Stratford-on-Avon", "Wychavon", "Test Valley", "Winchester",
                       "Sedgemoor", "Welwyn Hatfield", "Bracknell Forest", "Newark and Sherwood", "Sevenoaks",
                       "East Hampshire", "Chichester", "Cheltenham", "Stroud", "Tunbridge Wells", "Waveney",
                       "East Staffordshire", "Gedling", "Fareham", "Bassetlaw", "Erewash", "Rushcliffe",
                       "Taunton Deane", "Dover", "Chorley", "West Lancashire", "St Edmundsbury", "Broxtowe",
                       "North Kesteven", "Mendip", "Crawley", "South Staffordshire", "Shepway", "Wyre", "South Ribble",
                       "Hinckley and Bosworth", "West Oxfordshire", "Carlisle", "Scarborough", "Worthing", "Mansfield",
                       "Gravesham", "Darlington", "Chesterfield", "Dartford", "South Lakeland", "Rugby",
                       "North Norfolk", "Hertsmere", "Lichfield", "Eastbourne", "Worcester", "West Dorset", "Lewes",
                       "North East Derbyshire", "Mid Suffolk", "Wyre Forest", "Woking", "South Derbyshire", "Fenland",
                       "Great Yarmouth", "Cannock Chase", "Spelthorne", "Staffordshire Moorlands", "Kettering",
                       "North West Leicestershire", "Lincoln", "Allerdale", "Blaby", "Watford", "Broxbourne",
                       "Bromsgrove", "Rushmoor", "Chiltern", "North Devon", "Hart", "Rother", "West Lindsey",
                       "Hartlepool", "Three Rivers", "Hastings", "High Peak", "South Holland", "Pendle", "Hambleton",
                       "East Northamptonshire", "Harborough", "Babergh", "Castle Point", "South Northamptonshire",
                       "East Dorset", "Surrey Heath", "Burnley", "East Cambridgeshire", "Tewkesbury", "Stevenage",
                       "Mole Valley", "Tandridge", "Selby", "Runnymede", "Harlow", "Cotswold", "Rochford", "Uttlesford",
                       "Redditch", "Gosport", "Forest of Dean", "South Hams", "Hyndburn", "Daventry", "Mid Devon",
                       "Epsom and Ewell", "Bolsover", "Fylde", "Wellingborough", "Tamworth", "Brentwood",
                       "Malvern Hills", "Derbyshire Dales", "North Dorset", "Copeland", "Rossendale", "South Bucks",
                       "Barrow-in-Furness", "Boston", "Corby", "Torridge", "Weymouth and Portland", "Forest Heath",
                       "Adur", "North Warwickshire", "Maldon", "Ribble Valley", "Oadby and Wigston", "Craven",
                       "West Devon", "Ryedale", "Eden", "Richmondshire", "Melton", "Christchurch", "Purbeck", "Rutland",
                       "West Somerset", "City of London", "Isles of Scilly"]



def Main():
    for location in locations_to_target:
        print("checking " + location)
        goog_url = "https://www.google.co.uk/search?q=storage+"
        goog_url += location
        visit_google_url(goog_url)
    print(list_of_sites)
    print(test_list)


def visit_google_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'}
    google_page = requests.get(url, headers=headers).content
    sort_of_link = re.compile(r'<h3 class="r"><a href="(https?://w{,3}\.?([^/"]*))')
    iterator = sort_of_link.finditer(str(google_page))
    for match in iterator:
        if str(match.group(1)) not in list_of_sites:
            list_of_sites.append(str(match.group(1)))


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
