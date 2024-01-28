import requests

def get_teams():
    response = requests.get('http://localhost:5000/teams')
    if response.status_code == 200:
        return response.json()
    return []

def get_members(team_name):
    response = requests.get(f'http://localhost:5000/members/{team_name}')
    if response.status_code == 200:
        return response.json()
    return []

def get_member_preferences(member_name):
    response = requests.get(f'http://localhost:5000/preferences/{member_name}')
    if response.status_code == 200:
        return response.json()
    return {}