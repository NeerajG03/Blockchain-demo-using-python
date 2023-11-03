import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("   # Welcome to the Blockchain Patient Record Demo! 👋")

st.sidebar.success("Select one of the tasks!")

st.markdown(
    f"""
This demo app illustrates the power of blockchain technology in managing patient records. It allows you to perform three key actions:

1. **Add Patient Records**: Create and store patient records securely in the blockchain, ensuring data integrity and immutability.
2. **Validate Blockchain**: Verify the integrity of the blockchain to ensure the authenticity of patient records.
3. **View Ledger**: Explore the complete history of patient records stored in the blockchain.

### How to Use the App

1. **Add Patient Records**: Navigate to the "Add-Validate" page to create and add new patient records. Provide details such as the patient's name, diagnosis, treatment, and date of the record.
2. **Validate Blockchain**: Go to the "Add-Validate" page to check if the blockchain is tamper-proof and that all patient records remain intact.
3. **View Ledger**: On the "View Ledger" page, you can access the entire history of patient records, allowing you to review and audit the data.

This demo showcases the advantages of blockchain technology in healthcare, offering transparency, security, and data integrity. Feel free to explore the features and experience the benefits of blockchain for managing patient records.
Start by navigating to the respective pages using the menu on the left. If you have any questions or need assistance, please don't hesitate to reach out. Enjoy the demo!

### The questions answered are as follows
- Have you ever had trouble in the past 6 months from your neck
- Have you ever had trouble in the past 6 months from your upper back
- Have you ever had trouble in the past 6 months from your lower back
- Have you ever had trouble in the past 6 months from your shoulder
- Have you ever had trouble in the past 6 months from your elbows
- Have you ever had trouble in the past 6 months from your wrist or hands
- Have you ever had trouble in the past 6 months from your hips or thighs
- Have you ever had trouble in the past 6 months from your knees
- Have you ever had trouble in the past 6 months from your ankles or feet
"""
)