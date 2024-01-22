import argparse
import requests
import MarkdownParser

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
    body = body.replace('[]', '[&#96;commit-hash&#96;]')
    tempstr = body.split('commit/')[1]
    tempstr = tempstr[0:7]
    body = body.replace('commit-hash', tempstr)
    htmlbody = MarkdownParser.parse(body)
    headers = {
        "Authorization": f"Bearer {token}",  # 使用你的Token
        "Content-Type": "application/json"
    }
    data={
        "title": args.title,
        "body": htmlbody,
        "status": args.status,
    }
    response = requests.post(url, headers=headers, json=data)

    return response.json()

if __name__ == '__main__':
    UpdateIncident()