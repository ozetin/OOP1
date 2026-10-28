class Poezd:
    def __init__(self, kuda, number, time):
        self.dannye = {
            "punkt": kuda,
            "number": number,
            "time": time
        }

    def get_slovar(self):
        return self.dannye