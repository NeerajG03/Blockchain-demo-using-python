import streamlit as st
from BlockChain import Blockchain 
from Record import PatientRecord
import datetime
import random
import atexit

def highlight_words(text, words_to_highlight):
    for word in words_to_highlight:
        text = text.replace(word, f"**{word}**")
    return text

st.set_page_config(page_title="Add/Validate", page_icon="➕")
st.sidebar.header("Add/Validate")
st.title("Add Patient Record or Validate the Blockchain")

if 'my_blockchain' not in st.session_state:
    st.session_state.my_blockchain = Blockchain()

my_blockchain = st.session_state.my_blockchain

parts = ['neck' ,'upper back' ,'lower back' ,'shoulder' ,'elbows' ,'wrist or hands' ,'hips or thighs' ,'knees' ,'ankles or feet'] 

my_expander = st.expander(label='## Add Record')
with my_expander:
    st.title("Add Patient Record")
    patient_name = st.text_input("**Patient Name**")
    age = st.slider('**Patient Age**', 0, 130, 25)
    col1, col2 = st.columns(2)
    with col1:
        feet = st.number_input("**Height in Feet**", min_value=0, step=1, max_value=8, key="feet")
    with col2:
        inches = st.number_input("**Height in Inches**", min_value=0,max_value=11, step=1, key="inches")
    weight = st.slider('**Patient Weight**', 5, 200, 10)
    record_date = str(st.date_input("**Record Date**"))
    replies = []

    with open("Data/Qs.txt", "r") as file:
        lines = file.readlines()

    st.write("**Questionaire**")
    for line in lines:
        text = line.strip()
        text = highlight_words(text, parts)
        reply = st.toggle(text)
        replies.append(reply)


    if st.button("Add Record"):
        # questions_list = questions.split('\n')
        print(replies,len(replies))
        id = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_{random.randint(0, 1000)}"
        patient_record = PatientRecord(id, patient_name,age , weight, f"{feet}'{inches}", replies, record_date)
        # patient_id, name ,age ,weight ,height , Qs, date
        my_blockchain.mine_block(patient_record)
        st.success("Record added to the blockchain!")



# st.set_page_config(page_title="Check Validity", page_icon="✅")
# st.sidebar.header("Check Validity")

# Page 2: Check Blockchain Validity
sec_expander = st.expander(label='## Check Validity')
with sec_expander:
    st.title("Check Blockchain Validity")
    if st.button("Check Validity"):
        if my_blockchain.is_valid_chain():
            st.success("Blockchain is valid.")
        else:
            st.error("Blockchain is not valid.")
