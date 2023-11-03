from json import JSONEncoder

class PatientRecord:
    def __init__(self, patient_id, name ,age ,weight ,height , Qs, date):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.date = date
        self.record = Qs
    
    def __str__(self):
        return f"""Patient ID: {self.patient_id}\n
        Name: {self.name}\n
        Weight: {self.weight}\n
        Age: {self.age}\n
        Height: {self.height}\n
        Answers: {self.record}\n
        Date: {self.date}"""

class PatientRecordEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__