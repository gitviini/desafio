from flask import Flask, render_template, make_response, request as req, jsonify

app = Flask(__name__)

from app.controlers.default import *