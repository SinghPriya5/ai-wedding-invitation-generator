import textwrap
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from image_generator import generate_couple
from message_agent import generate_message

st.title("AI Wedding Invitation Generator")

details = st.text_input("Enter wedding details")

if st.button("Generate Card"):

    message = generate_message(details)
    message = message.replace("–", "-")

    couple_img = generate_couple()

    # Background
    img = Image.new("RGB", (1100,650), "#FFEFF2")

    draw = ImageDraw.Draw(img)

    # Load font
    font_title = ImageFont.truetype("GreatVibes-Regular.ttf",60)
    font_text = ImageFont.truetype("GreatVibes-Regular.ttf",38)

    # Border
    draw.rectangle((10,10,1090,640), outline="#D4AF37", width=8)

    # Couple image
    couple = Image.open(couple_img).convert("RGB")
    couple = couple.resize((420,420))

    img.paste(couple,(30,100))

    # Title
    draw.text((520,70), "Wedding Invitation", fill="#883DE4", font=font_title)
    wrapped_text = textwrap.fill(message, width=25)
    # Invitation text
    draw.multiline_text(
        (450,100),
        message,
        fill="#3b1f1f",
        font=font_text,
        spacing=10
    )

    st.image(img)