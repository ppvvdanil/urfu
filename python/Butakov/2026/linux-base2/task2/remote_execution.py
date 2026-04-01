import shutil
import subprocess
import sys

from flask import Flask
from flask import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['WTF_CSRF_ENABLED'] = False


class CodeForm(FlaskForm):
    code = StringField(validators=[DataRequired()])
    timeout = IntegerField(validators=[DataRequired(), NumberRange(min=1, max=30)])


def run_python_code_in_subproccess(code: str, timeout: int):
    cmd = [sys.executable, '-c', code]
    if shutil.which('prlimit'):
        cmd = ['prlimit', '--nproc=1:1', *cmd]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=False,
    )

    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        details = (stdout + stderr).strip()
        message = f'Исполнение кода не уложилось в {timeout} сек.'
        if details:
            message = f'{message}\n{details}'
        return False, message

    return True, (stdout + stderr).strip()


@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if not form.validate_on_submit():
        return jsonify({'errors': form.errors}), 400

    code_data = form.code.data
    timeout_data = form.timeout.data
    if code_data is None or timeout_data is None:
        return jsonify({'errors': {'form': ['Invalid form data']}}), 400

    is_ok, output = run_python_code_in_subproccess(code_data, int(timeout_data))
    if is_ok:
        return jsonify({'result': output}), 200
    return jsonify({'error': output}), 408


if __name__ == '__main__':
    app.run(debug=True)
