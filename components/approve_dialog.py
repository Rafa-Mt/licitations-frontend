import streamlit as st
from services.fetch import update_state

@st.dialog("Approve, reject, or set pending for licitation")
def approve_dialog(licitation_id):
    option = st.selectbox(
        "Set state",
        ( "Approved", "Rejected")
    )

    print(f"licitation: {licitation_id}")
    if st.button("Send state", use_container_width=True):
        if option == "Approved":
            new_state = 2
            update_state(licitation_id, new_state)
            st.toast("State updated successfully")
            st.rerun()
        elif option == "Rejected":
            new_state = 3
            update_state(licitation_id, new_state)
            st.toast("State updated successfully")
            st.rerun()