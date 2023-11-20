import requests
from bs4 import BeautifulSoup
import csv

# Specify the URL of the website
urls = [
"https://jakxp.com/product/1740/Brother-TZ-221-P-touch-Label-Tape-9mm-38-Black-on-White",
"https://jakxp.com/product/7890/XPrex-Label-Tape-Use-for-Dymo-A18055-Black-on-White-12mm-HS-Tube",
"https://jakxp.com/product/7900/XPrex-Label-Tape-Use-for-Dymo-A18057-Black-on-White-19mm-HS-Tube",
"https://jakxp.com/product/7640/XPrex-Label-Tape-Use-for--Brother-DK-11201--29mm--400pcs",
"https://jakxp.com/product/1010/Printer-Ribbon-for-OKI-182--320--321--390-Black",
"https://jakxp.com/product/7500/Brother-TZ-242-P-touch-Label-Tape-18mm-Red-on-White",
"https://jakxp.com/product/8650/Xprex-Barcode-Ribbon-45mm-x-300m",
"https://jakxp.com/product/7470/Brother-TZ-135-P-touch-Label-Tape-12mm-White-on-Clear",
"https://jakxp.com/product/7460/Brother-MK-631-Label-Black-on-Yellow-12mm",
"https://jakxp.com/product/980/XPrex-Brother-Ribbon-AX10-Compatible",
"https://jakxp.com/product/1690/Epson-Ribbon-DFX9000",
"https://jakxp.com/product/1760/Brother-TZ-232-P-touch-Label-Tape-12mm-12-Red-on-White",
"https://jakxp.com/product/800/OKI-Ribbon-for-Microline-182-and-3320",
"https://jakxp.com/product/7590/Casio-XR-9WE1-Label-Printer-9mm--White",
"https://jakxp.com/product/1020/Xprex-Barcode-Ribbon-110mm-x-300m",
"https://jakxp.com/product/7860/XPrex-Label-Tape-Use-for-Dymo-45803-Black-on-White--19mm",
"https://jakxp.com/product/7880/XPrex-Label-Tape-Use-for-Dymo--A1805443-Black-on-White--24mm-HS-Tube",
"https://jakxp.com/product/1790/Brother-TZ-631-P-touch-Label-Tape-12mm-12-Blak-on-Yellow",
"https://jakxp.com/product/1780/Brother-TZ-621-P-touch-Label-Tape-9mm-38-Black-on-Yellow",
"https://jakxp.com/product/7480/Brother-TZ-141-P-touch-Label-Tape-18mm-Black-on-Clear",
"https://jakxp.com/product/7720/XPrex-Label-Tape-Use-for-Brother-TZ-222-Red-on-White-9mm",
"https://jakxp.com/product/7700/XPrex-Label-Tape-Use-for-Brother-DK-211-Black-on-White-6mm",
"https://jakxp.com/product/7530/Brother-TZ-561-P-touch-Label-Tape-36mm-Black-on-Blue",
"https://jakxp.com/product/7540/Brother-TZ-611-P-touch-Label-Tape-6mm-Black-on-Yellow",
"https://jakxp.com/product/7730/XPrex-Label-Tape-Use-for-Brother-TZ-232-Red-on-White-12mm",
"https://jakxp.com/product/1820/Dymo-45010-D1-Tape12mm-x-7m-Black-on-Transparent",
"https://jakxp.com/product/7680/XPrex-Label-Tape-Use-for-Brother-DK-231-Black-on-White-12mm",
"https://jakxp.com/product/7910/XPrex-Label-Tape-Use-for-Dymo-A40913-Black-on-White--9mm",
"https://jakxp.com/product/7710/XPrex-Label-Tape-Use-for-Brother-TZ-221-Black-on-White-9mm",
"https://jakxp.com/product/7690/XPrex-Label-Tape-Use-for-Brother-TZ-131-Black-on-Clear-12mm",
"https://jakxp.com/product/7610/Dymo-45016-D1-Tape-Label-12mm-x-7m-Black-on-Blue",
"https://jakxp.com/product/7760/XPrex-Label-Tape-Use-for-Brother-TZ-551-Black-on-Blue-24mm",
"https://jakxp.com/product/840/Brother-TZ-131-P-touch-Label-Tape-12mm-12-Black-on-Clear",
"https://jakxp.com/product/830/Brother-TZ-121-P-touch-Label-Tape-9mm-38-Black-on-Clear",
"https://jakxp.com/product/7520/Brother-TZ-435-P-touch-Label-Tape-12mm-White-on-Red",
"https://jakxp.com/product/7650/XPrex-Label-Tape-Use-for-Brother-DK-11204--17mm-400pcs",
"https://jakxp.com/product/7870/XPrex-Label-Tape-Use-for-Dymo--A18051-Black-on-White-6mm",
"https://jakxp.com/product/1730/Brother-TZ-211-P-touch-Label-Tape-6mm-14-Black-on-White",
"https://jakxp.com/product/7660/XPrex-Label-Tape-Use-for-Brother-DK-22205-62mm-400pcs",
"https://jakxp.com/product/860/Dymo-Rhino-1848918759-Flexible-Nylon-Tape-19mm-x-35---Black-on-White",
"https://jakxp.com/product/1830/Dymo-45013-D1-Tape12mm-x-7m-Black-on-white",
"https://jakxp.com/product/7750/XPrex-Label-Tape-Use-for-Brother-TZ-251-Black-on-White-24mm",
"https://jakxp.com/product/850/Casio-XR-12WE1-EZ-Label-Printer-12mm-x-8m-Black-on-White",
"https://jakxp.com/product/8630/Xprex-Barcode-Ribbon-110mm-x-74m",
"https://jakxp.com/product/1710/Epson-Ribbon-Cartridge-LQ590",
"https://jakxp.com/product/7770/XPrex-Label-Tape-Use-for-Brother-TZ-621-Black-on-Yellow-9mm",
"https://jakxp.com/product/7670/XPrex-Label-Tape-Use-for-Brother-DK-221-Black-on-White-29mm",
"https://jakxp.com/product/1750/Brother-TZ-231-P-touch-Label-Tape-12mm-12-Black-on-White",
"https://jakxp.com/product/1000/XPrex-Erc-27-Black-Compatible",
"https://jakxp.com/product/7830/XPrex-Label-Tape-Use-for-Casio-AR-9WE-Black-on-White-9mm",
"https://jakxp.com/product/8620/Xprex-Barcode-Ribbon-110mm-x-450m",
"https://jakxp.com/product/7930/XPrex-Label-Tape-Use-for-Dymo-A45018-Black-on-Yellow-12mm",
"https://jakxp.com/product/8670/Xprex-Barcode-Ribbon-55mm-x-91m",
"https://jakxp.com/product/1700/Epson-Ribbon-Cartridge-LQ350",
"https://jakxp.com/product/1770/Brother-TZ-241-P-touch-Label-Tape-18mm-34-Black-on-White",
"https://jakxp.com/product/7790/XPrex-Label-Tape-Use-for-Brother-TZ-641-Black-on-Yellow-18mm",
"https://jakxp.com/product/7600/Dymo-40910-D1--Tape-Label--9mm-x-7m--Black-on-Transparent",
"https://jakxp.com/product/7800/XPrex-Label-Tape-Use-for-Brother-TZ-651-Black-on-Yellow-24mm",
"https://jakxp.com/product/7570/Brother-TZ-661-P-touch-Label-Tape-36mm-Black-on-Yellow",
"https://jakxp.com/product/8610/Xprex-Barcode-Ribbon-106mm-x-300m",
"https://jakxp.com/product/1800/Brother-TZ-251-P-touch-Label-Tape-24mm-1-Black-on-White",
"https://jakxp.com/product/7920/XPrex-Label-Tape-Use-for-Dymo-A43613-Black-on-White-6mm",
"https://jakxp.com/product/910/XPrex-Labelling-Tape-Brother-M-M-K-621-Tape--BlackYellow-9-mm",
"https://jakxp.com/product/7630/Dymo-45803-D1-Tape19mm-x-7m-Black-on--White",
"https://jakxp.com/product/930/Xprex-A18053--Dymo-Rhino-Industrial-Heat-Shrink-Tube-Black-on-White-9mm-Label-Tape-Compatible",
"https://jakxp.com/product/4000/XPrex-Labelling-Tape-Brother--HSe-231-Heat-Shrink-Tube-Tape-Cassette--Black-on-White-117mm-wide",
"https://jakxp.com/product/7840/XPrex-Label-Tape-Use-for-Dymo-18489-18759-Black-on-White-19mm-FLexible-Nylon",
"https://jakxp.com/product/7740/XPrex-Label-Tape-Use-for-Brother-TZ-241-Black-on-White-18mm",
"https://jakxp.com/product/1720/Epson-Ribbon-Cartridge-LQ690",
"https://jakxp.com/product/7580/Casio-XR-6GN1--Label-Printer-6mm",
"https://jakxp.com/product/7940/XPrex-Labelworks-Use-For-Epson-AS9KW--Black-on-White-12mm",
"https://jakxp.com/product/8640/Xprex-Barcode-Ribbon-40mm-x-91m",
"https://jakxp.com/product/8660/Xprex-Barcode-Ribbon-55mm-x-74m",
"https://jakxp.com/product/940/XPrex-Epson-Labelworks-AS12KW-Label-Tape-Cartridge-Black-On-Clear-12mmx8m-Compatible",
"https://jakxp.com/product/7780/XPrex-Label-Tape-Use-for-Brother-TZ-631-Black-on-Yellow-12mm",
"https://jakxp.com/product/7510/Brother-TZ-261-P-touch-Label-Tape-36mm-Black-on-White",
"https://jakxp.com/product/810/Fargo-45200-YMCKO-Full-Color-Ribbon-for-DTC4500-Series-ID-Card-Printers",
"https://jakxp.com/product/790/Epson-Ribbon-Cassette-ERC--27B-Black",
"https://jakxp.com/product/7820/XPrex-Label-Tape-Use-for-Casio--AR12WE-Black-on-White-12mm",
"https://jakxp.com/product/920/Xprex-Casio-label-tape-XR-12YW-Black-on-Yellow-12mm--Compatible",
"https://jakxp.com/product/7550/Brother-TZ-641-P-touch-Label-Tape-18mm-Black-on-Yellow",
"https://jakxp.com/product/7490/Brother-TZ-222-P-touch-Label-Tape--9mm-Red-on--White",
"https://jakxp.com/product/7850/XPrex-Label-Tape-Use-for-Dymo-40918-Black-on-Yellow-9mm",
"https://jakxp.com/product/7560/Brother-TZ-651-P-touch-Label-Tape-24mm-Black-on-Yellow",
"https://jakxp.com/product/7810/XPrex-Label-Tape-Use-for-Brother-TZ-751-Black-on-Green-24mm",
"https://jakxp.com/product/7450/Brother-MK-621-Label-Black-on-Yellow-9mm",
"https://jakxp.com/product/870/Receipt-Printer-Rolls-80mm-x-80mx-12-core-Thermal--1pc",
"https://jakxp.com/product/1840/Dymo-53713-D1-Tape-24mm-x-7m-Black-on-White",
"https://jakxp.com/product/7620/Dymo-45018-D1-Tape12mm-x-7m-Black-on-Yellow",
"https://jakxp.com/product/1810/Dymo-40913-D1-Standard-Tape-9mm-x-7m---Black-on-White"
]

# Specify the CSV file name


csv_file = '/Users/adityamaindan/Desktop/Dadas/Ribbons&Tapes.csv'

# Write headers to the CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Brand', 'Code', 'Price', 'Description', 'URL', 'Image'])

    # Loop through each URL
    for url in urls:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Specify the class names for the different parts (adjust based on the structure of the website)
            part1_class = "tiheading"
            part2_class = "ttext"
            part3_class = "tpropricedet mb-3"
            part4_class = "tproheading"
            part6_class = "show-img"

            # Extract data from the different parts
            data_part1 = soup.find('h1', class_=part1_class).text.strip() if soup.find('h1', class_=part1_class) else ''
            data_part2 = soup.find('p', class_=part2_class).text.strip() if soup.find('p', class_=part2_class) else ''
            data_part3 = soup.find('p', class_=part3_class).text.strip() if soup.find('p', class_=part3_class) else ''
            data_part4 = soup.find('p', class_=part4_class).text.strip() if soup.find('p', class_=part4_class) else ''
            data_part5 = url
            data_part6 = soup.find('img', id=part6_class).get('src') if soup.find('img', id=part6_class) else ''

            # Write data row-wise
            csv_writer.writerow([data_part1, data_part2, data_part3, data_part4, data_part5, data_part6])
            print(f'Data from {url} has been written to {csv_file}')
        else:
            print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
