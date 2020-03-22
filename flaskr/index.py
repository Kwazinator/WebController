from flask import (
    Blueprint, render_template, request
)
from flaskr.dataaccess.DeviceDAO import DeviceDAO
import json
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
            boolean2 = request.form['boolean2']
            integer1 = request.form['integer1']
            DeviceDAO().update_graph_by_id(1,boolean1,boolean2,integer1)
            return 'OK'
        return '422'
    except Exception as e:
        print('error in update')
        print(e)
        return '501'
    finally:
        pass
