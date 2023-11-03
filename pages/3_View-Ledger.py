import streamlit as st
from BlockChain import Blockchain 
from Record import PatientRecord

my_blockchain = st.session_state.my_blockchain

st.set_page_config(page_title="Show Ledger", page_icon="📃")
st.sidebar.header("Show Ledger")

# Page 3: Display Ledger
st.title("Blockchain Ledger")
if st.button("Show Ledger"):
    for block in my_blockchain.chain:
        st.write(f"Block {block.index} - Hash: {block.hash}")
        st.write(f"Data:\n {block.data}")
        st.write("-" * 50)