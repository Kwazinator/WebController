from flask import (
    Blueprint, render_template, request
)
from flaskr.dataaccess.entities.Device import Device
import subprocess
import json

from flaskr.dataaccess.DeviceDAO import DeviceDAO

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    '''
    could add code to fetch current defaults of session and populate EX.

    response = subprocess.call('screen -S main -X stuff "jester.proc.virtTum.io.inputs??^M"',shell=True)
    json.loads(response)
    doorClosed = response['doorClosed')
    device = Device(1,name,doorClosed,otherparameters)

    '''
    device = Device(1,'device name',1,0,23) #sets defaults Device(id,name,boolean1,boolean2,integer1
    return render_template('index.html',device=device)

@bp.route('/update', methods=('GET','POST'))
def update():
    try:
        if request.method == 'POST':
            #ask for boolean1 in post request from data in ajax request in ./templates/javascript/script.js
            boolean1 = request.form['boolean1']

            #check boolean and convert to screen systemcall
            if boolean1 is '0':
                subprocess.call('screen -S main -X stuff "jester.proc.virtTum.io.inputs.doorClosed = False^M"',shell=True)
            elif boolean1 is '1':
                subprocess.call('screen -S main -X stuff "jester.proc.virtTum.io.inputs.doorClosed = True^M"',shell=True)

            boolean2 = request.form['boolean2']
            integer1 = request.form['integer1']
            return 'OK'
        return '422'
    except Exception as e:
        print('error in update')
        print(e)
        return '501'
    finally:
        pass
