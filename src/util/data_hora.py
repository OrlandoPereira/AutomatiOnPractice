from datetime import datetime

class DataHora:
    def __init__(self):
        self.data_hora = datetime

    def now(self):
        return str(self.data_hora.now().strftime("DT%Y%m%d-HR%H%M%S-"))

