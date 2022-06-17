from flask import Flask, render_template, request 
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
      if request.method == 'GET':
            return render_template('index.html')
            
      elif request.method == 'POST':
            return f'POST operation carried out on port:{socket.gethostname()}'
      else:
            print('CRUD operation not allowed')
      
if __name__ == '__main__':
      app.run(debug=True)