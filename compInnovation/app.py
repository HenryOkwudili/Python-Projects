from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import openai

app = Flask(__name__)

# OpenAI API Key (replace with your own key)
OPENAI_API_KEY = "your-openai-api-key"
openai.api_key = OPENAI_API_KEY


def init_db():
    # Initialize the database with a messages table
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        sender TEXT,
                        message TEXT,
                        response TEXT)''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    # Fetch all messages from the database
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    conn.close()
    return render_template('index.html', messages=messages)


@app.route('/message/<int:message_id>', methods=['GET', 'POST'])
def view_message(message_id):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM messages WHERE id=?", (message_id,))
    message = cursor.fetchone()
    conn.close()

    if request.method == 'POST':
        response_text = request.form['response']
        conn = sqlite3.connect('messages.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE messages SET response=? WHERE id=?", (response_text, message_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('message.html', message=message)


@app.route('/generate-response/<int:message_id>', methods=['POST'])
def generate_response(message_id):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM messages WHERE id=?", (message_id,))
    message_text = cursor.fetchone()[0]
    conn.close()

    # Generate AI response using OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": message_text}]
    )
    ai_response = response["choices"][0]["message"]["content"]

    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE messages SET response=? WHERE id=?", (ai_response, message_id))
    conn.commit()
    conn.close()

    return redirect(url_for('view_message', message_id=message_id))


@app.route('/add', methods=['POST'])
def add_message():
    sender = request.form['sender']
    message_text = request.form['message']
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, message, response) VALUES (?, ?, ?)", (sender, message_text, ''))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
