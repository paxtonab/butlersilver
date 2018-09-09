import json
import requests
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()


def get_latest_insta():
    """
    Helper function to get the latest instagram posts from @butlersiver

    :ret : insta_ids list of unique id's of 12 most recent insta posts
    """
    try:
        r  = requests.get("https://www.instagram.com/butlersilver/")
        data = r.text

        insta_text = data.split('window._sharedData =')[1].split(';')[0]
        insta_json = json.loads(insta_text)

        edges = [node for node in insta_json['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']]
        insta_ids = [node['node']['shortcode'] for node in edges]

        return insta_ids

    except:
        insta_ids = [u'Bm5xihGH-5y', u'BlRlDmRn8_z', u'BlQkPIRnYun', u'BlMDbqXl4-f', u'BlEUzH4HUxb', u'BkF-5qQn8An', u'BkF9SzlnCQE', u'Bi0FDbvnULU', u'BipxdfEnaim', u'Bg592nnBMGm', u'BgZky1Phqfs', u'BftJVe0Foag']
        return insta_ids
