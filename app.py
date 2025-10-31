from flask import Flask,render_template, request, redirect
from pymongo import MongoClient
from urllib.parse import quote_plus


# URL-encode the username and password
encoded_username = quote_plus("tusharwdesai")
encoded_password = quote_plus("Tush@3030")

uri = f"mongodb+srv://{encoded_username}:{encoded_password}@luster0.sicg5af.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#uri = "mongodb+srv://tusharwdesai:Tush@3030@cluster0.sicg5af.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['user_db']
collection = db['users']

app = Flask(__name__)

@app.route("/api/users",methods=['GET', 'POST'])
def insertapi():
  if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        
        if username and email:
            # Save to MongoDB
            # collection.insert_one({'username': username, 'email': email})
            # return redirect('/')
         try:
            # Try to insert into MongoDB
            collection.insert_one({'username': username, 'email': email})
            return redirect('/success')
         except errors.PyMongoError as e:
            flash(f'Error saving to database: {str(e)}', 'error')
            return render_template('index.html')


@app.route("/api/read")
def readapi():
   with open("data.json") as f1:
    result = f1.read()
   return result

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route("/")
def index():
 return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)