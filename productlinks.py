import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def is_product_link(url):
    # You can customize this function based on your understanding of product URLs
    return "/product/" in url

def get_product_links(url_list):
    product_links = set()
    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                links = {urljoin(url, a['href']) for a in soup.find_all('a', href=True)}
                product_links.update(filter(is_product_link, links))
            else:
                print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error during the request: {e}")

    return product_links

# Given URLs
urls = [
"https://jakxp.com/product-category/130/190/570/Ribbons-Tapes",
"https://jakxp.com/product-category/130/190/580/Ribbons-Tapes",
"https://jakxp.com/product-category/130/190/590/Ribbons-Tapes",
"https://jakxp.com/product-category/130/210/650/Ribbons-Tapes",
"https://jakxp.com/product-category/130/210/660/Ribbons-Tapes",
"https://jakxp.com/product-category/130/210/670/Ribbons-Tapes",
"https://jakxp.com/product-category/130/210/690/Ribbons-Tapes",
"https://jakxp.com/product-category/130/220/700/Ribbons-Tapes",
"https://jakxp.com/product-category/130/220/710/Ribbons-Tapes",
"https://jakxp.com/product-category/130/220/720/Ribbons-Tapes",
"https://jakxp.com/product-category/130/220/740/Ribbons-Tapes",
"https://jakxp.com/product-category/130/230/780/Ribbons-Tapes",
"https://jakxp.com/product-category/130/230/790/Ribbons-Tapes",
"https://jakxp.com/product-category/130/230/800/Ribbons-Tapes",
"https://jakxp.com/product-category/130/230/810/Ribbons-Tapes"
]


# Get unique product links
unique_product_links = get_product_links(urls)

# Print unique product links in a readable format
print("Product Links:")
for link in unique_product_links:
    print(link)
