from bs4 import BeautifulSoup
import requests
from flask import render_template, Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def get_news():
    url = "https://finance.yahoo.com/news"

    response = requests.get(url)
    stock_price_detail = response.text

    stock_price_detail_soup = BeautifulSoup(stock_price_detail, 'html.parser')

    a_tags = stock_price_detail_soup.select(selector='.content')

    title_links = []
    title_text = []

    for tag in a_tags:
        first_tag = tag.select_one(' .content a')
        if first_tag:
            title_links.append(first_tag.get('href',''))
            title_text.append(first_tag.get('title',''))

    print(f"text:{len(title_text)} | title:{len(title_links)}")

    return render_template('index.html', links=title_links, texts=title_text)


if __name__ == '__main__':
    app.run(debug=True)
