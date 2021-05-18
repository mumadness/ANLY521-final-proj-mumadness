Evaluating Google Translate for select language pairs using chrF++ metric
-------------------------------------------------------------------------
Please run ttest.py for a statistical evaluation of the translated
chrF++ scores. The example commands below will run on the hypothesis
translation files `*hyp.en` and the reference translations `*short.en`  

**Parameters**
| Parameter flag | explanation                                        |
|:---------------|:---------------------------------------------------|
| -srcl1         | source language 1; Required                        |
| -srcl2         | source language 2; Required                        |
| -nc            | character n-gram length; Default 6                 |
| -nw            | word n-gram length; Default 2                      |
| -b             | beta; assigns beta times more importance to recall |
| -s             | show sentence-level scores                         |

| language code | language |
|:--------------|:---------|
| it            | Italian  |
| de            | German   |
| el            | Greek    |
| fi            | Finnish  |
| nl            | Dutch    |

Example usage  
`python ttest.py -srcl1 it -srcl2 de`  
*Runs a ttest analysis with Italian and German as source languages with
default parameters*

`python ttest.py -srcl1 it -srcl2 el -nc 8 -nw 1`  
*Runs a ttest analysis with Italian and Greek as source languages.
Modifying parameters such that considers character 8-gram and word
unigram*

`python ttest.py -srcl1 nl -srcl2 fi -s`  
*Runs a ttest analysis with Dutch and Finnish as source languages.
Default parameters, but show sentence level scores*

**Requirements**  
*Please install these packages prior to running the script*  
NumPy  
SciPy

**Notes**
1. chrFplusplus.py is a modified version of the chrF++ score
   implementation @ https://github.com/m-popovic/chrF. It is imported as
   a module in the main `ttest.py` script

2. The preprocessing script `preprocessing.py` is presented for
   reference. The script reads the full-length Europarl data files
   downloaded from the internet. And takes 100 sentences and puts them
   in smaller data files that have 'short' in them.

3. I encountered a lot of difficulties with the PYPI googletrans API. It
   is not the official Google Translate API, and therefore does not work
   properly at all times. The most common error with the API is that it
   often wouldn't translate the sentences despite me having specified
   the correct source language. Because of this, I was not able to
   achieve even close to what I had planned for in terms of the
   objectives presented in the hypothesis presentation. I tried
   tinkering with the official Google Cloud translate API, but could not
   get it to work due to authentication problems. All in all, the amount
   of data processing took a hit once I wasn't able to attain the amount
   of data appropriate for statistical analysis.
