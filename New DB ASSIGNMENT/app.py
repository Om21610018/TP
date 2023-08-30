from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__, template_folder="templates")


# MySQL Configuration
db = mysql.connector.connect(
    host="db",  # This should match the MySQL service prn in docker-compose.yml
    user="root",
    password="password",
    database="mydatabase"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    prn = request.form.get('prn')
    name=request.form.get('name')
    email = request.form.get('email')
    age=request.form.get('age')
    branch=request.form.get('branch')
    
    # Insert data into MySQL
    insert_query = "INSERT INTO students (prn,name,email,age,branch) VALUES (%s,%s,%s,%s,%s)"
    cursor.execute(insert_query, (prn,name,email,age,branch))
    db.commit()
    
    return "Data saved successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
