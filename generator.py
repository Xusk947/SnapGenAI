import datetime
import os.path

import torch
import tqdm.tk
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

from camera import Camera

model_id = "radames/stable-diffusion-2-depth-img2img"

lov_ram = False

def save_image(image):
    image.save(f'output/output-{datetime.datetime.now()}')


class Generator():
    is_generating: bool = False

    def __init__(self):
        if lov_ram:
            self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
            self.pipe.enable_attention_slicing()
        else:
            self.pip = StableDiffusionPipeline.from_pretrained(model_id)

        self.pipe.to("cuda:0")
        self.pipe.enable_xformers_memory_efficient_attention()
        self.pipe.enable_model_cpu_offload()

        generator = torch.Generator()

    def generate(self, prompt: str, camera: Camera):
        if self.is_generating: return
        import threading

        threading.Thread(target=self.generate_and_save_image, args=(prompt, camera.get_capture(),), daemon=True).start()
        self.is_generating = True

    def generate_and_save_image(self, prompt, image):
        generator = torch.Generator()
        generator.manual_seed(0)
        save_image(self.pipe(prompt=prompt, image=image, generator=generator).images[0])
        self.is_generating = False
