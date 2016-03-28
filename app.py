from flask import Flask
from flask import render_template
from flask import request
import aiml

bot = aiml.Kernel()
try:
    print '[+] loading bot brain'
    bot.learn('brain/brain.aiml')
    print '[+] brain loaded'
    print 'App is running at port 8888'
except Exception as e:
    raise Exception(e)

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/apps', methods=['GET','POST'])
def echo():
    answer = bot.respond(request.form['text'])

    return render_template("index.html",data=answer)

if __name__ == "__main__":
	app.run(threaded=True, debug = True, host='0.0.0.0', port=8888, passthrough_errors=True)
