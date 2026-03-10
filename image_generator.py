from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)

def generate_couple():

    prompt = """
    indian wedding couple illustration,
    bride wearing red lehenga,
    groom wearing sherwani,
    wedding invitation style,
    pastel colors
    """

    image = pipe(prompt).images[0]

    image.save("couple.png")

    return "couple.png"