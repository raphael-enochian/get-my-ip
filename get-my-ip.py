#!/usr/bin/env python
# Raphael Enochian, September 2015
# Queries DDG for your IP address.
import requests


def main():
    headers = {
        "description": "Chrome 42.0.2311.135 (Win 7 32)",
        "useragent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
        "appname": "Netscape",
        "appversion": "5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
        "platform": "Win32",
        "vendor": "Google Inc.",
        "vendorsub": "",
        "buildID": "",
        "oscpu": "",
        "accept_encoding": "gzip,deflate,sdch",
        "accept_default": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "accept_lang": "en-US",
        "pixeldepth": "24",
        "colordepth": "24",
        "screens": "800x600,1024x600,1024x768,1152x864,1280x720,1280x768,1280x800,1280x960,1280x1024,1360x768,1366x768,1440x900,1400x1050,1600x900,1600x1200,1680x1050,1920x1080,1920x1200,2048x1152,2560x1440,2560x1600",
        "profileID": "W1",
    }
    ddg_url = 'https://duckduckgo.com/?q=what+is+my+ip&ia=answer&format=json'

    req = requests.get(ddg_url, headers=headers)
    print(req.json()['Answer'])

if __name__ == '__main__':
    main()
