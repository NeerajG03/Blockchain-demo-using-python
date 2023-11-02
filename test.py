import hashlib
import time
import json
from json import JSONEncoder

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + json.dumps(self.data, cls=PatientRecordEncoder) + str(self.nonce)
        return hashlib.sha256(data.encode()).hexdigest()


class PatientRecord:
    def __init__(self, patient_id, name, diagnosis, treatment):
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis
        self.treatment = treatment

class PatientRecordEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.timestamp = int(time.time())
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def mine_block(self, patient_record):
        new_block = Block(len(self.chain), self.get_latest_block().hash, int(time.time()), patient_record)
        while not new_block.hash.startswith('0000'):  # Basic proof-of-work for simplicity
            new_block.nonce += 1
            new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        return new_block

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example usage:
if __name__ == '__main__':
    my_blockchain = Blockchain()

    # Adding patient records
    patient1 = PatientRecord(1, "John Doe", "01010101010101010101010101010101010101010101010101010101010101010101", )
    patient2 = PatientRecord(2, "Jane Smith", "Injury", "Prescription B")

    my_blockchain.mine_block(patient1)
    my_blockchain.mine_block(patient2)

    print("Blockchain is valid:", my_blockchain.is_valid_chain())
    for block in my_blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}, Data: {block.data}")
