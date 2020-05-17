import logging
import gspread
import json
import os

from flask import Flask
import google.auth

app = Flask(__name__)

logging.getLogger().setLevel(logging.INFO)


@app.route('/<id>', methods=['GET'])
def api_get(id):
    logging.info('Getting the id {}'.format(id))
    record = get_record(id)
    return json.dumps(record)


def get_client():
    credentials, project = google.auth.default(
        scopes=[
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
            ])
    return gspread.authorize(credentials)


def get_record(id):
    client = get_client()
    sheet = client.open_by_key(os.environ.get('SHEET_ID','1fRUorOlOFRQ7-tNs-OzPDHF9HKDWWi9zmo4oMd1AGVU')).sheet1
    data = sheet.get_all_records()

    for d in data:
        if d['id'] == int(id):
            return d


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)