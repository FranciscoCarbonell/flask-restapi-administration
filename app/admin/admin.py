from flask import url_for, request
from flask_admin.form import ImageUploadField
from werkzeug.datastructures import FileStorage
from werkzeug.security import generate_password_hash
from app import admins, db
from jinja2 import Markup
from app.models.user import User, Roles
from app.models.player import Player
from flask_admin.contrib.sqla import ModelView
from .admin_view import LoginModelView
from flask import current_app


class ImageField(ImageUploadField):
    def __init__(self, *args , ** kwargs):
        ImageUploadField.__init__(self, base_path=current_app.config['UPLOADED_PHOTOS_DEST'],
                                  endpoint ='bp_upload.getimg', **kwargs)


class ViewPlayer(LoginModelView):
    form_widget_args = {
        'image': {
            'readonly': True
        }
    }
    def on_model_change(self, form, model, is_created):
        if form.data['image_name'] is not None:
            if isinstance(form.data['image_name'], FileStorage):
                print('entra')
                model.image = request.url_root[:-1] + url_for('bp_upload.getimg', filename=form.data['image_name'].filename)
                print(model.image)
                model.image_name = form.data['image_name'].filename

    def _list_thumbnail(self, context, model, name):
        if model.image:
            return Markup(f'<img src="{model.image}" width="100" height="120" />')
        return ''

    column_formatters = {'image': _list_thumbnail}
    form_overrides = dict(image_name=ImageField)


class ViewUser(LoginModelView):
    def on_model_change(self, form, model, is_created):
        if form.data['password'][0:13] != 'pbkdf2:sha256':
            model.password = generate_password_hash(form.data['password'])


admins.add_view(ViewPlayer(Player, db.session))
admins.add_view(ModelView(Roles, db.session))
admins.add_view(ViewUser(User, db.session))
