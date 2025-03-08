import re
import streamlit as st

#page_styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔑", layout="centered")

#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50% background-color: #4CFAF50; color: white, font-size: 18px; }
    .stButton button: hover { background-color: #45a049;}
</style)
    """, unsafe_allow_html=True)

#page title and description

st.title("🚀 Password Strength Meter 🔐")
st.write("Enter your password below to check its security level 🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1 #increased score by 1.
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 #increased score by 1.(from 1 to 2)
    else:
        feedback.append("❌ Password should contain **both uppercase(A-Z) and lowercase(a-z) letters**")
        
    if re.search(r"\d", password):
        score += 1 #increased score by 1.(from 2 to 3)
    else:
        feedback.append("❌ Password should contain **atleast one number (0-9)**")
        
    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1 #increased score by 1.(from 3 to 4)
    else:
        feedback.append("❌ Password should contain **atleast one special character(!@#$%^&*)**")
        
    #display password strength
    if score == 4:
        st.success("✅ **Strong Password** Your password is **strong**")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to improve your password")
    
# feedback
    if feedback:
        with st.expander(" ** Improve your password 🔍**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is **strong** 🔒")

#Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password")