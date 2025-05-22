Project Preis-Gau
The project was developed from the ground up with a simple idea in mind:
Enable users who still jot down their grocery lists with pen and paper to effortlessly compare current offers and promotions from nearby supermarkets. By simply taking a photo of their handwritten list, users can discover the best deals available across major German retail chains.

Supported Stores
The following supermarket chains are currently integrated into the system:

Aldi Süd
Aldi Nord
Rewe (via official API)
Edeka
Lidl

Each of these retailers uses a unique and frequently changing data structure for presenting their weekly offers. This poses a particular challenge for consistent parsing and data normalization—especially in the case of Edeka, where structural inconsistencies and errors in their web content make it difficult to extract data reliably.

Technical Overview
OCR Engine: pytesseract is used to convert images of handwritten grocery lists into machine-readable text.

Web Scraping: BeautifulSoup is utilized to scrape product data from all retailer websites except Rewe, which provides access via a public API.

Challenges
Inconsistent Data Formats: Each store presents its data differently, and often changes these formats without notice.

Error-Prone Sources: Especially with Edeka, where malformed HTML or missing information can interrupt the parsing process.

Homogenization Complexity: Creating a unified structure for storage and filtering is non-trivial due to the above challenges.
