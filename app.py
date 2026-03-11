import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("💍 AI Wedding Invitation Generator")

# Inputs
bride = st.text_input("Bride Name")
groom = st.text_input("Groom Name")
venue = st.text_input("Venue")

haldi = st.text_input("Haldi Date")
mehendi = st.text_input("Mehendi Date")
sangeet = st.text_input("Sangeet Date")
wedding = st.text_input("Wedding Date")

if st.button("Generate Card"):

    width = 1000
    height = 650

    img = Image.new("RGB",(width,height),"#FFF0F5")
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = ImageFont.truetype("GreatVibes-Regular.ttf",70)
    heading_font = ImageFont.truetype("GreatVibes-Regular.ttf",45)
    text_font = ImageFont.truetype("GreatVibes-Regular.ttf",32)

    # Border
    draw.rectangle((10,10,width-10,height-10),outline="#D4AF37",width=6)

    # Heading
    draw.text((420,40),"Wedding Invitation",fill="#8B0000",font=title_font)

    # Couple image
    couple = Image.open("couple.png").convert("RGB")
    couple = couple.resize((330,330))
    img.paste(couple,(60,180))

    # Blessing text
    blessing = "With the blessings of our parents"

    draw.text((430,140),blessing,fill="#4B1E1E",font=text_font)

    # Couple names
    names = f"{bride}  &  {groom}"

    draw.text((430,180),names,fill="#8B0000",font=heading_font)

    invite = "invite you to celebrate their wedding"

    draw.text((430,230),invite,fill="#4B1E1E",font=text_font)

    # Event details
    draw.text((430,290),f"Haldi     : {haldi}",fill="#4B1E1E",font=text_font)
    draw.text((430,330),f"Mehendi   : {mehendi}",fill="#4B1E1E",font=text_font)
    draw.text((430,370),f"Sangeet   : {sangeet}",fill="#4B1E1E",font=text_font)
    draw.text((430,410),f"Wedding   : {wedding}",fill="#4B1E1E",font=text_font)

    # Venue
    draw.text((430,470),f"Venue : {venue}",fill="#8B0000",font=text_font)

    st.image(img)

    st.download_button(
        label="Download Invitation Card",
        data=img.tobytes(),
        file_name="wedding_invitation.png",
        mime="image/png"
    )