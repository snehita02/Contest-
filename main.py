# importing flask and required packages in flask
from flask import Flask,render_template,request,redirect,url_for,flash
from Forms import signup,login,post
import database as db


#creating an app instance for the website
app=Flask(__name__)

#adding secret key
app.config['SECRET_KEY']='meety'

global user
global error
#creating a login or signup page

@app.route("/",methods=['GET','POST'])
def login_page():

    signup_form=signup()
    login_form=login()
    if signup_form.validate_on_submit():
        print(request.form)
        if request.form['submit']=="pressed_login":
            userid=request.form['userid']
            passwd=request.form['passwd']
            global user
            user= request.form.get('userid')
            print(user)
            if db.check_user(userid,passwd):
                print(user)
                return redirect(url_for('home', user= user))
        elif request.form['submit']=="pressed_signup":
            userid = request.form['userid']
            passwd = request.form['passwd']

            if db.add_user(userid,passwd)==False:
                global error
                error="user id already exists please try another username"
                print("thee is a n error")
                flash(error)
                # return redirect(url_for('error'))
    #directing to login page of contest
    return render_template('login.html',signup=signup_form,login=login_form)


#creating home page:
@app.route("/home",methods=['GET','POST'])
def home():

    print("in home page",user)
    posts=db.show_posts()
    print(request.form)
    if 'like' in request.form:
        db.add_like(request.form['like'])
        return redirect(url_for('home'))
    if 'page' in request.form:
        print("hi",request.form)

        if request.form['page']=='home':
            return redirect(url_for('home'))
        elif request.form['page']=='day':
            return redirect(url_for('day'))
        elif request.form['page']=='profile':
            return redirect(url_for('profile'))
    return render_template('home.html',posts=posts)


#day contest page
@app.route("/type_today",methods=['GET','POST'])
def day():
    img=url_for('static',filename='1.jpg')
    posts = db.today_posts()
    print(request.form)
    if 'like' in request.form:
        db.add_like(request.form['like'])
        return redirect(url_for('day'))
    if 'page' in request.form:
        print("hi", request.form)

        if request.form['page'] == 'home':
            return redirect(url_for('home'))
        elif request.form['page'] == 'day':
            return redirect(url_for('day'))
        elif request.form['page'] == 'profile':
            return redirect(url_for('profile'))
    return render_template('day.html', posts=posts,img=img)

#profile page
@app.route("/profile",methods=['GET','POST'])
def profile():
    posts = db.user_posts(user)
    form=post()
    print(request.form)
    if 'like' in request.form:
        db.add_like(request.form['like'])
        return redirect(url_for('profile'))
    if 'posting' in request.form:
        print("posting in request")
        if request.form['posting'] == 'pressed_post':
            quoet = str(request.form.get('quoet'))
            db.add_post(user, quoet)
            return redirect(url_for('profile'))
    if 'page' in request.form:
        print("hi", request.form)

        if request.form['page'] == 'home':
            return redirect(url_for('home'))
        elif request.form['page'] == 'day':
            return redirect(url_for('day'))
        elif request.form['page'] == 'profile':
            return redirect(url_for('profile'))
    return render_template('profile.html', posts=posts,form=form)


@app.route("/error",methods=['GET','POST'])
def error():
    return render_template('error.html',error=error)
#make the app run continusly with debugging
if __name__=='__main__':
    app.run(debug=True)