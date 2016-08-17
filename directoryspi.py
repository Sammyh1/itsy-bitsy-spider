import re
import requests


def Main():
    page_of_site_links = requests.get("http://www.storage.co.uk/find-self-storage/organisations").content
    list_of_links = re.search(r'colspan-4.*<div class="section">', str(page_of_site_links))
    print(list_of_links.group(0))
    individual_link = re.compile(r'<a href="([^>]*)"')
    iterator = individual_link.finditer(list_of_links.group(0))

    for link in iterator:
        individual_directory_url = "http://www.storage.co.uk" + str(link.group(1))
        individual_directory_page_content = requests.get(individual_directory_url).content
        storage_information_string = "," + "," + ","
        name_search = re.search(r'<span class="name">([^<]*)</span>', str(individual_directory_page_content))
        url_search = re.search(r'<a class="url" href="([^"]*)"', str(individual_directory_page_content))
        phone_search = re.search(r'<p><strong>Phone:</strong> <span class="tel">([^<]*)</span>', str(individual_directory_page_content))
        email_search = re.search(r'<p><strong>Email:</strong> <span class="tel">([^<]*)</span>', str(individual_directory_page_content))
        if name_search:
            storage_information_string += str(name_search.group(1) + "," + ",")
        else:
            storage_information_string += "," + ","
        if url_search:
            storage_information_string += str(url_search.group(1) + "," + ",")
        else:
            storage_information_string += "," + ","
        if phone_search:
            storage_information_string += str(phone_search.group(1) + ",")
        else:
            storage_information_string += ","
        if email_search:
            storage_information_string += str(email_search.group(1) + ",")
        else:
            storage_information_string += ","
        print(storage_information_string)
        """
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
        """

Main()
