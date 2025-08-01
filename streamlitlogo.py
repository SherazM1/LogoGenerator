from template import EMAIL_SIGNATURE_TEMPLATE
import streamlit as st
import base64
import urllib.parse

st.title("Email Signature Generator")
st.text("Hey: To use: Insert everything in the given fields, download the signature as an HTML, open it, copy and paste it into Outlook, and then if its underlined, highlight it and remove underlines. Should work for any and all signatures")

# User fields
def get_base64_img(file):
    return base64.b64encode(file.read()).decode("utf-8")

logo_file = st.file_uploader("Upload the company logo", type=["png", "jpg", "jpeg"])

if logo_file is not None:
    # Detect file type for the correct MIME type in data URL
    filetype = logo_file.type.split("/")[-1]
    base64_img = get_base64_img(logo_file)
    logo_url = f"data:image/{filetype};base64,{base64_img}"
else:
    logo_url = ""  # Or

name = st.text_input("Name")
title = st.text_input("Job Title")
email = st.text_input("Email")
website = st.text_input("Website")
address = st.text_input("Address")
maps_url = f"https://maps.google.com/?q={urllib.parse.quote(address)}"
phone = st.text_input("Phone Number")
company_website = st.text_input("Company Website")
website_url = st.text_input("Enter Website URL")

# ... more fields as needed

# Fill the template
fields = {
    "name": name,
    "title": title,
    "email": email,
    "website": website,
    "address": address,
    "phone": phone,
    "logo_url": logo_url,
    "maps_url": maps_url,
    "company_website": company_website,
    "website_url": website_url,
    
    
}
signature_html = EMAIL_SIGNATURE_TEMPLATE.format(**fields)

st.markdown("### Signature Preview")
st.markdown(signature_html, unsafe_allow_html=True)

st.download_button(
    "Download as HTML",
    data=signature_html,
    file_name="signature.html",
    mime="text/html"
)
