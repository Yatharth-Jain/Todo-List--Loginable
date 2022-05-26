from website import create_app,db
from website.models import User,Notes
from flask_sqlalchemy import SQLAlchemy
import flask

app=create_app()
app.app_context().push()
print("Hello")
if __name__=='__main__':
    app.run(debug=True)