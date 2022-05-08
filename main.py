import csv
from bs4 import BeautifulSoup
import requests
import json

# Load countries from json
f = open('countries.json')
countries_data = json.load(f)

csvFile = open('The World Factbook Scraped Data.csv', 'w')
writer = csv.writer(csvFile)

for country in countries_data:
    page = requests.get(country["link"])
    soup = BeautifulSoup(page.content, "html.parser")

    # Apply line breaks as new lines
    for br in soup.find_all("br"):
        br.replace_with("\n")

    # Introduction section (get all sub-headings and text, i.e. <h3> and <p>)
    introduction = soup.find(id="introduction")
    if introduction is not None:
        introduction_divs = introduction.find_all("div")

    headings = []
    text_content = []

    for introduction_div in introduction_divs:
        introduction_subheading = introduction_div.find("h3")
        introduction_text = introduction_div.find("p")
        if (all([introduction_subheading, introduction_text])):
            headings.append(introduction_subheading.text)
            text_content.append(introduction_text.text)

    # Geography section
    geography = soup.find(id="geography")
    if geography is not None:
        geography_divs = geography.find_all("div")

    for geography_div in geography_divs:
        geography_subheading = geography_div.find("h3")
        geography_text = geography_div.find("p")
        if (all([geography_subheading, geography_text])):
            headings.append(geography_subheading.text)
            text_content.append(geography_text.text)

    # People and society section
    people = soup.find(id="people-and-society")
    if people is not None:
        people_divs = people.find_all("div")

    for people_div in people_divs:
        people_subheading = people_div.find("h3")
        people_text = people_div.find("p")
        if (all([people_subheading, people_text])):
            headings.append(people_subheading.text)
            text_content.append(people_text.text)

    # Environment section
    environment = soup.find(id="environment")
    if environment is not None:
        environment_divs = environment.find_all("div")

    for environment_div in environment_divs:
        environment_subheading = environment_div.find("h3")
        environment_text = environment_div.find("p")
        if (all([environment_subheading, environment_text])):
            headings.append(environment_subheading.text)
            text_content.append(environment_text.text)

    # Government section
    government = soup.find(id="government")
    if government is not None:
        government_divs = government.find_all("div")

    for government_div in government_divs:
        government_subheading = government_div.find("h3")
        government_text = government_div.find("p")
        if (all([government_subheading, government_text])):
            headings.append(government_subheading.text)
            text_content.append(government_text.text)

    # Economy section
    economy = soup.find(id="economy")
    if economy is not None:
        economy_divs = economy.find_all("div")

    for economy_div in economy_divs:
        economy_subheading = economy_div.find("h3")
        economy_text = economy_div.find("p")
        if (all([economy_subheading, economy_text])):
            headings.append(economy_subheading.text)
            text_content.append(economy_text.text)

    # Energy section
    energy = soup.find(id="energy")
    if energy is not None:
        energy_divs = energy.find_all("div")

    for energy_div in energy_divs:
        energy_subheading = energy_div.find("h3")
        energy_text = energy_div.find("p")
        if (all([energy_subheading, energy_text])):
            headings.append(energy_subheading.text)
            text_content.append(energy_text.text)

    # Communications section
    communications = soup.find(id="communications")
    if communications is not None:
        communications_divs = communications.find_all("div")

    for communications_div in communications_divs:
        communications_subheading = communications_div.find("h3")
        communications_text = communications_div.find("p")
        if (all([communications_subheading, communications_text])):
            headings.append(communications_subheading.text)
            text_content.append(communications_text.text)

    # Transportation section
    transportation = soup.find(id="transportation")
    if transportation is not None:
        transportation_divs = transportation.find_all("div")

    for transportation_div in transportation_divs:
        transportation_subheading = transportation_div.find("h3")
        transportation_text = transportation_div.find("p")
        if (all([transportation_subheading, transportation_text])):
            headings.append(transportation_subheading.text)
            text_content.append(transportation_text.text)

    # Military and security section
    military = soup.find(id="military-and-security")
    if military is not None:
        military_divs = military.find_all("div")

    for military_div in military_divs:
        military_subheading = military_div.find("h3")
        military_text = military_div.find("p")
        if (all([military_subheading, military_text])):
            headings.append(military_subheading.text)
            text_content.append(military_text.text)

    # Terrorism section
    terrorism = soup.find(id="terrorism")
    if terrorism is not None:
        terrorism_divs = terrorism.find_all("div")

    for terrorism_div in terrorism_divs:
        terrorism_subheading = terrorism_div.find("h3")
        terrorism_text = terrorism_div.find("p")
        if (all([terrorism_subheading, terrorism_text])):
            headings.append(terrorism_subheading.text)
            text_content.append(terrorism_text.text)

    # Transnational Issues section
    issues = soup.find(id="transnational-issues")
    if issues is not None:
        issues_divs = issues.find_all("div")

    for issues_div in issues_divs:
        issues_subheading = issues_div.find("h3")
        issues_text = issues_div.find("p")
        if (all([issues_subheading, issues_text])):
            headings.append(issues_subheading.text)
            text_content.append(issues_text.text)

    writer.writerow(['Country'] + headings)
    csvData = [country["country"]] + text_content
    writer.writerow(csvData)


f.close()
csvFile.close()
