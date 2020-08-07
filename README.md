# SplitTableProcessing
# Language: Python
# Input: SUMMARY (from Mothur)
# Output: PREFIX
# Tested with: PluMA 1.1, Python 3.6


PluMA plugin that takes a table of counts (output from Mothur as a .summary file)
and produces multiple output files of taxa counts, split by taxonomic classification.

The user must provide an output prefix.  If no taxonomic directories (i.e. kingdom)
are present, the output files will be prefix.kingdom.csv, prefix.phylum.csv, etc.

If the directories are present, it will use kingdom/prefix.csv, phylum/prefix.csv, etc.
