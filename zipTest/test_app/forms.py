from django.forms import Form, CharField


class GitForm(Form):
    nickname = CharField(max_length=150)