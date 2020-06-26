from flask import Blueprint, request, render_template, current_app, send_from_directory
from flask_uploads import UploadSet, IMAGES

bp_upload = Blueprint('bp_upload', __name__)
photos = UploadSet('photos', IMAGES)

'''
@bp_upload.route('/index', methods=["GET", "POST"])
def index_upload():
    if request.method == "POST":
        photo = request.files.get('photo')
        photos.save(photo)
    return render_template('index.html')

@bp_upload.route('/images/<string:image>')
def showimg(image):
    path = photos.url(image)
    print(path)
    return render_template('show.html', image=path)
'''

@bp_upload.route('/images/get/<string:filename>')
def getimg(filename):
    return send_from_directory(current_app.config["UPLOADED_PHOTOS_DEST"],filename)