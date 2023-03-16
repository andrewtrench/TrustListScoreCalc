import streamlit as st


def cal_attribute_score(ratio, ads_score, ssl, whois):
    score = ((((ratio / 1500) * 4) + (ads_score * 3) + (whois * 2) + (ssl * 1)) * 10)
    return score

st.text("Enter the following attributes to get the URL Attribute score")
ratio = st.number_input("Ratio", min_value=0.0, max_value=1500.0, step=0.1)
ads_score = st.number_input("Ads Score", min_value=0.0, max_value=1.0, step=1.0)
whois = st.number_input("Whois", min_value=0.0, max_value=1.0, step=0.5)
ssl = st.number_input("SSL", min_value=0.0, max_value=1.0, step=1.0)

score = cal_attribute_score(ratio, ads_score, ssl, whois)
show_score = st.empty()
show_score.write(f"Score: {score}")

reset = st.button("Reset")
if reset:
    ratio, whois, ssl, ads_score = 0.0, 0.0, 0.0, 0.0
    show_score.write(f"Score: {score}")

st.text("Enter the following attributes to get the URL Quality score")
contact = st.number_input("Contact", min_value=0.0, max_value=1.0, step=1.0)
contact_confidence = st.number_input("Contact Confidence", min_value=0.0, max_value=1.0, step=0.1)
policy = st.number_input("Policy", min_value=0.0, max_value=1.0, step=1.0)
policy_confidence = st.number_input("Policy Confidence", min_value=0.0, max_value=1.0, step=0.1)
authors = st.number_input("Authors", min_value=0.0, max_value=1.0, step=1.0)
authors_confidence = st.number_input("Authors Confidence", min_value=0.0, max_value=1.0, step=0.1)
ad_indicator = st.number_input("Ad Indicator", min_value=0.0, max_value=1.0, step=1.0)
ad_indicator_confidence = st.number_input("Ad Indicator Confidence", min_value=0.0, max_value=1.0, step=0.1)

def cal_quality_score(contact, contact_confidence, policy, policy_confidence, authors, authors_confidence, ad_indicator, ad_indicator_confidence):
    quality_score = (((contact * contact_confidence) * 2) + ((policy * policy_confidence) * 4) + ((authors * authors_confidence) * 3) + ((ad_indicator * ad_indicator_confidence) * 1) * 10)

    return quality_score

quality_score = cal_quality_score(contact, contact_confidence, policy, policy_confidence, authors, authors_confidence, ad_indicator, ad_indicator_confidence)
show_quality_score = st.empty()
show_quality_score.write(f"Quality Score: {quality_score}")
quality_reset = st.button("Quality Reset")
if quality_reset:
    contact, contact_confidence, policy, policy_confidence, authors, authors_confidence, ad_indicator_confidence, ad_indicator =0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
