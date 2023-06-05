from flask import Flask, request, jsonify
from sklearn.cluster import KMeans
import cv2
from collections import Counter

app = Flask(__name__)

app.name = "seinet-cactus-backend"

@app.route('/api/uploadImage', methods=['POST'])
def get_subscribed_data():
    # Process the request data and create a new user
    # ...
    response = {}
    image = request.files['image']

    print(image)
    codes = get_colors(get_image(image), 7)

    return jsonify(codes)

def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

def get_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def get_colors(image, number_of_colors):
    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)
    # sort to ensure correct color percentage
    counts = dict(sorted(counts.items()))

    center_colors = clf.cluster_centers_
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]

    return hex_colors

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(port=8080, host="0.0.0.0", debug=True)
