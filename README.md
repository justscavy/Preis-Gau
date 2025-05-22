## Project Preis-Gau

**Project Preis-Gau** was developed from scratch with a simple idea:  
Allow users who still write their grocery lists with pen and paper to take a photo and instantly compare offers and promotions from nearby supermarkets.

By leveraging OCR and data scraping, the project enables quick and convenient price comparisons across several major German retailers.

## Supported Stores

The following supermarkets are currently integrated into the system:

- **Aldi Süd**
- **Aldi Nord**
- **Rewe**
- **Edeka**
- **Lidl**

## Technical Stack

- **OCR**: [pytesseract](https://github.com/madmaze/pytesseract) is used to convert handwritten lists into text.
- **Web Scraping**: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) is used to extract offer data from store websites (except Rewe).
- **API Integration**: Rewe provides an API, which is used to fetch structured offer data directly.

## Key Challenges

- **Inconsistent Data Structures**: Each store formats its data differently and frequently changes these formats, requiring constant adjustments.
- **Faulty Data (Edeka)**: Edeka’s data often includes structural errors or inconsistencies, making reliable extraction difficult.
- **Data Homogenization**: Unifying the scraped and parsed data into a consistent format for filtering and storage is a non-trivial task due to the varying data sources.

## Future Goals

- Improve OCR accuracy for handwritten lists.
- Build a robust data normalization pipeline.
- Add more stores and support international retailers.
- Create a user-friendly front-end for broader accessibility.
