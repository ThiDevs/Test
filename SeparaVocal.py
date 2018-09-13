from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa

import librosa.display

y, sr = librosa.load('RapLord.mp3', duration=120)


# And compute the spectrogram magnitude and phase
S_full, phase = librosa.magphase(librosa.stft(y))