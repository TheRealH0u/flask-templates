import os, jwt, datetime
from flask import jsonify, abort, session, url_for, redirect, request
from functools import wraps


generate = lambda x: os.urandom(x).hex()
key = 'SOtqCasVL3Icp0fBOiFg5W2YdvgkqKrpki0nXzdKUUWKTSigK0'


def response(message):
    return jsonify({'message': message})


def createJWT(username):
    token_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=360)
    encoded = jwt.encode(
        {
            'username': username,
            'exp': token_expiration
        },
        key,
        algorithm='HS256'
    )
    return encoded


def verifyJWT(token):
    try:
        token_decode = jwt.decode(
            token,
            key,
            algorithms=['HS256']
        )
        return token_decode
    except:
        return abort(400, 'Invalid token!')


def authenticated(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('web.login'))
        verifyJWT(token)
        return f(*args, **kwargs)
    return decorator


def isAdmin(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = verifyJWT(request.cookies.get('token'))
        if token and token['username'] == 'admin':
            return f(*args, **kwargs)
        else:
            return abort(401, 'Unauthorised access detected!')
    return decorator
