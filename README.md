# English character bigram frequencies and transitional frequencies

For use in, e.g., creating controlled stimuli for artificial language learning experiments with English-speaking participants, or computing corpus-based transitional probabilities between English bigrams.

Created by Elizabeth Pankratz in 2022 based on web corpus data from [ENCOW16A-NANO](https://www.webcorpora.org).


## Illustration

This is an excerpt from the matrix containing transitional frequencies between character bigrams:


|    	| zr 	| bu  	| mn 	| ke  	| hv 	| mo  	|
|----	|----	|-----	|----	|-----	|----	|-----	|
| zr 	| 0  	| 0   	| 0  	| 0   	| 0  	| 0   	|
| bu 	| 0  	| 3   	| 1  	| 25  	| 0  	| 6   	|
| mn 	| 0  	| 5   	| 0  	| 0   	| 0  	| 1   	|
| ke 	| 0  	| 100 	| 1  	| 16  	| 0  	| 266 	|
| hv 	| 0  	| 0   	| 0  	| 0   	| 0  	| 1   	|
| mo 	| 0  	| 2   	| 2  	| 210 	| 0  	| 12  	|
| aa 	| 0  	| 22  	| 3  	| 8   	| 0  	| 44  	|

For the transition from syllable $i$ to syllable $j$, this matrix shows the transitional frequency in cell $[i, j]$.
For instance, the transitional frequency from "mo" to "ke" appears 210 times, e.g., in words like "smoke".


## What is this good for?

If you are running artificial language learning experiments with English-speaking participants and want to limit the influence of their prior linguistic knowledge on your task, then it may be useful to ensure that your artificial language does not contain bigrams or bigram transitions that resemble those in English.

- With the frequency list of CV syllables, you can restrict your choice of syllables to a particular frequency range.
- With the matrix of co-occurrence frequencies, you can create words using syllable sequences that appear together with particular frequencies.


## Contents

**The data:**

- `data/bigram_freq_mtx.csv`: Matrix of transitional frequencies.
- `data/bigram_freqs.csv`: Frequency of each observed bigram overall.


**The code used to create this data:**

- `code/1_get_encow_sents.py`: A Python 2 script run on the SeaCOW server in fall 2022. Queries the web corpus for all sentences belonging to boilerplate class `a` or `b` (that is, actual content and not just the peripheral junk that's often found on websites) and in documents of badness class `a` or `b` (that is, well-formed standard English).

  - In: Nothing.
  - Out: `data/encow_sents.csv` (gitignored due to size; contains 351,392 sentences)

- `code/2_count_bigrams.ipynb`: Gets all character bigrams from subset of ENCOW data. Counts them and all transitions between them.

  - In: `data/encow_sents.csv`
  - Out: 
    - `data/bigram_freqs.csv`
    - `data/bigram_freq_mtx.csv`

