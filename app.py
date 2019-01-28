from flask import Flask, render_template, session,request,redirect,url_for
from database import add_user, get_all_users,query_by_username
app = Flask(__name__)

app.secret_key="sarah"

@app.route('/')
def home():
  if session.get('display_login') == True:
    session['display_login'] = False
    return render_template('homepage.html', logged_in=True)
  else:
    return render_template('homepage.html', logged_in=False)


# @app.route('/')
# def homepage():
#     return render_template('homepage.html')




@app.route('/signup', methods=['GET', 'POST'])
def signup_route():
  if request.method == 'GET':
    return render_template('signup.html')
  else:
    print ('Received POST request for sign up!')
    # nationality = request.form['nationality']
    name = request.form['name']
    username=request.form['username']
    password= request.form['password']
    
    g=add_user(name,username, password)

    if g!=None:
      print ('we already have a user with that name')
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login_route():
  if 'logged_in' in session and session['logged_in']==True:
    return redirect (url_for('home'))
  if request.method == 'POST':
    # return redirect (url_for('home'))
    print('hey')
    username = request.form['username']
    user=query_by_username(username)
    if user==None:
      return redirect (url_for('signup_route'))
    else:
      # if request.form.get('password') and
        if request.form['password']== user.password:
            session["logged_in"] = True
            session["user_id"] = user.name
            session["display_login"] = True


        return render_template('homepage.html')
  else:
    return render_template('login.html') 

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/logout')
def logout_route():
  if 'user_id' in session:
    del session['user_id']
    session['logged_in']=False
  return redirect(url_for('home'))
  print('logged out')

@app.route('/addprogramme')
def addprogramme():
    return render_template('addprogramme.html')

@app.route('/vprogramme')
def vprogramme():
    return render_template('vprogramme.html')




if __name__ == '__main__':
    app.run(debug=True)


