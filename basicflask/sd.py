from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name="singh"
    list1=[10,20,30]
    return render_template('cd.html',name=name)
@app.route('/list')
def index1():
    list1=[10,20,30]
    return render_template('cd.html',list1=list1)
@app.route('/listt')
def index2():
    list2=(30,40,50)
    return render_template('cd.html',list2=list2)

if __name__=="__main__":
    app.run(debug=True)
