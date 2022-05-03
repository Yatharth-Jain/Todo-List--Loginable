from flask import Blueprint, redirect, render_template , request,flash, url_for
from .models import User,db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in Successfully!','success')
                login_user(user, remember=True)
                print("Logged in Done")
                return redirect(url_for('views.home'))

            else:
                flash('Incorrect Password!','error')
        else:
            flash('Email Does Not Exist!','error')
    return render_template('login.html',boolean=True,user=current_user)

@auth.route('/logout')
@login_required                 # if logged in then the function will run
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if(request.method=='POST'):
        name=request.form.get('username')
        email=request.form.get('email')
        pass1=request.form.get('password1')
        pass2=request.form.get('password2')
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already exist.")

        elif len(email)<4:
            flash('Email must be greater than 4 character.','error')

        elif len(name)<2:
            flash('Name must be greater than 1 character.','error')
            
        elif pass1!=pass2:
            flash('Password should Match.','error')

        elif len(pass1)<7:
            flash("Password lenght should be greater than 6.",'error')
        else:
            pass1=generate_password_hash(pass1,method='sha256')
            new_user=User(name=name,email=email,password=pass1)
            db.session.add(new_user)
            db.session.commit()
            print(f'{name}--{email}--{pass1}--{pass2}')
            flash("Account has been Created.",'success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
            
    return render_template('Signup.html',user=current_user)
    
