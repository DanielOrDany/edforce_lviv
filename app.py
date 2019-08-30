from flask import Flask, request, jsonify, json
import psycopg2 as db
from datetime import datetime
from flask_cors import CORS
import uuid
import pybase64

# Init app
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret'

CORS(app)

@app.route('/owners/register', methods=['POST'])
def register():
    data = request.get_json()
    print('beckend')
    print(data)
    for item in data:
        print(item)
        id = uuid.uuid4()
        first_name = item['first_name']
        last_name = item['last_name']
        email = item['email']
        owner_password = item['password']
        created = datetime.utcnow()
        print(id)
        print(first_name)
        print(last_name)
        print(email)
        print(created)
        print(owner_password)

        con = None
        try:
            con = db.connect( database = "d99gqkbd6vao8t",
            user = "tjdzfptfviuxhq",
            password = "013755cf03bd0a8c0d4b0d446921e61702718a849c0eacd2baf477271e601c5d",
            host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
            port = "5432")
            cursor = con.cursor()
            cursor.execute("INSERT INTO owners" + "(id, first_name, last_name, email, password, created)" +
            " VALUES ('"+str(id)+"','"+str(first_name)+"','"+str(last_name)+"','"+str(email)+"','"+str(owner_password)+"','"+str(created)+"');")
            con.commit()

        except (Exception, db.DatabaseError) as error:
            print(error)

        if con is not None:
            con.close()

    return "Hello, cross-origin-world!"

@app.route('/owners/find-owner', methods=['POST'])
def findOnwer():
    result = ""
    data = request.get_json()
    print('beckend')
    print(data)
    for item in data:
        print(item)

        email = item['email']
        owner_password = item['password']   

        print(email)
        print(owner_password)

        con = None
        try:
            con = db.connect( database = "d99gqkbd6vao8t",
            user = "tjdzfptfviuxhq",
            password = "013755cf03bd0a8c0d4b0d446921e61702718a849c0eacd2baf477271e601c5d",
            host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
            port = "5432")
            cursor = con.cursor()
            cursor.execute("SELECT * FROM owners WHERE email = '" + str(email) + "' AND password = '" + str(owner_password) + "';")
            rows = cursor.fetchall()
            for row in rows:
                if row == None:
                    console.log('nobody')
                    return jsonify({'result': 'nobody'})

                else:
                    print(row[3])
                    return jsonify({'result': 'user exists'})

        except (Exception, db.DatabaseError) as error:
            print(error)

        if con is not None:
            con.close()

    return jsonify({'result': result})

@app.route('/test', methods=['POST'])
def addTest():
    data = request.get_json()
    print('beckend')
    print(data)
    for item in data:
        print(item)
        ask = item['ask']
        answers = item['answers']
        answer = item['answer']
        test_code = item['testCode']
        status = item['status']
        print(ask)
        print(answers)
        print(answer)
        print(test_code)
        print(status)
        con = None
        try:
            con = db.connect( database = "d99gqkbd6vao8t",
            user = "tjdzfptfviuxhq",
            password = "013755cf03bd0a8c0d4b0d446921e61702718a849c0eacd2baf477271e601c5d",
            host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
            port = "5432")
            cursor = con.cursor()
            cursor.execute("INSERT INTO tests" + "(id, ask, answers, answer, test_code, status)" +
            " VALUES ('"+str(uuid.uuid4())+"','"+str(ask)+"','"+str(answers)+"','"+str(answer)+"','"+str(test_code)+"','"+str(status)+"');")
            con.commit()
        except (Exception, db.DatabaseError) as error:
            print(error)

        if con is not None:
            con.close()

    return "Hello, cross-origin-world!"

@app.route('/check-test-code', methods=['POST'])
def check_test_code():
    print('check')
    data = request.get_json()
    print(data)
    print(data['test_code'])
    con = None
    try:
        con = db.connect( database = "d99gqkbd6vao8t",
        user = "tjdzfptfviuxhq",
        password = "013755cf03bd0a8c0d4b0d446921e61702718a849c0eacd2baf477271e601c5d",
        host = "ec2-46-137-113-157.eu-west-1.compute.amazonaws.com",
        port = "5432")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tests WHERE test_code = '"+data['test_code']+"';")
        rows = cursor.fetchall()
        for row in rows:
            if row == None:
                return jsonify({'code': 'none'})
            else:
                code = row[4]
                response = app.response_class({'code':code}, status=200, mimetype='application/json')
                return response
        con.commit()
    except (Exception, db.DatabaseError) as error:
        print(error)

    if con is not None:
        con.close()

# Run Server
if __name__ == "__main__":
    app.run(debug=True)