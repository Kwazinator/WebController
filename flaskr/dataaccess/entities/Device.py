class Device:

    def __init__(self, self_id=None, name=None, boolean1=None, boolean2=None,integer1=None):
        self.id = self_id
        self.name = name
        self.boolean1 = boolean1
        self.boolean2 = boolean2
        self.integer1 = integer1

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'boolean1': self.boolean1,
            'boolean2': self.boolean2,
            'integer1': self.integer1
        }

