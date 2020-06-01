import numpy as np
import simpleaudio as sa
import time


def piano_note(frequency):
    """
    Create A Piano Note Sound given a certain key.

    ========  =====================================
    **Arguments**
    frequecy  Key Note Frequency in HZ
    ========  =====================================

    """
    pi = np.pi
    time = np.linspace(0, 1, num=44100)
    Y = np.sin(2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time)

    # Adding overnotes

    Y += np.sin(2 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 2
    Y += np.sin(3 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 4
    Y += np.sin(4 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 8
    Y += np.sin(5 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 16
    Y += np.sin(6 * 2 * pi * frequency * time) * np.exp(-0.0004 * 2 * pi * frequency * time) / 32

    # Increasing Sound Saturation
    Y += Y * Y * Y

    # Saturating Sound Quatlity
    Y *= 1 + 16 * time * np.exp(-6 * time)

    # Making Sure the highest value is in 16 bit range
    Y = Y * (2 ** 15 - 1) / np.max(np.abs(Y))

    return np.array(Y, dtype=np.int16)


def key_freq(n):
    """
    Calculate frequency given key Number.
    
    =====================================
    :param n: Key Number
    :return: frequency in HZ
    """
    return 440*((np.power(2, 1./12))**(n-49))


def compute_an_dn(fs, f, d, b):
    """
    Compute Vibration Spectrum of Strings.
    
    ======================================
    :param fs: Sampling Frequency.
    :param f:  Key Note Frequency (Base Note).
    :param d: Pluck position along string over
              string length.
    :param b: String Stiffness 
    :return: Array of calculated spectrum 
    """
    nharm = int(fs//(2.0*f))
    print(nharm)
    An = []
    dn = []

    for i in range(nharm):
        i += 1
        tmp = (2/((np.pi**2)*(i**2) * d*(1-d))) * np.sin(i*np.pi*d)
        An.append(round(tmp, 4))
        tmp = np.sqrt(1.0 + (i**2)*(b**2 + 10**-8))
        dn.append(round(tmp, 4))
    return np.array(An, dtype=np.float32), np.array(dn, dtype=np.float32)


def guitar_note(b, d, f):
    """
    Compute Guitar Amplitudes. 
    
    =====================================
    :param b: String Stiffness 
    :param d: Pluck position along string over
              string length.
    :param f: Note Frequency 
    :return: Array of computed Amplitudes
    """
    sj = []
    gama = 1.7

    bpm = 80
    fs = 44100
    An, dn = compute_an_dn(fs, f, d, b)

    Nt = int((fs*60)/bpm)

    for i in range(fs):
        s = 0.0
        for x in range(len(An)):
            s += An[x] * np.cos(2.0 * np.pi * i * f * dn[x] * (x+1)/fs) * np.exp(-gama * (x+1) *i/fs)
        sj.append(round(s, 6))

    # Mapping range to 16 bit
    sj = sj * (2 ** 15 - 1) / np.max(np.abs(sj))
    return np.array(sj, dtype=np.int16)


def karplus_strong(wavetable, n_samples):
    """Synthesizes a new waveform from an existing wavetable, modifies last sample by averaging."""
    samples = []
    current_sample = 0
    previous_value = 0
    while len(samples) < n_samples:
        wavetable[current_sample] = 0.5 * (wavetable[current_sample] + previous_value)
        samples.append(wavetable[current_sample])
        previous_value = samples[-1]
        current_sample += 1
        current_sample = current_sample % wavetable.size

    samples = np.array(samples)

    # Mapping to 16bit range
    samples = samples * (2 ** 15 - 1) / np.max(np.abs(samples))
    return samples.astype(np.int16)


def create_wave_table(fs, freq):
    """
    Creates a Wave table of a certain Frequency.

     =====================================
    :param freq: A Given Frequency (HZ)
    :return: Wave TAble Array
    """
    wave_table_size = fs // int(freq)
    wave_table = (100 * np.random.randint(0, 10, wave_table_size) - 1).astype(np.float) / 10
    return wave_table


def play_sound(data, fs):
    """
    Uses Sounddevice to produce sound.

    =====================================
    :param data: numpy array
    :param fs: Sample Rate
    """
    sa.play_buffer(data, len(data.shape), 2, fs)
    time.sleep(1)


if __name__ == '__main__':
    fs = 44100
    f = 220.0
    d = 0.1
    b = 0.0
    # a, n = computeAnDn(fs, f, d, b)

    for i in range(28, 45):
        key = piano_note(key_freq(i))
        play_sound(key, fs)

    # guitar sounds are ranged from 82 HZ to 320 Hz
    for i in range(20, 45, 4):
        print(key_freq(i))
        play_sound(karplus_strong(create_wave_table(fs, key_freq(i)), fs), fs)

    #
    # for i in range(28, 35):
    #     key = guitar_note(b, d, key_freq(i))
    #     play_sound(key, fs)
