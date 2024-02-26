from flask import Flask, render_template, redirect, session
from form import RegisterForm, LoginForm, FeedbackForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = "123ABC"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:malongar12@localhost:5432/Users"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

class Register(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(), nullable=False, unique=True)
    lastName = db.Column(db.String(), nullable=False, unique=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False, unique=True)
    feedback = db.relationship("Feedback", backref="register", cascade="all,delete")
    
    
class Feedback(db.Model):
    """Feedback."""

    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(
        db.String(20),
        db.ForeignKey('register.username'),
        nullable=False,
    )
  
   
@app.route("/tweets")
def tweets():
    tweets = Feedback.query.all()
    return render_template("tweets.html", tweets=tweets)
 
 
 
@app.route("/feedback", methods= ["GET", "POST"])  
def feedback():
    form = FeedbackForm()
    

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        username = form.username.data
        
        feedback = Feedback(title=title, content=content,)

        db.session.add(feedback)
        db.session.commit()
  
        return redirect("/tweets")

    return render_template("feedback.html", form=form)
   

@app.route("/<username>")
def user(username):
    
    usrname = Register.query.get_or_404(username).first()
    
    return render_template("user.html", usrname= usrname)



@app.route("/logout")
def logout():
    session.pop("username")
    
    return redirect("/login")


@app.route("/")
def showuser():
    
    if "username" not in session:
        
        return redirect("/register")
    
    user = Register.query.all()
    return render_template("user.html", user=user)




@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.userName.data
        pwd = form.password.data
        
        user = Register.query.filter_by(username=username).first()
        
        if user:
            if bcrypt.check_password_hash(user.password, pwd):
                
                session["username"] = user.username
                return redirect("/feedback")
       
    return render_template("login.html", form=form)






@app.route("/register", methods= ["GET", "POST"])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        firstname = form.firstName.data
        lastname = form.lastName.data
        username = form.userName.data
        email = form.email.data
        password = form.password.data
        
        pw_hash = bcrypt.generate_password_hash(password)
        hashed = pw_hash.decode("utf8")
        
        user = Register(firstName=firstname, lastName=lastname, username=username, email=email, password=hashed)
        
        session["username"] = user.username
        
        db.session.add(user)
        db.session.commit()
        
        return redirect("/")
 
    return render_template("register.html", form= form)

