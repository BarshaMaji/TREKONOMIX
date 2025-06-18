import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trekonomix - Plan Your Trip", layout="centered")

# 🎨 Custom Styled Background
page_bg = """
<style>
body {
  background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
  background-size: cover;
  background-attachment: fixed;
}

h1, h2, h3 {
  color: white !important;
  text-shadow: 2px 2px 4px #000;
  text-align: center;
}

.stApp {
  background-color: rgba(0, 0, 0, 0.4);
  padding: 2rem;
  border-radius: 10px;
  color: white;
}

div.stButton > button {
  background-color: #FFA500;
  color: black;
  font-weight: bold;
  border-radius: 10px;
  padding: 0.5em 2em;
  transition: 0.3s;
}

div.stButton > button:hover {
  background-color: #FFD700;
  color: #000;
}

.stTextInput > div > input {
  background-color: rgba(255,255,255,0.9);
  color: black;
  font-weight: bold;
}

.stSlider > div > div {
  background-color: rgba(255,255,255,0.7);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🧡 Title and Image
st.markdown("<h1>🌍 Trekonomix</h1>", unsafe_allow_html=True)
st.image("https://source.unsplash.com/1200x400/?travel,explore,nature", use_column_width=True)

# 🧾 Form
st.markdown("### 💡 Tell us about your dream trip:")
with st.form("trip_form"):
    destination = st.text_input("📍 Destination")
    days = st.slider("🗓️ Duration (days)", 1, 30, 5)
    budget = st.number_input("💰 Budget (INR)", min_value=1000, step=500, value=20000)
    submitted = st.form_submit_button("🔍 Search")

if submitted:
    st.session_state["destination"] = destination
    st.session_state["days"] = days
    st.session_state["budget"] = budget

    st.success("Planning your trip... Hang tight! 🚀")
    components.html(
        """
        <script>
            setTimeout(function() {
                window.location.href = '/Trekonomix/pages/2_Trip_Overview';
            }, 1500);
        </script>
        """,
        height=0
    )
