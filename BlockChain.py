from Block import Block
import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    @classmethod
    def from_dict(self, cls, data):
        blockchain = cls()
        for block_data in data["chain"]:
            block = Block(
                block_data["index"],
                block_data["previous_hash"],
                block_data["timestamp"],
                block_data["data"]
            )
            block.hash = block_data["hash"]
            block.nonce = block_data["nonce"]
            blockchain.chain.append(block)
        return blockchain

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
        while not new_block.hash.startswith('0000'): # basic check to analyze (can be anyform of checking)
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