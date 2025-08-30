import streamlit as st

# --- App State Management ---
# Use session state to track which part of the app to display.
if 'show_card' not in st.session_state:
    st.session_state.show_card = False
if 'show_pdf' not in st.session_state:
    st.session_state.show_pdf = False

# --- Page Setup and Custom Styling ---
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")
st.markdown("""
<style>
.main-container {
    background-color: #ffe6f2; /* Light pink background */
    padding: 3rem;
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
    font-family: 'Georgia', serif;
}

.title-text {
    font-size: 3em;
    font-weight: bold;
    color: #e91e63; /* Pink color */
    margin-bottom: 20px;
}

.envelope-button button {
    background-color: #880e4f; /* Darker pink */
    color: white;
    font-size: 1.5rem;
    padding: 15px 30px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.envelope-button button:hover {
    background-color: #c2185b; /* Lighter on hover */
}

.card-text {
    font-size: 1.5em;
    color: #4a148c; /* Purple color */
    font-style: italic;
    margin-top: 2rem;
    line-height: 1.5;
}

.pdf-button button {
    background-color: #4a148c; /* Purple color */
    color: white;
    font-size: 1.25rem;
    padding: 10px 20px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 2rem;
}

.pdf-button button:hover {
    background-color: #6a1b9a; /* Lighter on hover */
}

.pdf-embed-container {
    width: 100%;
    height: 800px;
    border: none;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- PDF File URL ---
# IMPORTANT: This placeholder is a public PDF link.
# Please replace it with the direct URL to your own PDF file.
# The URL must end with ".pdf" to work correctly.
pdf_url = "https://drive.google.com/file/d/1IfjZ3WzQRJJ77YBDQd9PTF2CaT3LbHPH/view?usp=sharing".replace("/view?usp=sharing", "/preview")

# --- Main App Logic ---

# Check if we should display the PDF viewer
if st.session_state.show_pdf:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title-text'>Your Special Message! 🎉</h1>", unsafe_allow_html=True)
    
    # Embed the PDF using an iframe
    st.markdown(f"""
    <iframe src="{pdf_url}" class="pdf-embed-container"></iframe>
    """, unsafe_allow_html=True)

    # Add a button to go back if needed
    if st.button("Go Back"):
        st.session_state.show_card = False
        st.session_state.show_pdf = False
        st.rerun() # Refresh the page to reset state

    st.markdown("</div>", unsafe_allow_html=True)

# Check if we should display the card with the message and button
elif st.session_state.show_card:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title-text'>Happy Birthday! 🎈</h1>", unsafe_allow_html=True)
    st.markdown("<p class='card-text'>Hope your day is filled with love, laughter, and everything that makes you happy. This little surprise is for you!</p>", unsafe_allow_html=True)
    
    # The "Click here" button to show the PDF
    if st.button("Click here to see your gift!", key="show_pdf_button"):
        st.session_state.show_pdf = True
        st.rerun() # Refresh the page to show the PDF
    st.markdown("</div>", unsafe_allow_html=True)

# Default view: the closed envelope
else:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title-text'>You've Got Mail! 🎁</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.2em; color: #4a148c;'>A special surprise is waiting for you...</p>", unsafe_allow_html=True)
    
    # The "Open the envelope" button
    if st.button("Open the Envelope", key="open_envelope_button"):
        st.session_state.show_card = True
        st.rerun() # Refresh the page to show the card
    st.markdown("</div>", unsafe_allow_html=True)
