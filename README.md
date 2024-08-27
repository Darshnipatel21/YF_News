## Yahoo Finance News Scraper
This project is a simple web application built using Flask that scrapes news headlines from the Yahoo Finance website and displays them on a web page. The app uses BeautifulSoup for web scraping and Flask-Bootstrap for styling.

## Features
1. Scrapes the latest news headlines from Yahoo Finance.
2. Displays the headlines as clickable links on the homepage.
3. Utilizes Flask-Bootstrap for a responsive design.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- pip (Python package installer) is available.

## Installation
Clone the Repository

```bash
git clone https://github.com/yourusername/yahoo-finance-news-scraper.git
cd yahoo-finance-news-scraper
```

## Create and Activate a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install the Required Packages

```bash
pip install -r requirements.txt
```

# Content of requirements.txt:

```makefile
Flask==2.0.1
Flask-Bootstrap==3.3.7.1
requests==2.26.0
beautifulsoup4==4.9.3
```

## Usage
Run the Application

```bash
python app.py
```

Access the Application Open your web browser and navigate to **http://127.0.0.1:5000/**. You should see a list of the latest Yahoo Finance news headlines.

## File Structure
- **app.py:** The main Flask application file.
- **templates/index.html:** The HTML template for rendering the news headlines.
- **requirements.txt:** Contains the list of dependencies required to run the application.
- **README.md:** This file.

## Troubleshooting
If you encounter any issues:

Ensure that you are connected to the internet, as the app requires access to Yahoo Finance to fetch the news.
Verify that all required Python packages are installed.

## Contributing
Contributions are welcome! Please fork this repository, create a new branch for your feature or bug fix, and submit a pull request.


