from flask import Flask, request, jsonify

app = Flask(__name__)

app.name = "seinet-cactus-backend"

@app.route('/api/uploadImage', methods=['POST'])
def get_subscribed_data():
    # Process the request data and create a new user
    # ...
    response = {'message': 'User created successfully',
                'name': str(app.name)}
    image = request.files['image']
    print(image)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


# if __name__ == '__main__':
#     app.run(port=8080, host="0.0.0.0", debug=True)
