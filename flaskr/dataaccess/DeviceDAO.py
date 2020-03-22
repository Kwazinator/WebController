from flaskr.db import get_db
from flaskr.dataaccess.entities.Device import Device

class DeviceDAO:

    def __init__(self):
        pass

    def get_graph_by_id(self,id):
        try:
            db = get_db()
            cursor = db.cursor()
            row = cursor.execute('SELECT * FROM device WHERE id=?', (id,)).fetchone()
            return Device(row[0], row[1], row[2], row[3],row[4])
        except Exception as e:
            print('error in get_graph_item')
            print(e)
        finally:
            pass

    def update_graph_by_id(self, id, boolean1,boolean2,integer1):
        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute('UPDATE device SET boolean1=?, boolean2=?, integer1=? WHERE id=?',(boolean1,boolean2,integer1,id))
            db.commit()
        except Exception as e:
            print('error in update_graph_by_id')
            print(e)
            return None
        finally:
            pass