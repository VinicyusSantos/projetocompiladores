class Form:
    def __init__(self, title, fields):
        self.title = title
        self.fields = fields

class Field:
    def __init__(self, kind, label):
        self.kind = kind
        self.label = label
