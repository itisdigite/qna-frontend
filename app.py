from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__, template_folder="templates")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Write the username and password to a csv file
    with open("credentials.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
    # Read the username and password from the csv file
    with open("credentials.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return "Login successful!"
    
    # Here, you can add your logic to verify the username and password.
    if username == 'admin' and password == 'admin':
        return redirect(url_for('index'))
    else:
        return 'Login Failed'


@app.route('/register')
def register():
    return render_template('register.html')

# ----------------**--------------------
# @app.route('/verify', methods=['GET', 'POST'])
# def verify():
#     if request.method == 'POST':
#         verification_code = request.form['verification_code']
#         # Add your verification logic here
#         return "Verification Successful"  # Placeholder response
#     return render_template('verification.html')



if __name__ == '__main__':
    app.run(debug=True, port=8080)

#

# Step 3: Define a route for '/login'
#@app.route("/login")
#def login():
    # Render 'login.html' when the '/login' route is accessed
    #return render_template("login.html")

#if __name__ == '__main__':
    # Step 4: Run the Flask application
    # Set debug=True for development to auto-reload on changes
    #app.run(debug=True, port=8081)

     # Simple registration page or logic here
    #return redirect(url_for("Register.html")) # Removed the erroneous part
    # If you intended to redirect, you might have meant something like this:
    # return redirect(url_for('register'))
