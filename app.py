from flask import Flask, render_template, request, redirect, url_for
import re
from models import db, Log

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        log_file = request.files.get('logfile')
        if log_file:
            lines = log_file.read().decode('utf-8').splitlines()

            ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'
            status_pattern = r'\" (\d{3})'
            time_pattern = r'\[(.*?)\]'

            for line in lines:
                ip = re.search(ip_pattern, line)
                status = re.search(status_pattern, line)
                time = re.search(time_pattern, line)

                new_log = Log(
                    content=line,
                    ip_address=ip.group() if ip else None,
                    status_code=status.group(1) if status else None,
                    timestamp=time.group(1) if time else None
                )
                db.session.add(new_log)
            db.session.commit()
            return redirect(url_for('view_logs'))
    return render_template('upload.html')

@app.route('/logs')
def view_logs():
    logs = Log.query.all()
    return render_template('view_logs.html', logs=logs)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
