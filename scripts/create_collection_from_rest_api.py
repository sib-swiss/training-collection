import requests


API_URL = "https://glittr.org/api/list"


def format_repo_line(repo):
    display_name = repo['author']['display_name'].strip()
    name = repo['name']
    url = repo['url']
    website = repo['website']

    label = f"**{display_name}** {name}"

    if website:
        return f"- [{label}]({url}) | [website]({website})\n"
    return f"- [{label}]({url})\n"

def get_repos():
    response = requests.get(API_URL, timeout=30)
    response.raise_for_status()
    return response.json()

def write_toc(collection_list, outfile):
    for category in collection_list:
        category_name = category['name']
        outfile.write(f"- [{category_name}](#{category_name.lower().replace(' ', '-')})\n")
        for topic in category['topics']:
            topic_name = topic['name']
            outfile.write(f"  - [{topic_name}](#{topic_name.lower().replace(' ', '-')})\n")


def write_collection(collection_list, outfile):
    for category in collection_list:
        category_name = category['name']
        outfile.write("\n## " + category_name + '\n\n')
        for topic in category['topics']:
            topic_name = topic['name']
            outfile.write("\n### " + topic_name + '\n\n')
            repo_list = topic['repositories']
            for repo in repo_list:
                outfile.write(format_repo_line(repo))

if __name__ == '__main__':
    collection_list = get_repos()

    output_file = 'README.md'

    with open(output_file, 'w') as outfile:
        with open('scripts/collection_header.md') as infile:
            for line in infile:
                outfile.write(line)
            write_toc(collection_list, outfile)
            write_collection(collection_list, outfile)
