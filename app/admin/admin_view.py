from flask import redirect
from flask_admin import AdminIndexView
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView


class LoginViewMixin(object):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect('/login')


class LoginModelView(LoginViewMixin, ModelView):
    pass


class AdminView(LoginViewMixin, AdminIndexView):
    pass