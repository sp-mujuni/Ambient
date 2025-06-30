from pydub.generators import Sine
from pydub import AudioSegment

MOOD_FREQUENCIES = {
    "relax": [432, 528],
    "focus": [417, 741],
    "love": [639, 528],
    "release": [396, 417],
    "spiritual": [852, 963],
}

def generate_ambient_tone(mood="relax", duration=10000, filename='static/tones/preview.wav'):
    freqs = MOOD_FREQUENCIES.get(mood.lower(), [432])
    combined = AudioSegment.silent(duration=duration)
    
    for freq in freqs:
        tone = Sine(freq).to_audio_segment(duration=duration).apply_gain(-5)
        combined = combined.overlay(tone)

    combined.export(filename, format='wav')
    return filename
