from transformers import AutoTokenizer, AutoModelForTextToWaveform
# import torch
# from os import environ
# environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:256"

# These lines are commented because my GPU does not have enough memory to compute.
# When run on any device with bigger GPU, then I could enable this.

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# torch.cuda.empty_cache()
# model.to(device)

# copy the musicgen-small model into "project root" directory. else it won't work.
tokenizer = AutoTokenizer.from_pretrained("musicgen-small", do_sample=True, local_files_only=True)

# Load model directly
model: AutoModelForTextToWaveform = AutoModelForTextToWaveform.from_pretrained("musicgen-small", do_sample=True, local_files_only=True)

# the frame_rate of model we have considered 51.2 till now.
frame_rate = model.config.audio_encoder.frame_rate

#sampling rate of model
sampling_rate = model.config.audio_encoder.sampling_rate

print("\nModel has been imported from model.py successfully!\n")