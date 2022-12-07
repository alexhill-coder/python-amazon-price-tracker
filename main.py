# Uses the modules BeautifulSoup, requests and smtplib.
from bs4 import BeautifulSoup
import requests
import smtplib

# Sets the email address you want the program to access.
my_email = "emailaddress"

# Sets the password to allow the program to access the account.
password = "emailpassword"

# The url address of the item to be price checked.
item_url = "https://www.amazon.co.uk/Pokemon-Brilliant-Diamond-Nintendo-Switch" \
           "/dp/B096W29KXB/ref=sr_1_25?brr=1&content-id=amzn1.sym.d191d14d-5ea3-" \
           "4792-ae6c-e1de8a1c8780&pd_rd_r=17d4667b-5330-4e49-909c-ec4a7317cfce&pd_" \
           "rd_w=U86Fh&pd_rd_wg=nZddh&pf_rd_p=d191d14d-5ea3-4792-ae6c-e1de8a1c8780&pf_" \
           "rd_r=J2MMTP3Y7S9NDY4D70ZR&qid=1661729545&rd=1&s=videogames&sr=1-25&th=1"

# Provides browser information that might otherwise prevent access to certain websites.
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",

}

# Retrieves the page information
response = requests.get(url=item_url, headers=headers)

# Lets the program know its HTML and retrieves the text.
soup = BeautifulSoup(response.text, "html.parser")

# Retrieves the name section of the product on the page.
find_title = soup.find(name="span", id="productTitle").getText()

# Retrieves the price section of the product on the page.
find_price = soup.find(name="span", id="priceblock_ourprice")

# Retrieves only the price and converts it to a number.
price = float(find_price.getText()[1:])

# Retrieves the title and removes excess information.
title = find_title.strip()

# Checks to see if the price is less than £35.00
if price < 35:

    # Connects with a gmail account.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        # Allows the program to email to a specified address the title, price and url of the item.
        connection.sendmail(from_addr=my_email,
                            to_addrs="sendtoemailaddress",
                            msg=f"Subject:Amazon Price Alert!\n\n{title} is now ${price}.\n{item_url}")
