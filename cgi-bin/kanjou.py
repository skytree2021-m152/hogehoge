#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi, requests



def main(content, access_token="AIzaSyAzX7s-hgiekJ7KzSJvfI2yoElbEcZrpLM"):
    geturl = 'https://language.googleapis.com/v1/documents:analyzeSentiment?key={}'.format(access_token)
    h = {'Content-Type': 'application/json'}
    b = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": content
        },
        "encodingType": "UTF8"
    }
    res = requests.post(geturl, headers=h, json=b).json()
    return res