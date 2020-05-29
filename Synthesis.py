import numpy as np


def pianoNote(frequency):
    """
    Create A Piano Note Sound given a certain key.

    ========  =====================================
    **Arguments**
    frequecy  Key Note Frequency in HZ
    ========  =====================================

    """
    pi = np.pi
    time = np.linspace(0, 1, num= 44100)
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

    return np.array(Y)


def keyFreq(n):
    """
    Calculate frequency given key Number.
    
    =====================================
    :param n: Key Number
    :return: frequency in HZ
    """
    return 440*((np.power(2, 1./12))**(n-49))


def computeAnDn(fs, f, d, b):
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


def guitarNote(b, d, f):
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
    An, dn = computeAnDn(fs, f, d, b)

    Nt = int((fs*60)/bpm)

    for i in range(Nt):
        s = 0.0
        for x in range(len(An)):
            s += An[x] * np.cos(2.0 * np.pi * i * f * dn[x] * (x+1)/fs) * np.exp(-gama * (x+1) *i/fs)
        sj.append(round(s, 6))

    return np.array(sj, dtype=np.float32)


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
    return np.array(samples)


def createWaveTable(fs, freq):
    """
    Creates a Wave table of a certain Frequency.

     =====================================
    :param freq: A Given Frequency (HZ)
    :return: Wave TAble Array
    """
    wavetable_size = fs // int(freq)
    wavetable = (2 * np.random.randint(0, 2, wavetable_size) - 1).astype(np.float)
    return wavetable


def playSound(data, fs):
    """
    Uses Sounddevice to produce sound.

    =====================================
    :param data: numpy array
    :param fs: Sample Rate
    """
    sd.play(data, fs)
    time.sleep(1)


if __name__ == '__main__':
    import sounddevice as sd
    from scipy.io import wavfile
    import time

    fs = 44100
    f = 220.0
    d = 0.1
    b = 0.0    
    # wavfile.write("Test.wav", int(fs), note)

    # a, n = computeAnDn(fs, f, d, b)

    # note = guitarNote(b, d, keyFreq(28))
    for i in range(28, 35):
        key = pianoNote(keyFreq(i))
        sd.play(key, samplerate=fs)
        time.sleep(1)

    for i in range(28, 35):
        key = guitarNote(b, d, keyFreq(i))
        sd.play(key, samplerate=fs)
        time.sleep(1)

    for i in range(30):
        playSound(karplus_strong(createWaveTable(fs, keyFreq(i)), 2*fs), fs)

    # from oct2py import Oct2Py
    #
    # with Oct2Py() as oc:
    #     a = oc.audioplayer(key, fs)
    #     oc.play(a)

