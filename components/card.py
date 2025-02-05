import streamlit as st


def card(name: str, description: str, state: str):
    container = st.container(border=True)

    container.header(name)
    left, right = container.columns([0.8, 0.2])
    left.subheader(description)
    match state:
        case "approved": right.success(f"Approved", icon=':material/check_circle')
        case "rejected": right.error(f"Rejected")
        case "pending": right.info(f"Pending")

    return container
