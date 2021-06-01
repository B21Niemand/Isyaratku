#app.py

import logging

from flask import Flask, request
from store import download_image

app = Flask(__main__)

@app.route('/')
def download_picture():
	huruf = request.form['huruf']
	image = r"/([^/]*[^/\d])\d*\.jpg"
	if huruf in image:
		return download_image()
	else:
		return 'Data Tidak Tersedia'

@app.errorhandler(500)
def server_error(e):
	logging.exception('An error occurred during a request.')
	return """An internal error occured""",500

if __name__ == "__main__":
    app.run(debug=True)
