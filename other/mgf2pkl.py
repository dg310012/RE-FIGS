import numpy as np
import pandas as pd
import sys
from tqdm import tqdm
import pickle
import sys
sys.path.append('../..')
parameters = sys.argv
path = parameters[1]

f = open(path)
content = f.read()
entries = content.split('END IONS\n\n')

target = {}
decoy = {}
for entry in tqdm(entries):
    if len(entry) < 5:
        continue
    else:
        title = entry.split('TITLE=')[1].split(' ')[0]
        file = entry.split('TITLE=')[1].split(' ')[1]
        charge = int(entry.split('CHARGE=')[1].split('\n')[0][0])
        mz = float(entry.split('PEPMASS=')[1].split('\n')[0])
        seq = entry.split('SEQ=')[1].split('\n')[0]
        spectrum_string = entry.split('=')[-1].split('\n')[1:-1]
        spectrum = np.array([peak.split(' ')
                             for peak in spectrum_string]).astype('float')
        spectrum = spectrum[np.argsort(spectrum[:, 0])]
        key = (seq, charge)
        tmp_dict = {}
        tmp_dict['PrecursorMZ'] = mz
        tmp_dict['Spectrum'] = spectrum
        if 'DECOY' in title:
            decoy[key] = tmp_dict
        else:
            target[key] = tmp_dict
target.update(decoy)
with open(path.replace('.mgf', '.pkl'), 'wb')as g:
    pickle.dump(target, g)
f.close()
