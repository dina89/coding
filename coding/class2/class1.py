from requests import get

def get_google_site():
    result = get("https://www.google.com")
    print(result)

if __name__ == '__main__':
    get_google_site()