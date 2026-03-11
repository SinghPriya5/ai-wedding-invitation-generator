import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap

st.title("💍 AI Wedding Invitation Generator")

# User Inputs
bride = st.text_input("Bride Name")
groom = st.text_input("Groom Name")
venue = st.text_input("Venue")

haldi = st.text_input("Haldi Date")
mehendi = st.text_input("Mehendi Date")
sangeet = st.text_input("Sangeet Date")
wedding = st.text_input("Wedding Date")

if st.button("Generate Card"):

    # Card size
    width = 1000
    height = 650

    img = Image.new("RGB",(width,height),"#FFF0F5")
    draw = ImageDraw.Draw(img)

    # Load fonts
    title_font = ImageFont.truetype("GreatVibes-Regular.ttf",70)
    text_font = ImageFont.truetype("GreatVibes-Regular.ttf",38)

    # Border
    draw.rectangle((10,10,width-10,height-10),outline="#D4AF37",width=6)

    # Couple Image
    couple = Image.open("couple.png").convert("RGB")
    couple = couple.resize((350,350))
    img.paste(couple,(40,150))

    # Invitation Message
    message = f"""
With the blessings of our parents

{bride} & {groom}

invite you to celebrate their wedding

🌼 Haldi: {haldi}
🌿 Mehendi: {mehendi}
🎶 Sangeet: {sangeet}
💍 Wedding: {wedding}

📍 Venue: {venue}
"""

    # Wrap text so it doesn't go outside image
    wrapped_text = textwrap.fill(message,width=28)

    draw.multiline_text(
        (450,120),
        wrapped_text,
        fill="#4B1E1E",
        font=text_font,
        spacing=15
    )

    st.image(img)

    # Download button
    st.download_button(
        label="Download Invitation Card",
        data=img.tobytes(),
        file_name="wedding_invitation.png",
        mime="image/png"
    )