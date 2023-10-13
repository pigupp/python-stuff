import numpy as np
import pyaudio
from scipy.signal import butter, sosfilt, sosfilt_zi


# settings
signal_rate = 44100 # sample rate
signal_buffer = 2**8 # buffer size
bp_order = 5 # filter order
bp_lowcut = 800 # lowcut frequency
bp_highcut = 4000 # highcut frequency


# bandpass filter
def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = fs / 2
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='bandpass', output='sos')
        return sos

# program
if __name__ == "__main__":
    # create filter
    sos = butter_bandpass(bp_lowcut, bp_highcut, signal_rate, order=bp_order)

    # set initial filter state
    bp_state = sosfilt_zi(sos)

    # apply filter to buffer and return to output
    def callback(in_data, frame_count, time_info, status):
        global bp_state
        data = np.frombuffer(in_data, dtype=np.int16) # convert data to ndarray
        out_data, bp_state = sosfilt(sos, data, zi=bp_state) # apply bandpass
        return (out_data.astype(np.int16), pyaudio.paContinue)

    # create audio stream
    pa = pyaudio.PyAudio()
    stream = pa.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=signal_rate,
        input=True,
        output=True,
        frames_per_buffer=signal_buffer,
        stream_callback=callback
    )

    # start and maintain stream
    stream.start_stream()
    while stream.is_active():
        pass
