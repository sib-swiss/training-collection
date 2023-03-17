import requests

def get_repos():
    r = requests.get("https://glittr.org/api/list")
    collection_list = r.json()
    return(collection_list)

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
                if repo['website'] == '':
                    outfile.write(f"- [**{repo['author']['display_name']}** {repo['name']}]({repo['url']})\n")
                else:
                    outfile.write(f"- [**{repo['author']['display_name']}** {repo['name']}]({repo['url']}) | [website]({repo['website']})\n")

if __name__ == '__main__':
    collection_list = get_repos()

    output_file = 'README.md'

    with open(output_file, 'w') as outfile:
        with open('scripts/collection_header.md') as infile:
            for line in infile:
                outfile.write(line)
            write_toc(collection_list, outfile)
            write_collection(collection_list, outfile)
