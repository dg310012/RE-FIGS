# RE-FIGS
Repeat-Enhancing Featured Ion-Guided Stoichiometry (RE-FIGS) is a complete and compact solution on DI-SPA data for more confident identifications and corresponding label free quantifications. 

## code
### RE-FIGS-ID.py
The bootstrap aggregation linear discriminant analysis based identification. The meaning of each parameter when the program is running is as follows:

* mzML_file: the mzml file path.
* SSM_file: the spectrum spectrum match results file (CsoDIAq csv format file before FDR filtering). To get this file, you need to run the original experiment using CsoDIAq, which runs with the default parameters. CsoDIAq making address to https://github.com/CCranney/CsoDIAq. Note that the original CsoDIAq code needs to be modified to output this file, as follows: 

    Find the "perform_spectra_pooling_and_analysis" function in csodiaq_identification_functions.py, whose last two lines are:
    ```
    smf.print_milestone('\nBegin Writing to File: ')
    allSpectraMatches.write_output(outFile, querySpectraFile, maccCutoff, queScanValuesDict, libIdToKeyDict, lib)
    ```
    You need to replace it with the following code:
    ```
    smf.print_milestone('\nBegin Writing to File: ')
    allSpectraMatches.write_output(outFile.replace('.csv','NoFilter.csv'), querySpectraFile, -1, queScanValuesDict, libIdToKeyDict, lib)
    allSpectraMatches.write_output(outFile, querySpectraFile, maccCutoff, queScanValuesDict, libIdToKeyDict, lib)
    ```
    After the changes are complete, reinstall CsoDIAq. CsoDIAq will then output the file, which ends with 'nofilter.csv', when it is done qualitatively.
    
* lib_file: the spectral library path. We only support .pkl files.
* start_cycle: the cycle No. starts from.
* end_cycle: the cycle No. ends with.
* good_shared_limit: the threshold to select good target.
* good_cos_sim_limit: the threshold to select good target. range(0,1).
* good_sqrt_cos_sim_limit: the threshold to select good target. range(0,1).
* good_count_within_cycle_limit: the threshold to select good target.
* tol: fragment mass error(tolerance) in ppm.
* scans_per_cycle: the scan number in each cycle.
* seed: the seed to randomly choose decoy.

### RE-FIGS_Quant.py
label free quantification on DI-SPA data. The meaning of each parameter when the program is running is as follows:

* mzML_file:the mzml file path.
* SSM_file: the final identification results file.
* lib_file: the spectral library path. We only support .pkl files.
* topN: keep topN peaks in spectral library.
* tol: fragment mass error(tolerance) in ppm.

### myms.py
Provide some functions.

### sparse_nnls.py
Provide some functions.

## jupyter
The jupyter source program in this folder is used for statistical analysis, you can see our statistical results in the output column.

## other
### mgf2pkl.py
The purpose of this file is to convert .mgf library files to .pkl format.

### pkl2mgf.py
The purpose of this file is to convert .pkl library files to .mgf format.