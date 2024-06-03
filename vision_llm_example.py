import openai
import base64
from PIL import Image
from io import BytesIO
import aiohttp
import asyncio

# Replace with your OpenAI API key
OPENAI_API_KEY = ""

openai.api_key = OPENAI_API_KEY

async def get_image_analysis(image_path):
    # Read and encode the image
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    # Resize the image to 512x512 directly
    image = Image.open(BytesIO(image_bytes))
    resized_image = image.resize((512, 512))

    # Re-encode to base64
    buffered = BytesIO()
    resized_image.save(buffered, format=image.format)
    resized_base64 = base64.b64encode(buffered.getvalue()).decode()

    prompt = "Example this image"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{resized_base64}",
                            "detail": "high"  # Specify image quality detail
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload) as response:
            if response.status == 200:
                response_data = await response.json()
                description = response_data['choices'][0]['message']['content']
                return {"description": description}
            else:
                response_text = await response.text()
                raise Exception(f"Error from OpenAI: {response_text}")

# Example usage
image_path = 'integrated_service.png'
response = asyncio.run(get_image_analysis(image_path))
print(response)
