from run import app
from flask import Flask, request, make_response
from hashlib import sha1


@app.route('/text_reply')
def text_replay():
    if request.method == 'GET':
        token = r'test' # 这个根据自己的设置自行修改
        signature = request.args.get('signature', '')
        echostr = request.args.get('echostr', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        tmp = [timestamp, nonce, token]
        tmp.sort()
        tmp = ''.join(tmp)
        if signature == sha1(tmp).hexdigest():
            return  make_response(echostr)
        else:
            return "Access denied.diy"
    pass















