import requests
from bs4 import BeautifulSoup
amt_of_rounds = int(input("Enter the number of countries you want: "))   #to extract this amount of countries from the table

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)               #passing url in request.get to get the html of the page and header to prove that bot is not seeking for data
soup = BeautifulSoup(response.text, "html.parser")          #converting response into processable html data using beautifulsoup

gdp_table = soup.find("table", class_="wikitable")          #to extract the gdp table under response 
rows = gdp_table.find_all("tr")                             #to find the rows under gdp table
count = 0                                                   #to keep a check that only number entered by user countries follow
for row in rows[1: ]:                                      #skip header row
    count += 1                                              
    columns = row.find_all("td")                           #to find columns under row
    if len(columns) > 1:
        country_col = columns[0]                           #country is located on index 0 as per gdp table's visualisation....
        gdp_col = columns[1]                               #gdp(IMF) is located at index 1 as per gdp table's visualisation....

        country_link = country_col.find("a")               #finding the country link
        if country_link:
            country_name = country_link.text.strip()
            gdp_text = gdp_col.text.strip() if gdp_col else "N/A"
            print(f"Country: {country_name} \n GDP in millions USD: {gdp_text}\n Position: {count}\n")     #printing the final data
            if count == amt_of_rounds:                      #if country number reached the amount given by user, the programe breaks
                break
