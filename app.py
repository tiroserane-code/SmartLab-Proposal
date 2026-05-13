import streamlit as st
import datetime

# --- SETUP ---
st.set_page_config(page_title="Manual Lab Scanner", layout="centered")

if "logs" not in st.session_state:
    st.session_state.logs = []

# --- MAIN UI ---
st.title("📸 Manual Recognition & Tagging")
st.info("Point camera -> Take Photo -> Type Name -> Save")

# 1. LIVE CAMERA VIEW
img_file = st.camera_input("Scanner View")

if img_file:
    st.image(img_file, caption="Captured Image", width=300)
    
    # 2. MANUAL INPUT FIELDS
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Category", ["Student Attendance", "Kitchen Item"])
    
    with col2:
        name_input = st.text_input(f"Enter Name (e.g., Spoon or Irose)")

    # 3. SAVE BUTTON
    if st.button("📌 Tag and Log to System"):
        if name_input:
            timestamp = datetime.datetime.now().strftime("%I:%M %p")
            entry = {
                "Time": timestamp,
                "Category": category,
                "Label": name_input
            }
            st.session_state.logs.append(entry)
            st.success(f"Logged: {name_input} as {category}")
        else:
            st.error("Please enter a name before logging.")

# --- DATA TABLE ---
st.divider()
st.subheader("📊 Session Logs (Discussion Summary)")

if st.session_state.logs:
    # Display the logs in a clean table
    st.table(st.session_state.logs)
    
    # Admin Email Section
    if st.button("✉️ Send this Log to tiroserane@gmail.com"):
        st.write("Preparing email for Irose Rane Tupaz...")
        st.success("Report Sent!")
else:
    st.write("No items tagged yet. Use the camera above.")

# --- ADMIN SIDEBAR ---
with st.sidebar:
    st.header("Admin Controls")
    if st.button("Clear All Logs"):
        st.session_state.logs = []
        st.rerun()
