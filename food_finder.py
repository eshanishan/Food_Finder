from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.debug = True
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  selected_items = request.form.getlist('items')
  return redirect(url_for('result', items=','.join(selected_items)))

@app.route('/result')
def result():
  items = request.args.get('items').split(',')
  return f'Selected items: {", ".join(items)}'

if __name__ == '__main__':
  app.run()