import os
import re
import argparse
from message_send import MessageSend


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--issue_title', type=str, required=True)
    parser.add_argument('--issue_content', type=str, required=True)
    args = parser.parse_args()

    pushplus_token = os.environ.get('PUSHPLUS_TOKEN')
    serverChan_sendkey = os.environ.get('SERVERCHAN_SENDKEY')
    weCom_tokens = os.environ.get('WECOM_TOKENS')
    weCom_webhook = os.environ.get('WECOM_WEBHOOK')
    bark_deviceKey = os.environ.get('BARK_DEVICEKEY')
    feishu_deviceKey = os.environ.get('FEISHU_DEVICEKEY')

    message_tokens = {
        'pushplus_token': pushplus_token,
        'serverChan_token': serverChan_sendkey,
        'weCom_tokens': weCom_tokens,
        'weCom_webhook': weCom_webhook,
        'bark_deviceKey': bark_deviceKey,
        'feishu_deviceKey': feishu_deviceKey,
    }

    args.issue_content = args.issue_content.replace('`', '')
    message_send = MessageSend()
    message_send.send_all(message_tokens, args.issue_title, args.issue_content)

    print('finish')

if __name__ == '__main__':
    main()
