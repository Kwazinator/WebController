from flask import (
    Blueprint, render_template, request
)

import subprocess
import json

from flaskr.dataaccess.DeviceDAO import DeviceDAO

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    device = DeviceDAO().get_graph_by_id(1)
    return render_template('index.html',device=device)

@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/update', methods=('GET','POST'))
def update():
    try:
        if request.method == 'POST':
            boolean1 = request.form['boolean1']
            print(boolean1)
            if str(boolean1) == '0':
                print('false')
                subprocess.call('screen -S main -X stuff "jester.proc.vertTum.io.inputs.doorClosed = False^M"',shell=True)
            elif str(boolean1) == '1':
                print('true')
                subprocess.call('screen -S main -X stuff "jester.proc.vertTum.io.inputs.doorClosed = True^M"',shell=True)
            boolean2 = request.form['boolean2']
            integer1 = request.form['integer1']

            '''with open('data.xml') as myfile:
                data = myfile.read()'''


            DeviceDAO().update_graph_by_id(1,boolean1,boolean2,integer1)
            return 'OK'
        return '422'
    except Exception as e:
        print('error in update')
        print(e)
        return '501'
    finally:
        pass
