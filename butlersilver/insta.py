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

        insta_ids = [node['code'] for node in insta_json['entry_data']['ProfilePage'][0]['user']['media']['nodes']]

        return insta_ids

    except:

        insta_ids = [u'BVaXPHqFx_S',
         u'BVFbTP5Fupy',
         u'BVA7ngyFmdv',
         u'BUvQqjQllm9',
         u'BUKwMl-l-yW',
         u'BTmozaFFinr',
         u'BTfLlaIFEkO',
         u'BSw7yuwgcvQ',
         u'BSmaS56DCaz',
         u'BSmXPSnDEt2',
         u'BSef4H_ASUs',
         #u'BR9ta90gUWM',
         u'BRt2otYAiIv',
         u'BReYEnGjGiY',
         u'BRWY1MxDUhe',
         u'BQvdvhNDIUA',
         u'BQEtLszg7qV',
         u'BQBG0Pih6nA',
         u'BPvoDlLhrpt',
         u'BPtEPCyhbLb',
         u'BPoAujNhUaw',
         u'BPfQniwhHm_',
         u'BPVxe8yBVSL',
         u'BPVufKSBn1b',
         u'BPGZmHihMAX',
         u'BOs6i3ihqkl']
        return insta_ids
