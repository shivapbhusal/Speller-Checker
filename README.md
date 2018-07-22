# Speller-Checker for .tex files

This project deals with the spellchecking and auto correction. It uses the Unix dictionary from the location ``/usr/share/dict/words``.
Some plural words and forms of verbs are missing in the default unix dictionary. Additionally, this dictionary was also used:``http://www.mieliestronk.com/corncob_lowercase.txt``

In the future, this dictionary will also be used to incorporate common people names: ``http://gutenberg.org/ebooks/3201``

# Dependencies:
* Python version 2.7 or above. 

# Installation steps:
* Download project from ``` ```
* Navigate to the root of the project folder and type this on your terminal: ```python setup.py install```


# Acknowledgement
* The auto correction module is inspired from Peter Norvig's article on writing an auto-corrector: ```https://norvig.com/spell-correct.html```
