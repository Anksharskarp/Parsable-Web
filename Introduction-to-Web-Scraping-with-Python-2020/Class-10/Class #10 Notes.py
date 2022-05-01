from bs4 import BeautifulSoup
import requests
import pandas
import matplotlib.pyplot as plt #'plt' is short for plot
#We will be creating a histogram with matplotlib...
addresses = []
prices = []
numBeds = []


for i in range(0, 5):
    try:
        url = "https://www.century21.com/real-estate/carmel-in/LCINCARMEL/?s={}".format(i*20)
        # In this case, we add the 'i*20' because the end of the url goes up by 20s

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        houses = soup.find_all('div', class_="property-card-primary-info")

        for house in houses:
            address = house.find('div', class_="property-address").text
            address = address.replace('\n', '')

            price = house.find('a', class_="listing-price").text
            price = price.replace('\n', '')
            price = price.replace('$', '')
            price = price.replace(',', '')

            beds = house.find('div', class_="property-beds")
            #Exception handling if the number of beds is inavailable, resulting in an attributeError for the text
            if (beds == None):
                beds = 'N/A'
            else:
                beds = beds.text
            beds = beds.replace('\n', '')

            addresses.append(address)
            prices.append(int(price))
            numBeds.append(beds)
    except:
        print("An exception occured during parsing.")

housesdf = pandas.DataFrame(
    {
        'Address': addresses,
        'Price': prices,
        'Number of Bedrooms': numBeds
    })
print(housesdf)
housesdf.to_csv('carmelHouses.csv')
# Code for price histogram
housesdf.hist(column="Price")
housesdf.plot.bar() #Shows for every single house.
plt.show()
