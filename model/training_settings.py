import keying_stats as ks

training_settings = {
    # signal properties
    'snr': {'low': -16, 'high': 50},
    'wpm': {'low':12, 'high':48},
    'doppler_spread': {'low':0.1, 'high':3},    
    'keying_style': [[ks.KeyingStyle.HandKey, ks.KeyingStyle.Paddle, ks.KeyingStyle.Computer], [0.25,0.5,0.25]], 
    'pitch_error': {'low':-30, 'high':30},
    'noise_floor': {'low':-20, 'high':20},
    
    # spectrogram properties
    'frame_step': 64, # 64 => 93.75 ms
    'window_function_length': 300,

    # tech consts
    'spectrogram_width': 512,
    'spectrogram_height': 22,
    'overlap_margin': 3,
    'continuous': True,
    'fft_length': 512, # 512 => 11.7 Hz, 

    # training properties
    'batch_size': 4,
    'batch_count': int((30 * 60 * 6000) / (64 * (256 * 2))),
    'randomize_every_batches': 5
}    
