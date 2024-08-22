from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_segitiga', methods=['POST'])
def generate_segitiga():
    number_str = request.form.get('number')
    number = int(number_str)
    result = generate_segitiga_pattern(number)
    return jsonify({"result": result})

@app.route('/generate_ganjil', methods=['POST'])
def generate_ganjil():
    number_str = request.form.get('number')
    number = int(number_str)
    result = generate_ganjil_pattern(number)
    return jsonify({"result": result})

@app.route('/generate_prima', methods=['POST'])
def generate_prima():
    number_str = request.form.get('number')
    number = int(number_str)
    result = generate_prima_pattern(number)
    return jsonify({"result": result})

def generate_segitiga_pattern(number):
    result = ''
    str_num = str(number)
    for i in range(len(str_num)):
        idx = i + 1
        result += str_num[i] + "0" * idx + '\n'
    return result.strip()

def generate_ganjil_pattern(max_number):
    result = [str(i) for i in range(1, max_number + 1) if i %2 != 0]
    return result

def generate_prima_pattern(max_number):
    result = [str(num) for num in range(2, max_number + 1) if is_prime(num)]
    return result

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True

if __name__ == '__main__':
    app.run(debug=True)