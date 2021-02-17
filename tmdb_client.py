import requests
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOTQ2YzM5Njk0M2EzM2E2ZTRkNzkzMDkwYTA5NjVkMSIsInN1YiI6IjVmZDNjYTVkYTBiNmI1MDA0MGZhYWNiMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UAILJLxS8FlWFv6m1eMlvm-QDWGClba_bCUHs8huNYA"


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}/{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

print(get_poster_url("/eLT8Cu357VOwBVTitkmlDEg32Fs.jpg"))

def get_movies(how_many, list_type):
    t = list_type
    data = get_movies_list(t)
    return data["results"][:how_many]

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


# do testów
def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list2(list_type):
   return call_tmdb_api(f"movie/{list_type}")

def get_single_movie2(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast2(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")



