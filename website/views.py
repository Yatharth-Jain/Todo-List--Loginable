from .models import Notes
from flask import Blueprint, flash, redirect, render_template,request
from flask_login import login_required, current_user
from . import db

views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if(request.method=='POST'):
        note=request.form['note']
        print("\n\n\n\nDone\n\n\n\n")
        if(len(note)<1):
            flash('Note is too short!','error')
        else:
            new_note=Notes(data=note,user_id=current_user.uid)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!','success')
            print("Done")

    return render_template('Home.html',user=current_user)

@views.route('/del/<int:nid>')
def deletenote(nid):
    delnote=Notes.query.filter_by(nid=nid).first()
    db.session.delete(delnote)
    db.session.commit()
    flash('Note Deleted!','success')
    return redirect('/')