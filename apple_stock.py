import requests
from bs4 import BeautifulSoup


def scrape_apple_stock():
    url = 'https://finance.yahoo.com/quote/AAPL/history?p=AAPL'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Check if the table can be found
    table = soup.find('table')
    if not table:
        print("No table found on the page.")
        return

    # Print the table for verification
    print(f"Table found: {table}")

    # Find all rows in the table
    rows = table.find_all('tr')[1:]  # Skip header row

    print("Apple Historical Stock Prices:")
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 6:  # Ensure there are enough columns
            date = cols[0].text.strip()
            close_price = cols[4].text.strip()
            if date.lower() != 'dividend' and close_price:
                print(f"Date: {date}, Close Price: {close_price}")


if __name__ == "__main__":
    scrape_apple_stock()
    pass
