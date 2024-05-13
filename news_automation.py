from sys import argv

API_KEY = 'd25cc0bde2cd4aeca732c66175bcc2d9'

URL = ('https://newsapi.org/v2/top-headlines?')

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

if __name__ == "--main__":
    print(f"Getting news for you {argv[1]}...\n")
    get_articles_by_category(argv[1])
    print(f"Successfully retrieved top {argv[1]} headlines")
