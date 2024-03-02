import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

user_movie_name = input("Enter movie name: ").lower()  # Convert input to lowercase

res = requests.get(url, headers=headers)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

movie_found = False  # Flag to track whether any movie matches the input name

for tag in soup.findAll('a', {'class': 'ipc-title-link-wrapper'}):
    movie_link = tag.text.strip().lower()  # Convert movie name to lowercase
    movie_name = movie_link.split('. ')[-1]  # Split by '.' and take the second part
    if movie_name == user_movie_name:
        movie_id = tag['href']
        movie_url = f'https://www.imdb.com{movie_id}'
        #print(movie_url)
        movie_found = True  # Set flag to True since movie is found
        break

url2=movie_url
res2 = requests.get(url2, headers=headers)
html2 = res2.text
soup2 = BeautifulSoup(html2, 'html.parser')


#Here we get the director url 
for tag in soup2.findAll('a',{'class':'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'}):
    #print(tag.text.strip())
    director=tag.text.strip()
    id=tag['href']
    dir_url=f'https://www.imdb.com{id}'
    #print(dir_url)
    break

url3=dir_url
res3 = requests.get(url3, headers=headers)
html3 = res3.text
soup3 = BeautifulSoup(html3, 'html.parser')

print("Director: ",director)

#Here we get the similar movies which are directed by the same director
print("Movies you may like: ")
for tag in soup3.findAll('a',{'class':'ipc-primary-image-list-card__title'}):
    m_url1=tag['href']
    m_url=f'https://www.imdb.com{m_url1}'
    print(tag.text.strip())
    print(m_url)



if not movie_found:
    print("Movie not present in top 250.")

    
