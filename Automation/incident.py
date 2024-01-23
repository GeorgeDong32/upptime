import argparse
import requests
import re

def UpdateIncident():
    parser = argparse.ArgumentParser()
    parser.add_argument('--token', type=str, required=True)
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--title', type=str, required=True)
    parser.add_argument('--content', type=str, required=True)
    parser.add_argument('--status', type=str, required=True)
    args = parser.parse_args()
    url = args.url
    token = args.token
    body = args.content
    # 处理 body
    body = body.replace('[]', '[commit-hash]')
    tempstr = body.split('commit/')[1]
    tempstr = tempstr[0:7]
    body = body.replace('commit-hash', tempstr)
    pattern = r'\[(.*?)\]\((.*?)\)'
    repl = r'<a href="\2">\1</a>'
    body = re.sub(pattern, repl, body, flags=re.DOTALL)
    body = body.replace('\"', '\\"', 2)
    body = body.replace('\"', '\\"', 2)
    body = body.replace('**', '<b>', 1)
    body = body.replace('**', '</b>', 1)
    body = body.replace('()', '')
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data={
        "title": args.title,
        "body": body,
        "status": args.status,
    }
    response = requests.post(url, headers=headers, json=data)
    if(response.status_code == 201 or response.status_code == 200):
        return response.json()
    else:
        return response.text

if __name__ == '__main__':
    UpdateIncident()