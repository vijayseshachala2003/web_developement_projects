from flask import Flask,render_template,request,url_for,redirect
import cx_Oracle as cxo
con=cxo.connect('system/Boss2003@localhost:1521/xe')
app=Flask(__name__)
@app.route("/")
@app.route('/mainPage')
def mainPage():
     return render_template('mainPage.html')
# mainPage --> login
@app.route("/login",methods = ['post','get'])
def login():
    return render_template('logInPage.html')
#or login to accountLog
@app.route('/redirect_create',methods=['post','get'])
def redirect_create():
    return render_template('accountLog.html')
# from accountLog to login
@app.route('/create_to_login',methods = ['post','get'])
def create_to_login():
    return render_template('logInPage.html')
@app.route('/validate_login',methods=["post","get"])
def validate_login():
    username=request.form.get('email')
    password=request.form.get('pwd')
    cur=con.cursor()
    rows=cur.execute('select * from userinfo')
    for i in rows.fetchall():
        #print(username,i[0],password,i[1])
        if username==i[0] and password==i[1]:
            return render_template('basicStore.html')
    return render_template('fail.html')

@app.route('/resubmit')
def resubmit():
    return render_template('logInPage.html')


@app.route('/insert_details',methods=['get'])
def insert_details():
    f_name = request.form.get('first')
    l_name = request.form.get('last')
    email = request.form.get('email')
    pwd = request.form.get('pwd')
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO userinfo VALUES(:username,:password,:fname,:lname)",[email,pwd,f_name,l_name])
        print("inserted ")
        con.commit()
        cur.close()

        return render_template('logInPage.html')
    except Exception as e:
        print(e)
        return render_template('fail.html')
# create to store
@app.route("/subpass")
def subpass():
    return render_template('basicStore.html')
# cart

@app.route("/cart")
def cart():
    print("before")
    return render_template('checkout.html')
    print("after")
@app.route('/done')
def done():
    print("before done")
    return render_template('thankyou.html')
    print("after done")
if __name__=="__main__":
    app.run(debug = True)