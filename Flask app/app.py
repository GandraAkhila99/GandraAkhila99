#

from flask import Flask , render_template , request
app = Flask(__name__) # interfacee between by server and my application wsgi
import pickle
model=pickle.load(open('Chance of Admit.pkl','rb'))

@app.route('/') # bind to an url 
def helloworld():
    return render_template("index.html")
@app.route('/login',methods = ['POST']) # bind to an url 
def admin():
    p = request.form["gs"]
    q = request.form["ts"]
    r = request.form["ur"]
    s = request.form["sop"]
    t = request.form["lop"]
    u = request.form["cgpa"]
    v = request.form["research"]
    x = [[float(p),float(q),float(r),float(s),float(t),float(u),int(v)]]
    z = model.predict(x)
    return render_template("index.html", z ="Chance of Admit:"+ str(z[0][0]))

@app.route('/result')#url
def result():
    return "hie user"
if __name__ == "__main__" :
    app.run(debug = True)

