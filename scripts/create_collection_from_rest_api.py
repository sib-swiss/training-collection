import requests
from requests.auth import HTTPBasicAuth
import sys

r = requests.get("https://glittr.org/api/repositories",
                    auth=HTTPBasicAuth('user', 'pw'))

data_dict = r.json()['data']

collection_dict = {}
for repo in data_dict:
    category = repo['tags'][0]['category']
    topic = repo ['tags'][0]['name']
    if category not in collection_dict.keys():
        collection_dict[category] = {}
        collection_dict[category][topic] = [repo]
    else:
        if topic in collection_dict[category].keys():
            collection_dict[category][topic].append(repo)
        else:
            collection_dict[category][topic] = [repo]

for category in collection_dict.keys():
    sys.stdout.write(f"- [{category}](#{category.lower().replace(' ', '-')})\n")
    for topic in collection_dict[category].keys():
        sys.stdout.write(f"  - [{topic}](#{topic.lower().replace(' ', '-')})\n")

for category in collection_dict.keys():
    sys.stdout.write("\n## " + category + '\n\n')
    for topic in collection_dict[category].keys():
        sys.stdout.write("\n### " + topic + '\n\n')
        for repo in collection_dict[category][topic]:
            if repo['website'] == '':
                sys.stdout.write(f"- [**{repo['author']['display_name']}** {repo['name']}]({repo['url']})\n")
            else:
                sys.stdout.write(f"- [**{repo['author']['display_name']}** {repo['name']}]({repo['url']}) | [website]({repo['website']})\n")


