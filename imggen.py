import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from dotenv import load_dotenv
load_dotenv()

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://beta.dreamstudio.ai/membership

# Click on the following link once you have created an account to be taken to your API Key.
# https://beta.dreamstudio.ai/membership?tab=apiKeys

# Paste your API Key below.

os.environ['STABILITY_KEY'] = os.getenv('STABILITY_KEY')

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    # key=os.getenv("STABILITY_KEY"),
    verbose=True, # Print debug messages.
    engine="stable-diffusion-768-v2-1",
    # engine="stable-diffusion-v1-5", # Set the engine to use for generation. 
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0 
    # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)

def make_image(input):
    # the object returned is a python generator
    answers = stability_api.generate(
        prompt= input,
        cfg_scale=5.0, 
        steps=30  # defaults to 50 if not specified
    )
    # iterating over the generator produces the api response
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                # img = Image.open(io.BytesIO(artifact.binary))
                # img.show()
                img = Image.open(io.BytesIO(artifact.binary))
                # return img.resize((250, 250))  # I think this returns a Jpeg
                img.save("temp.png") 
