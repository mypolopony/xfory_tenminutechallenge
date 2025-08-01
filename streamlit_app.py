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
        "Amazon", "Netflix", "Tesla", "Apple", "Microsoft", "Nvidia", "Asana", "Calendly", "Kickstarter", "Coursera"
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
    
