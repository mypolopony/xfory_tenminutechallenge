import nltk
import streamlit as st
import random
from nltk.corpus import words

# Download required NLTK data
@st.cache_data
def download_nltk_data():
    nltk.download('words', quiet=True)
    return True

download_nltk_data()

# --- Generate obscure plural nouns ---
def pluralize(noun):
    if noun.endswith('y') and noun[-2] not in 'aeiou':
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'


if __name__ == "__main__":
    # nltk.download('words', quiet=True)
    all_words = [w.lower() for w in words.words() if w.isalpha() and len(w) >= 4]
    sampled_nouns = random.sample(all_words, 500)
    plural_nouns = sorted(set(pluralize(w) for w in sampled_nouns))

    # --- Tech companies ---
    TECH_COMPANIES = [
        "Uber", "Airbnb", "Spotify", "Stripe", "Coinbase", "Slack", "Zoom", "Tinder", "Robinhood", "Notion",
        "Figma", "DoorDash", "Instacart", "Lyft", "Shopify", "Pinterest", "Reddit", "Square", "Dropbox", "Snapchat",
        "YouTube", "Twitch", "GitHub", "OpenAI", "Palantir", "Salesforce", "Twitter", "Facebook", "LinkedIn", "Google",
        "Amazon", "Netflix", "Tesla", "Apple", "Microsoft", "Nvidia", "Asana", "Calendly", "Kickstarter", "Coursera",
        "Meta", "WhatsApp", "Discord", "Yelp", "Quora", "Medium", "Wix", "Squarespace", "WeWork",
        "Robinhood", "Plaid", "Stripe Atlas", "Gusto", "Canva", "Notion Labs", "Zapier", "Webflow", "Airtable",
        "Grammarly", "Duolingo", "Headspace", "Calm", "Fitbit", "Peloton", "Oculus", "Roku", "Sonos", "Nest",
        "Ring", "GoPro", "Bumble", "Hinge", "Yik Yak", "Clubhouse", "Patreon", "Substack", "Trello", "Basecamp",
        "Monday.com", "ClickUp", "Jira", "Confluence", "GitLab", "Bitbucket", "Heroku", "Vercel", "Netlify",
        "Cloudflare", "DigitalOcean", "Linode", "AWS Lambda", "Azure Functions", "Google Cloud Functions",
        "Firebase", "Twilio", "SendGrid", "Mailchimp", "HubSpot", "Zoho", "SalesLoft", "Outreach", "Drift",
        "Intercom", "Zendesk", "Freshdesk", "Help Scout", "Typeform", "SurveyMonkey", "Slack Connect", "Microsoft Teams",
        "Google Meet", "Cisco Webex", "BlueJeans", "GoToMeeting", "Jitsi", "Discord",
        "Telegram", "Signal", "Viber", "WhatsApp Business", "Line", "WeChat", "KakaoTalk", "Snapchat Ads",
        "TikTok Ads", "Pinterest Ads", "Reddit Ads", "Quora Ads", "Yandex Direct", "Bing Ads", "Amazon Advertising",
        "Facebook Ads Manager", "Google AdWords", "AdRoll", "Taboola", "Outbrain", "Criteo", "AdColony",
        "Unity Ads", "Chartboost", "IronSource", "AppLovin", "Vungle", "AdMob", "Facebook Audience Network",
        "Google AdSense", "Media.net", "PropellerAds", "PopAds", "AdMaven", "Adsterra", "ExoClick", "TrafficJunky",
        "Clickadu", "AdCash", "Adsterra", "AdSupply", "AdClickMedia", "AdHitz", "BidVertiser", "RevenueHits",
        "AdMingle", "AdBrite", "Adblade", "Adknowledge", "AdGear", "Adform", "Smaato", "InMobi", "Millennial Media",
        "MoPub", "Tapjoy", "Chartboost", "Leadbolt", "AdColony", "Unity Ads", "IronSource", "AppLovin",
        "Vungle", "AdMob", "Facebook Audience Network", "Google AdSense", "Media.net", "PropellerAds", "PopAds",
        "AdMaven", "Adsterra", "ExoClick", "TrafficJunky", "Clickadu", "AdCash", "Adsterra", "AdSupply",
        "AdClickMedia", "AdHitz", "BidVertiser", "RevenueHits", "AdMingle", "AdBrite", "Adblade", "Adknowledge",
        "AdGear", "Adform", "Smaato", "InMobi", "Millennial Media", "MoPub", "Tapjoy", "Leadbolt",
        "AdColony", "Unity Ads", "IronSource", "AppLovin", "Vungle", "AdMob", "Facebook Audience Network",
        "Google AdSense", "Media.net", "PropellerAds", "PopAds", "AdMaven", "Adsterra", "ExoClick", "TrafficJunky",
        "Clickadu", "AdCash", "Adsterra", "AdSupply", "AdClickMedia", "AdHitz", "BidVertiser", "RevenueHits",
        "AdMingle", "AdBrite", "Adblade", "Adknowledge", "AdGear", "Adform", "Smaato", "InMobi",
        "Millennial Media", "MoPub", "Tapjoy", "Leadbolt", "AdColony", "Unity Ads", "IronSource", "AppLovin",
        "Vungle", "AdMob", "Facebook Audience Network", "Google AdSense", "Media.net", "PropellerAds", "PopAds",
        "AdMaven", "Adsterra", "ExoClick", "TrafficJunky", "Clickadu", "AdCash", "Adsterra", "AdSupply",
        "AdClickMedia", "AdHitz", "BidVertiser", "RevenueHits", "AdMingle", "AdBrite", "Adblade", "Adknowledge",
        "AdGear", "Adform", "Smaato", "InMobi", "Millennial Media", "MoPub", "Tapjoy", "Leadbolt"
    ]

    # --- Streamlit UI ---
    st.set_page_config(page_title="X for Y Generator", page_icon="🤖")
    st.title("🚀 It's like the X for Y Generator")
    st.markdown("Generate startup-style analogies like **'Uber for Cats'** or **'Spotify for Grandmas'**.")

    # Automatically generate combination on page load
    x = random.choice(TECH_COMPANIES)
    y = random.choice(plural_nouns)
    st.markdown(f"### 🌈 It's like the **{x}** for **{y}**.")
    
    # Add a refresh button to generate a new combination
    if st.button("🔁 Generate Another"):
        st.rerun()
    
    st.image("img/arjun.png", caption="a strong warrior")
    st.image("img/abhishek.png", caption="a beautiful milk")
    
