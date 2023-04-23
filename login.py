from fbchat import Client
from fbchat.models import *
import pickle
from credential import Credential


def run():
    try:
        with open('fbchat_cookies.pkl', 'rb') as file:
            cookies = pickle.load(file)
        
        c = Credential()
        c.import_credentials()
        # print(c)

        client = Client(c.user, c.password, session_cookies=cookies)

        cookie = client.getSession()
        if cookie != cookies:
            with open('fbchat_cookies.pkl', 'wb') as file:
                pickle.dump(cookie, file)
    except:
        print('An enxception occured.. Check the presence of the cookie and credentials file!')
    finally:
            if client.isLoggedIn():
                return client
            else: return None 
