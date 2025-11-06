#!/usr/bin/env python3
from flask import Flask, request, send_from_directory, jsonify, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

SUBMISSIONS_FILE = 'form_submissions.json'

def load_submissions():
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_submission(data):
    submissions = load_submissions()
    submission = {
        'timestamp': datetime.now().isoformat(),
        'data': data
    }
    submissions.append(submission)
    with open(SUBMISSIONS_FILE, 'w') as f:
        json.dump(submissions, f, indent=2)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        form_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'company': request.form.get('company'),
            'phone': request.form.get('phone'),
            'industry': request.form.get('industry'),
            'scale': request.form.get('scale'),
            'message': request.form.get('message')
        }
        
        save_submission(form_data)
        
        return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Thank You - CloudFactory Pro</title>
            <link rel="stylesheet" href="/style.css">
        </head>
        <body>
            <nav class="navbar">
                <div class="container">
                    <div class="logo">
                        <span class="logo-icon">⚙️</span>
                        <h1>CloudFactory Pro</h1>
                    </div>
                </div>
            </nav>
            
            <section class="contact">
                <div class="container">
                    <div class="contact-form" style="text-align: center; padding: 4rem 3rem;">
                        <div style="font-size: 4rem; margin-bottom: 1rem;">✅</div>
                        <h2 class="section-title" style="margin-bottom: 1rem;">Thank You!</h2>
                        <p style="font-size: 1.2rem; color: #6b7280; margin-bottom: 2rem;">
                            Your demo request has been submitted successfully.<br>
                            We'll get back to you within 24 hours.
                        </p>
                        <a href="/" class="btn-primary" style="display: inline-block;">Back to Home</a>
                    </div>
                </div>
            </section>
            
            <footer class="footer">
                <div class="container">
                    <div class="footer-content">
                        <div class="footer-section">
                            <h3>CloudFactory Pro</h3>
                            <p>Smart Manufacturing Dashboard powered by Cloud Platform</p>
                        </div>
                    </div>
                </div>
            </footer>
        </body>
        </html>
        '''
    except Exception as e:
        return f'<h1>Error: {str(e)}</h1><a href="/">Go back</a>', 500

@app.route('/submissions')
def view_submissions():
    submissions = load_submissions()
    return jsonify(submissions)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
