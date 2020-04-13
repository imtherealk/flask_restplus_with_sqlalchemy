from flask_wtf import FlaskForm as _Form


class Form(_Form):
    class Meta:
        csrf = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
