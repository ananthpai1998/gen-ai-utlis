import tensorflow as tf
from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify
import base64


def generate_images(user_input):
    
    print('Recived post request to generate images..')
    print('Loading the model ...')
    testing_gen = load_model('p1_gen.h5')
    print('Generating images ...')
    one_hot_labels = tf.one_hot(tf.constant([int(user_input)]), 10)
    random_latent_vectors = tf.random.normal(shape=(1, 100))
    generated_images = testing_gen(tf.concat([random_latent_vectors, one_hot_labels], axis=-1))
    image_data = tf.image.encode_png(tf.cast(generated_images[0] * 255, tf.uint8).numpy())
    encoded_image = base64.b64encode(image_data.numpy()).decode('utf-8')
    image_src = f"data:image/png;base64,{encoded_image}"
                
    html_response = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Generated Image</title>
                    </head>
                    <body>
                        <h1>Generated Image</h1>
                        <img src="{image_src}" alt="Generated Image" width="300" height="300">
                    </body>
                    </html>
                """
    return html_response


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET" or request.method == "POST":
        user_input = request.args.get('user_input')
        if user_input is not None: 
            try:    
                return generate_images(user_input)
            except Exception as e:
                return jsonify({"error": str(e)})           
        else:
            print('No user inputs received')
            return "No user inputs received"      
    return "Requested Method Not Implemented"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    