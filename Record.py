from json import JSONEncoder

class PatientRecord:
    def __init__(self, patient_id, name, Qs, date):
        self.patient_id = patient_id
        self.name = name
        self.generalHistory = Qs[:9]
        self.halfYearHistory = Qs[9:18]
        self.weekHistory = Qs[18:27]
        self.workInspect = Qs[29:32]
        self.awkwardMovement = Qs[32:43]
        self.handUsage = Qs[43:45]
        self.reaches = Qs[45:48]
        self.workMove = Qs[48:52]
        self.misc = Qs[52:58]
        self.hinder = Qs[58:61]
        self.attest = Qs[61]
        self.recordedOn = date

class PatientRecordEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
