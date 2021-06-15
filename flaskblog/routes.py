from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import sqlite3
from sqlite3 import Error
@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/events")
@login_required
def events():
    return render_template('events.html', title='Event Select')

@app.route("/safari")
def safari():
    return render_template('safari.html', title='SAFARI THEME')

@app.route("/pestal")
def pestal():
    return render_template('pestal.html', title='PESTAL THEME')

@app.route("/rainbow")
def rainbow():
    return render_template('rainbow.html', title='RAINBOW THEME')

@app.route("/moody")
def moody():
    return render_template('moody.html', title='MOODY THEME')

@app.route("/wcard")
@login_required
def wcard():
    return render_template('wcard.html', title='Choose Theme')

@app.route("/bcard")
@login_required
def bcard():
    return render_template('bcard.html', title='Choose Theme')

@app.route("/receipt")
@login_required
def receipt():
    return render_template('receipt.html', title='PAYMENT RECEIPT')

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@app.route("/pay")
@login_required
def pay():
    return render_template('pay.html', title='Pay')

@app.route('/form', methods = ['GET', 'POST'])
@login_required
def form():
        
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('forms.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM forms")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('forms.db')
            cur = conn.cursor()
            cur.execute("Insert into forms(pID,name,theme,PhoneNo,sex,Age,food,location,date,stime,etime,req,guestno,band,makeup,gname,bname) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (data.get('pID'),data.get('name'),data.get('theme'),data.get('PhoneNo'),data.get('sex'),data.get('Age'),data.get('food'),data.get('location'),data.get('date'),data.get('stime'),data.get('etime'),data.get('req'),data.get('guestno'),data.get('band'),data.get('makeup'),data.get('gname'),data.get('bname')))
            conn.commit()
            cur.execute("SELECT * FROM forms")
            rows = cur.fetchall()
            
            return render_template('form.html', data=rows)
            print(rows)
       except Error as e:
            print(e)
            
            return redirect('/receipt') 
    return render_template('form.html')

@app.route('/wform', methods = ['GET', 'POST'])
@login_required
def wform():
        
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('forms.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM forms")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('forms.db')
            cur = conn.cursor()
            cur.execute("Insert into forms(pID,name,theme,PhoneNo,sex,Age,food,location,date,stime,etime,req,guestno,band,makeup,gname,bname) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (data.get('pID'),data.get('name'),data.get('theme'),data.get('PhoneNo'),data.get('sex'),data.get('Age'),data.get('food'),data.get('location'),data.get('date'),data.get('stime'),data.get('etime'),data.get('req'),data.get('guestno'),data.get('band'),data.get('makeup'),data.get('gname'),data.get('bname')))
            conn.commit()
            cur.execute("SELECT * FROM forms")
            rows = cur.fetchall()
            
            return render_template('wform.html', data=rows)
            print(rows)
       except Error as e:
            print(e)
        
    return render_template('wform.html')

    
'''@app.route('/wform', methods = ['GET', 'POST'])
@login_required
def wform():
        
    if request.method == "POST":
       data = request.form
      
       conn = sqlite3.connect('wforms.db')
       cur = conn.cursor()
       cur.execute("SELECT * FROM wforms")
       rows = cur.fetchall()
    
       try:

            conn = sqlite3.connect('wforms.db')
            cur = conn.cursor()
            cur.execute("Insert into forms(pID,gname,bname,theme,PhoneNo,makeup,band,food,date,req,guestno) values (?,?,?,?,?,?,?,?,?,?,?)", (data.get('pID'),data.get('gname'),data.get('bname'),data.get('theme'),data.get('PhoneNo'),data.get('makeup'),data.get('band'),data.get('food'),data.get('date'),data.get('req'),data.get('guestno')))
            conn.commit()
            cur.execute("SELECT * FROM wforms")
            rows = cur.fetchall()
            
            return render_template('wform.html', data=rows)
            print(rows)
       except Error as e:
            print(e)
        
    return render_template('wform.html')'''
