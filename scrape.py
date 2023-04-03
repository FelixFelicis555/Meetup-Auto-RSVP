from bs4 import BeautifulSoup
import requests

def get_events_links(group):
    """
    Input: Links to the groups events page
    
    Output: list of all the links for unregistered events in the corresponding   group
    
    """
    try:
        response = requests.get(group)
        if response.status_code!=200:
            raise Exception
        html_data=BeautifulSoup(response.text,"html.parser")
        events=html_data.select("#attendButton")
        links=[event.get("href") for event in events]
    except Exception:
        return("Invalid status code received")
    except:
        return("An error occurs")
    return links
    