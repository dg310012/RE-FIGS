import numpy as np
import pandas as pd
import sys
from tqdm import tqdm
from bidict import bidict
from scipy import sparse
import struct
import zlib
import pickle
import sqlite3
import sys
sys.path.append('../..')
parameters = sys.argv
path = parameters[1]

with open(path, 'rb') as f:
    total = pickle.load(f)

with open(path.replace('.pkl', '.mgf'), 'w')as f:
    idx = 1
    for key in tqdm(total.keys()):
        seq = key[0]
        charge = key[1]
        f.write('BEGIN IONS\n')
        if 'DECOY-' in seq:
            title = "TITLE=DECOY_human.faims.{}.{} PROTEIN: DECOY_null\n".format(
                idx, idx)
            f.write(title)
        else:
            title = "TITLE=human.faims.{}.{} PROTEIN: SAMPLE\n".format(
                idx, idx)
            f.write(title)
        charge = "CHARGE={}+\n".format(charge)
        f.write(charge)
        mz = "PEPMASS={}\n".format(total[key]['PrecursorMZ'])
        f.write(mz)
        SEQ = "SEQ={}\n".format(seq)
        f.write(SEQ)
        scan = "SCAN={}\n".format(idx)
        f.write(scan)
        if 'DECOY-' in seq:
            protein = "PROTEIN=DECOY_null\n"
            f.write(protein)

        spc = total[key]['Spectrum']
        for peak in spc:
            line = "{:.3f} {:.2f}\n".format(peak[0], peak[1])
            f.write(line)
        f.write('END IONS\n\n')

        idx += 1
