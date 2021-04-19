from django.forms import Form, CharField


class GitForm(Form):
    login = CharField(max_length=150)