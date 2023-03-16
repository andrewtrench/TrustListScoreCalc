import streamlit as st


def cal_attribute_score(ratio, ads_score, ssl, whois):
    score = ((((ratio / 1500) * 4) + (ads_score * 3) + (whois * 2) + (ssl * 1)) * 10)
    return score

st.text("Enter the following attributes to get the attribute score")
ratio = st.number_input("Ratio", min_value=0.0, max_value=1500.0, step=0.1)
ads_score = st.number_input("Ads Score", min_value=0.0, max_value=1.0, step=1)
whois = st.number_input("Whois", min_value=0.0, max_value=1.0, step=0.1)
ssl = st.number_input("SSL", min_value=0.0, max_value=1.0, step=1)

score = cal_attribute_score(ratio, ads_score, ssl, whois)
show_score = st.empty()
show_score.write(f"Score: {score}")

reset = st.button("Reset")
if reset:
    ratio, whois, ssl, ads_score = 0.0, 0.0, 0.0, 0.0
    show_score.write(f"Score: {score}")
