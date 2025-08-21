import openai
import requests
from PIL import Image
from io import BytesIO

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'

def generate_image(prompt):
    # Use DALL·E to generate an image based on the prompt
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # Generate 1 image
        size="1024x1024"  # Image size
    )
    return response['data'][0]['url']

def display_image(image_url):
    # Fetch the image from the URL
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()

if __name__ == "__main__":
    # Specify the prompt for Snoop Dogg's image
    prompt = "portrait of Snoop Dogg"
    image_url = generate_image(prompt)
    display_image(image_url)
