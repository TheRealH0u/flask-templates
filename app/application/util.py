import os, datetime
from flask import jsonify, abort, session, url_for, redirect, request


generate = lambda x: os.urandom(x).hex()
key = 'SOtqCasVL3Icp0fBOiFg5W2YdvgkqKrpki0nXzdKUUWKTSigK0'


def response(message):
    return jsonify({'message': message})