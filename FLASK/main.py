from flask import Flask, request

app = Flask(__name__)

debug_mode = False
file_hash = "cdedf61f775fb1c091d29a32b6cc2e629f10efc6"


@app.route('/')
def root():
    return 'Welcome!'

@app.route('/hash')
def hash():
    if debug_mode == True:
        return "confirmed" #to be replaced with a token
    else:
        token = request.args.get("token")
        print(token)
        print(file_hash)
        if token == file_hash:
            return "confirmed"
        else:
            return "failed"