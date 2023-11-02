from Block import Block
from BlockChain import Blockchain
from Record import PatientRecord,PatientRecordEncoder

my_blockchain = Blockchain()
patient1 = PatientRecord(1, "John Doe", "0101010101010101010101010101010101010101010101010101010101010101", "Prescription A")
patient2 = PatientRecord(2, "Jane Smith", "101010101010101010101010101010101010101010101010101010101010101", "Prescription B")
my_blockchain.mine_block(patient1)
my_blockchain.mine_block(patient2)
print("Blockchain is valid:", my_blockchain.is_valid_chain())
for block in my_blockchain.chain:
    print(f"Block {block.index} - Hash: {block.hash}, Data: {block.data}")