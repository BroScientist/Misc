import requests
from bs4 import BeautifulSoup

url_list = []
home_url = 'https://www.rottentomatoes.com/top/bestofrt/?year=2019'
threshold = 85
results = {}


def get_soup(url):
    page = requests.get(url)
    page_soup = BeautifulSoup(page.content, 'html.parser')
    return page_soup


soup = get_soup(home_url)
table = soup.find('table', {'class': 'table'})
for url in table.find_all('a', href=True):
    full_url = 'https://www.rottentomatoes.com' + url['href']
    url_list.append(full_url)


def extract_movie_info(movie_url):
    # TODO check release year to get rid of those old-ass movies
    soup = get_soup(movie_url)
    movie_name = soup.find('h1', {'class': 'mop-ratings-wrap__title mop-ratings-wrap__title--top'}).get_text()
    box = soup.find('div', {'class':'mop-ratings-wrap__half audience-score'})
    try:
        audience_score = box.find('span', {'class': 'mop-ratings-wrap__percentage'}).get_text()
        audience_score = int(audience_score.strip().replace('%', ''))
    except Exception:
        audience_score = None
    if audience_score is not None and audience_score >= threshold:
        print(f'{movie_name} - {audience_score}')
        results[movie_name] = audience_score
    # return audience_score


def save_to_csv():
    import csv
    with open('results.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for result in results.items():
            writer.writerow([result[0], result[1]])


def save_to_txt():
    with open('results.txt', 'w') as f:
        for result in results.items():
            f.write(f'{result[0]} - {result[1]}')


soup = get_soup(home_url)
table = soup.find('table', {'class': 'table'})
for url in table.find_all('a', href=True):
    full_url = 'https://www.rottentomatoes.com' + url['href']
    url_list.append(full_url)

for movie_url in url_list:
    extract_movie_info(movie_url)

save_to_csv()
# extract_movie_info('https://www.rottentomatoes.com/m/dark_waters_2019')
# print(results)
# print(sorted(results.items(), key=lambda kv:(kv[1], kv[0])))