import ollama

def generate_message(details):

    prompt = f"""
    Create a SHORT and elegant Indian wedding invitation.

    Rules:
    - Maximum 4 lines
    - Clear event list
    - Simple wedding invitation style
    - No long paragraphs

    Format example:

    With the blessings of our parents

    Priya & Rahul

    Haldi – 18 Dec
    Mehendi – 19 Dec
    Sangeet – 19 Dec Evening
    Wedding – 20 Dec
    Venue – Kolkata

    Details:
    {details}
    """

    response = ollama.generate(
        model="llama3",
        prompt=prompt
    )

    return response["response"]