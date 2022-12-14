# RE-FIGS
Repeat-Enhancing Featured Ion-Guided Stoichiometry (RE-FIGS) is a complete and compact solution on DI-SPA data for more confident identifications and corresponding label free quantifications. 

## code running instructions
    1. git clone https://github.com/dg310012/RE-FIGS.git
    2. use pip to install the associated dependency libraries
    3. switch to the code folder
    4. run the RE-FIGS-ID.py to do the identification (the parameters for execution are described later)
    5. run the RE-FIGS_Quant.py to do the quantification (the parameters for execution are described later)

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
    After the changes are complete, reinstall CsoDIAq. CsoDIAq will then output the file, which ends with 'nofilter.csv', when peptide identification is complete.
    
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

Here is an example of a qualitative program execution:
```
python RE-FIGS-ID.py ../mzml/480_20210929_Hela_1ug_noRT_FAIMS_30to80_120ms_40min_250nL_01.mzML ../sample_trap_decoy_result/CsoDIAq-file1_480_20210929_Hela_1ug_noRT_FAIMS_30to80_120ms_40min_250nL_01_correctedNoFilter.csv ../lib/human.faims.fixed.download.sample.130941.RefEntrapment.psps23.RefDecoy.psps13.pkl 1 14 7 0.8 0.9 5 20 1500 13
```
### RE-FIGS_Quant.py
label free quantification on DI-SPA data. The meaning of each parameter when the program is running is as follows:

* mzML_file:the mzml file path.
* SSM_file: the final identification results file.
* lib_file: the spectral library path. We only support .pkl files.
* topN: keep topN peaks in spectral library.
* tol: fragment mass error(tolerance) in ppm.

Here is an example of quantitative program execution:
```
python RE-FIGS_Quant.py ../mzml/480_20210929_Hela_1ug_noRT_FAIMS_30to80_120ms_40min_250nL_01.mzML ../sample_trap_decoy_result/CsoDIAq-file1_480_20210929_Hela_1ug_noRT_FAIMS_30to80_120ms_40min_250nL_01_correctedNoFilter_withFeature_13cycle_7_5_LDA_ID.csv ../lib/human.faims.fixed.download.sample.130941.RefEntrapment.psps23.RefDecoy.psps13.pkl 10 20
```
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

## sh
### identification_DI-SPA-MCF7.sh
Shell script files used to generate RE-FIGS qualitative result files for MCF7 peptide samples.

### identification_Hela.sh
Shell script files used to generate RE-FIGS qualitative result files for Hela data.

### identification_ecoli-human-yeast.sh
Shell script files used to generate RE-FIGS qualitative result files for samples of three species.

### quantification_DI-SPA-MCF7.sh
Shell script files used to generate RE-FIGS quantitative result files for MCF7 peptide samples.

### quantification_Hela.sh
Shell script files used to generate RE-FIGS quantitative result files for Hela data.

### quantification_ecoli-human-yeast.sh
Shell script files used to generate RE-FIGS quantitative result files for samples of three species.