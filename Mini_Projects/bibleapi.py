

'''
https://github.com/wldeh/bible-api
'''

import requests
import pandas as pd


def bibleverse(book, chapter, verse):
    
    try:
        book = book.lower().replace(" ", "")
        response = requests.get(f"https://cdn.jsdelivr.net/gh/wldeh/bible-api/bibles/en-bsb/books/{book}/chapters/{str(chapter)}/verses/{str(verse)}.json")
        data = response.json()
        return data["text"]
    except:
        return 'error'


def scripture(book, chapter, verse):
    string = f'{book.capitalize()} {chapter}: {verse}'
    return string



df = pd.read_csv('/Users/steffanlynch/Downloads/christianjournalscriptures.csv')

df['scripture'] = df.apply(lambda x: scripture(x['book'].capitalize(), x['chapter'], x['verse']), axis=1)


df['text'] = df.apply(lambda x: bibleverse(x['book'].capitalize(), x['chapter'], x['verse']), axis=1)
