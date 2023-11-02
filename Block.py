import hashlib
import json
from Record import PatientRecordEncoder

class Block:
    '''
    Class that represents the block that can be entered into the blockchain
    '''
    def __init__(self, index, previous_hash, timestamp, record, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = record
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + json.dumps(self.data, cls=PatientRecordEncoder) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()
    
