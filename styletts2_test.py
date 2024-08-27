from styletts2 import tts

# No paths provided means default checkpoints/configs will be downloaded/cached.
my_tts = tts.StyleTTS2()

# Optionally create/write an output WAV file.
out = my_tts.inference("Hello there, I am now a python package.", output_wav_file="test.wav")

# Specific paths to a checkpoint and config can also be provided.
other_tts = tts.StyleTTS2(model_checkpoint_path='/PATH/TO/epochs_2nd_00020.pth', config_path='/PATH/TO/config.yml')

# Specify target voice to clone. When no target voice is provided, a default voice will be used.
other_tts.inference("Hello there, I am now a python package.", target_voice_path="/PATH/TO/some_voice.wav", output_wav_file="another_test.wav")
