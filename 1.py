import pyaudio
import struct
import math

# Set the chunk size and sample rate
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Create the PyAudio object
p = pyaudio.PyAudio()

# Open the audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Continuously listen to sound and print the level in decibels
while True:
    # Read audio data from the stream in chunks
    data = stream.read(CHUNK)

    # Convert the audio data to a list of samples
    samples = struct.unpack(f"{CHUNK}h", data)

    # Calculate the RMS value of the samples
    rms = math.sqrt(sum([(sample / 32768) ** 2 for sample in samples]) / len(samples))

    # Convert the RMS value to decibels and print it
    db = 20 * math.log10(rms)
    print(f"Sound level: {db:.2f} dB", end='\r', flush=True)
# Stop the stream and terminate the PyAudio object
stream.stop_stream()
stream.close()
p.terminate()
