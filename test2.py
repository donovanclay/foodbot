import io
import os
import warnings

from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key. https://beta.dreamstudio.ai/membership
# Click on the following link once you have created an account to be taken to your API Key. Paste it below when prompted after running the cell. https://beta.dreamstudio.ai/membership?tab=apiKeys
os.environ['STABILITY_KEY'] = 'sk-PvRC2INep84w7iMJtajedVpmTqnwDiGOCtyHfM2hOKbZ0lBS'

#@title <a name="Step 3"><font color="#FFFFFF">3. Import additional dependencies and establish our connection to the API.</font></a>



# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-v1-5", # Set the engine to use for generation. 
    # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0 stable-inpainting-v1-0 stable-inpainting-512-v2-0
)

#@title <a name="Step 4"><font color="#FFFFFF">4. Set up initial generation parameters, display image on generation, and safety warning for if the adult content classifier is tripped.</font></a>

# Set up our initial generation parameters.
answers = stability_api.generate(
    prompt="elephant dancing on a computer",
    # seed=992446758, # If a seed is provided, the resulting generated image will be deterministic.
    #                 # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
    #                 # Note: This isn't quite the case for Clip Guided generations, which we'll tackle in a future example notebook.
    # steps=30, # Amount of inference steps performed on image generation. Defaults to 30. 
    # cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
    #                # Setting this value higher increases the strength in which it tries to match your prompt.
    #                # Defaults to 7.0 if not specified.
    # width=512, # Generation width, defaults to 512 if not included.
    # height=512, # Generation height, defaults to 512 if not included.
    # samples=1, # Number of images to generate, defaults to 1 if not included.
    # # sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
    #                                              # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                 # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m)
)

# Set up our warning to print to the console if the adult content classifier is tripped.
# If adult content classifier is not tripped, save generated images.
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            display(img)