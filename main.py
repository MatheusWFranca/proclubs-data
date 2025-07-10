import requests
import pandas as pd
from datetime import datetime

club_id = 4606176

now = datetime.now().strftime('%Y%m%d')

base_url = 'https://proclubs.ea.com/api/fc'

headers = {
    'sec-ch-ua-platform': '"macOS"',
    'Referer': 'https://www.ea.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
}

def get_club_members():
    params = {
    'platform': 'common-gen5',
    'clubId': '4606176',
    }

    try:
        response = requests.get(f'{base_url}/members/career/stats', params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['members'])
            df.to_csv(f'history/{now}_stats.csv', index=False)
        else:
            print(response.status_code)
    except KeyError:
        print(KeyError)

def get_club_stats():
    params = {
    'platform': 'common-gen5',
    'clubIds': '4606176',
    }
    
    try:
        response = requests.get(f'{base_url}/clubs/info', params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame.from_dict(data[str(club_id)]['customKit'], orient='index', columns=['value'])
            df.to_csv(f'history/{now}_club_stats.csv', index=True)
        else:
            print(response.status_code)
    except NameError:
        print(NameError)

def get_club_overall_stats():
    params = {
    'platform': 'common-gen5',
    'clubIds': '4606176',
    }

    try:
        response = requests.get(f'{base_url}/clubs/overallStats', params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df = df.T
            df.to_csv(f'history/{now}_club_overral_stats.csv', index=True)
        else: 
            print(response.status_code)
    except NameError:
        print(NameError)

def get_members_detailed_stats():
    params = {
        'platform': 'common-gen5',
        'clubId': '4606176',
    }

    try:
        response = requests.get(f'{base_url}/members/stats', params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['members'])
            df.to_json(f'history/{now}_members_detailed_stats.json', orient='records', indent=2, index=False)
        else: 
            print(response.status_code)
    except NameError:
        print(NameError)

def get_lastest_games():
    params = {
        'platform': 'common-gen5',
        'clubIds': '4606176',
        'matchType': 'leagueMatch',
        'maxResultCount': '100',
    }

    try:
        response = requests.get(f'{base_url}/clubs/matches', params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df.to_json(f'history/{now}_get_latest_games.json', orient='records', indent=2, index=False)
        else: 
            print(response.status_code)
    except NameError:
        print(NameError)

def main():
    get_club_members()
    get_club_stats()
    get_club_overall_stats()
    get_members_detailed_stats()
    get_lastest_games()

if __name__ == "__main__":
    main()