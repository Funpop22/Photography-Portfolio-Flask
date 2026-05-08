from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# Database Set up karna
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, message TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    
    # Yahan hum password ko Hash (encrypt) kar rahe hain
    hashed_pwd = generate_password_hash('rk123')
    
    # Default admin check karke daalna
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', hashed_pwd))
    
    conn.commit()
    conn.close()

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Contact Form Data save
@app.route('/submit_contact', methods=['POST'])
def contact():
    name = request.form['name']
    message = request.form['message']
    
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()
    return "Thanks! Message Saved in Database."

# Secure Admin Panel Route
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username=?", (user,))
        user_record = c.fetchone()
        
        # Yahan hum check kar rahe hain ki kya user hai aur kya password ka hash match hota hai
        if user_record and check_password_hash(user_record[0], pwd):
            c.execute("SELECT * FROM contacts")
            all_messages = c.fetchall()
            conn.close()
            return render_template('admin.html', logged_in=True, messages=all_messages)
        else:
            conn.close()
            return "<h2 style='color:red; text-align:center;'>Galat Password yaar! Wapas try kar.</h2>"
            
    return render_template('admin.html', logged_in=False)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)