from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class NotepadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=256)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Save notepad')


def form_success(endpoint, message, category="success", **url_kwargs):
    flash(message, category)
    return redirect(url_for(endpoint, **url_kwargs))


def form_error(template, form, errors=None, **context):
    for field, messages in (errors or {}).items():
        for msg in messages:
            flash(f"{field}: {msg}", "error")
    return render_template(template, form=form, **context)