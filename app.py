from flask import Flask, render_template, request, send_file
import cv2
import numpy as np  # Menambahkan import NumPy
from pydub import AudioSegment

app = Flask(__name__)

# Fungsi untuk melakukan resize gambar menggunakan OpenCV
def resize_image(image, new_width, new_height):
    return cv2.resize(image, (new_width, new_height))

# Fungsi untuk melakukan kompresi audio menggunakan Pydub
def compress_audio(audio_file, bitrate):
    audio = AudioSegment.from_file(audio_file)
    compressed_audio = audio.set_frame_rate(bitrate)
    return compressed_audio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resize_image', methods=['POST'])
def resize_image_route():
    # Mendapatkan gambar dan ukuran yang diinginkan dari klien
    image_file = request.files['image']
    width = int(request.form['width'])  # Mendapatkan lebar yang diinginkan
    height = int(request.form['height'])  # Mendapatkan tinggi yang diinginkan
    
    # Proses resize gambar menggunakan OpenCV
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), -1)
    resized_image = resize_image(image, width, height)
    
    # Simpan gambar yang diubah ke sementara.jpg
    cv2.imwrite('sementara.jpg', resized_image)
    
    # Kirimkan gambar yang diubah kembali ke klien
    return send_file('sementara.jpg', mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
