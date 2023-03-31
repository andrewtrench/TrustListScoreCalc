import streamlit as st


def cal_attribute_score(ratio, ads_score, ssl, whois):
    score = ((((ratio / 1500) * 4) + (ads_score * 3) + (whois * 2) + (ssl * 1)) * 10)
    return score


st.title("TrustList URL Score Calculator")
st.text("Play with the following attributes to see the effect of the inputs on URL Attribute score")

st.text("Ratio is between 0 and 1500. Eg New York Times is around 1200 with 6bn links and 350m domains")
ratio = st.number_input("Incoming links: referring sites ratio between 0-1500", min_value=0.0, max_value=1500.0, step=0.1)

#st.text("Ads Score is between 0 and 1 ie. True or False")
ads_score = st.number_input("Has ads.txt? Ads Score is either 0 or 1 (True or False)", min_value=0.0, max_value=1.0, step=1.0)

#st.text("Whois is between 0, 0.5 and 1 ie. 0 if no record, 0.5 if date < 1 year, 1 if date > 1 year")
whois = st.number_input("Whois creation date < 1 year old? Whois 0 = none, 0.5 = date < 1 year, 1 = date > 1 year", min_value=0.0, max_value=1.0, step=0.5)

#st.text("SSL is between 0 and 1 ie. True or False")
ssl = st.number_input("Has SSL certificate and is connectable? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)

score = cal_attribute_score(ratio, ads_score, ssl, whois)
show_score = st.empty()
show_score.write(f"Attributes Score/100: {score}")

reset = st.button("Reset")
if reset:
    ratio, whois, ssl, ads_score = 0.0, 0.0, 0.0, 0.0
    show_score.write(f"Score: {score}")

st.text("Play with the following attributes to see the effect of the inputs on URL Quality score")

#st.text("Contact is either 0 and 1 ie. True or False")
contact = st.number_input("Has a quality Contact page? Contact 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)

#st.text("Contact Confidence is between 0 and 1 eg. 0.3")
contact_confidence = st.number_input("Contact Confidence 0 to 1 eg 0.3", min_value=0.0, max_value=1.0, step=0.1)

#st.text("Policy is either 0 and 1 ie. True or False")
policy = st.number_input("Has a policy page of some sort? Policy 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)

#st.text("Policy Confidence is between 0 and 1 eg. 0.3")
policy_confidence = st.number_input("Policy Confidence 0 to 1 eg 0.3", min_value=0.0, max_value=1.0, step=0.1)

#st.text("Authors is either 0 and 1 ie. True or False")
authors = st.number_input("We can identify Authors? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)

#st.text("Authors Confidence is between 0 and 1 eg. 0.3")
authors_confidence = st.number_input("Authors Confidence 0 to 1 eg 0.3", min_value=0.0, max_value=1.0, step=0.1)

#st.text("Ad Indicator is either 0 and 1 ie. True or False")
ad_indicator = st.number_input("Distinguishes between Ads and Editorial? Ad Indicator 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)

#st.text("Ad Indicator Confidence is between 0 and 1 eg. 0.3")
ad_indicator_confidence = st.number_input("Ad Indicator Confidence 0 to 1 eg 0.3", min_value=0.0, max_value=1.0, step=0.1)

ad_density_above_45_score = st.number_input("Ad Density Above 45? Score 0 or 1 eg 0.3", min_value=0.0, max_value=1.0, step=1.0)

def cal_quality_score(contact, contact_confidence, policy, policy_confidence, authors, authors_confidence, ad_indicator,
                      ad_indicator_confidence, ad_density_above_45_score):
    '''Calculate the quality score of a URL. Where there is a confidience score multiply the attribute by the confidence score. ie
    a quality contact page exists = 1 * 0.9 (if that was the confidence score.This will hopefully introduce some granularity to the
    quality score. The ad_density_above_45_score is a binary score of 0 or 1. If the ad density is above 45% then the score is 1 and 0 if below.
    The weighting of minus 1 is to ensure if has a significant impact on the quality score.'''

    quality_score = ((((contact * contact_confidence) * 2) + ((policy * policy_confidence) * 4) + (
                (authors * authors_confidence) * 3) + ((ad_indicator * ad_indicator_confidence) * 1) + (ad_density_above_45_score * -1)) * 10)

    return quality_score


quality_score = cal_quality_score(contact, contact_confidence, policy, policy_confidence, authors, authors_confidence,
                                  ad_indicator, ad_indicator_confidence, ad_density_above_45_score)
show_quality_score = st.empty()
show_quality_score.write(f"Quality Score /100: {quality_score}")
quality_reset = st.button("Quality Reset")
if quality_reset:
    contact, contact_confidence, policy, policy_confidence, authors, authors_confidence, ad_indicator_confidence, ad_indicator, ad_density_above_45_score = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0



st.text("Play with the following attributes to see the effect of the inputs on human review of the site")


quality_contact = st.number_input("Quality Contact Page? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)
policy_content = st.number_input("Quality Policy Page? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)
quality_authors = st.number_input("Quality Authors? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)
quality_ad_indicator = st.number_input("Quality Ad Indicator? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)
site_subjective_risk = st.number_input("Site Subjective Risk? 0 or 1, True or False", min_value=0.0, max_value=1.0, step=1.0)

def cal_human_quality_score(quality_contact, policy_content, quality_authors, quality_ad_indicator, site_subjective_risk):
    '''Calculate the quality score of a URL based on human review with appropriate weightings.'''

    human_quality_score = (((quality_contact * 2) + (policy_content * 4) + (quality_authors * 2) + (quality_ad_indicator * 1) + (site_subjective_risk*1)) * 10)

    return human_quality_score

human_review_score = cal_human_quality_score(quality_contact, policy_content, quality_authors, quality_ad_indicator, site_subjective_risk)

show_human_quality_score = st.empty()
show_human_quality_score.write(f"Human Review Score /100: {human_review_score}")
human_quality_reset = st.button("Human Review Reset")
if human_quality_reset:
    quality_contact, policy_content, quality_authors, quality_ad_indicator, site_subjective_risk = 0.0, 0.0, 0.0, 0.0, 0.0
