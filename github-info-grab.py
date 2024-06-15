# Adnan Adib
# 15th June, 2014
# 12:57PM
import os as adib
import json
import argparse

intro = '''
 _______  ___   _______  __   __  __   __  _______    ___   __    _  _______  _______ 
|       ||   | |       ||  | |  ||  | |  ||  _    |  |   | |  |  | ||       ||       |
|    ___||   | |_     _||  |_|  ||  | |  || |_|   |  |   | |   |_| ||    ___||   _   |
|   | __ |   |   |   |  |       ||  |_|  ||       |  |   | |       ||   |___ |  | |  |
|   ||  ||   |   |   |  |       ||       ||  _   |   |   | |  _    ||    ___||  |_|  |
|   |_| ||   |   |   |  |   _   ||       || |_|   |  |   | | | |   ||   |    |       |
|_______||___|   |___|  |__| |__||_______||_______|  |___| |_|  |__||___|    |_______|
'''

print(intro)

def get_github_user_info(username):
    command = f"curl -s https://api.github.com/users/{username}"
    result = adib.popen(command).read()
    return json.loads(result)

def print_user_info(user_info):
    keys = [
        "followers_url", "following_url", "gists_url", "starred_url", 
        "subscriptions_url", "organizations_url", "repos_url", 
        "events_url", "received_events_url", "type", "site_admin", 
        "name", "company", "blog", "location", "email", 
        "hireable", "bio", "twitter_username", "public_repos", 
        "public_gists", "followers", "following", "created_at", "updated_at",
        "avatar_url"
    ]
    
    info = {key: user_info.get(key, None) for key in keys}
    print(json.dumps(info, indent=4))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch GitHub user info")
    parser.add_argument('-u', '--username', type=str, required=True, help='github username')
    
    args = parser.parse_args()
    username = args.username
    
    user_info = get_github_user_info(username)
    print_user_info(user_info)
