import streamlit as st
import re
import random


def check_password_strength(password):
    score = 0
    feedback = []

    # length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 charactor long.")

        # upper & lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both upercase and lowercase letters.")

        # digital check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append(" Add at least one number (0-9).")


# special character check
    if re.search(r"\W", password):
        score += 1

    else:
        feedback.append("Include at least one special characters (!@#$%^&*).")

    # strength rating
    if score == 5:
        return "Strong Password!", [], "#28a745"

    elif score == 3:
        return "Moderate Password - Consider adding more securing features.", feedback, "#ffc107"

    else:
        return "Weak Password - Improve it using the suggestion below.", feedback, "#dc3545"


# function to generate a strong password
def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
    return "".join(random.sample(characters, 12))


# streamlit ui
st.set_page_config(page_title="Password Strength Meter",
                   page_icon="🔐", layout="centered")
st.markdown("""
       <style>
            .stApp {
               background-color:#f8f9fa;
               text-align: center;
            }
            .stTextInput {
            border-radius: 10px
            border: 1px solid #ced4da;
            padding: 10px;
            font-size: 16px;
            } 
            .stButton>button {
            background-color: #007bff;
            color:white;
            padding: 10px 15px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            }
            st.Button>button:hover {
            background-color: #0056b3;
            } 
        </style>     
""", unsafe_allow_html=True)
st.title(" 🔐 Password Strength Meter")
st.write("Enter your passward below to check its Strength")

# pasward input with toggle visibility
password = st.text_input("Enter your pasward:",
                         type="password", key="password")
show_password = st.checkbox("Show Password")

if show_password:
    st.write(f"Your Password: `{password}`")

if password:
    strength, feedback, color = check_password_strength(password)

    # show strength result wiyh colored text
    st.markdown(
        f"""<h3 style='color: {color};'>{strength}</h3>""", unsafe_allow_html=True)

    # show feedback only if password is weak ir moderate
    if feedback:
        st.write("### Suggestion to improve:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")

 # password generate button
if st.button("Generate strong Password"):
    st.success("### Suggested Strong Password:")
    st.code(generate_strong_password())
