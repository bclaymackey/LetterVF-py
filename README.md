# LetterVF
The phonemic verbal fluency task is a common cognitive assessment of language and executive functioning which asks participants to list as many words as they can that begin with a given letter. Verbal fluency tasks are widely used to identify deficits in verbal fluency, which have been associated with disorders such as schizophrenia and dementia. Verbal fluency tasks are scored by the number of correct responses, however analysis of “clusters” of related words within a response list can give insights into the cognitive strategies used by participants. Unfortunately, manual word cluster analysis is time and labor intensive and inconsistent, since raters may cluster words differently depending on how they themselves have phonetically categorized the words. We present an automated pipeline for quantification of strategy use in the phonemic verbal fluency task, “LetterVF”.  LetterVF is a python module (i.e., a script containing useful functions, which can be imported and used in other scripts) that uses a pronunciation dictionary to convert verbal fluency task data items into lists of phonemes, which can be analyzed to identify clusters of words that share similarities in any of several clustering categories. Additionally, LetterVF contains useful functions for identifying intrusions (words which do not follow the rules for the task), identifying perseverations (responses repeated within the same trial), counting the number of cluster switches in a list, and calculating the average size of clusters for a list. Analysis of data from 50 participants’ verbal fluency task responses indicated that analysis using LetterVF yields accuracy and consistency on par with manual analysis. Our hope is that this tool will allow researchers to get more out of their datasets, and explore new topics related to cognitive strategy use, such as how strategies change with age and differences in strategies between experimental groups.

## More Information
More information regarding LetterVF and how to use it can be found here:
[preprint](10.31234/osf.io/wavqu)

## License
[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2021 Brandon Clay Mackey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
