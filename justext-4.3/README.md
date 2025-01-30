# jusText 4

jusText is a tool for removing boilerplate content, such as navigation links, headers, and footers from HTML pages. It is designed to preserve mainly text containing full sentences and it is therefore well suited for creating linguistic resources such as Web corpora.

```
#!html
<a class="lnk" href="http://is.muni.cz/th/45523/fi_d/phdthesis.pdf">Paper</a>
|
<a class="lnk" href="/wiki/Justext/Cite">Cite</a>
|
<a class="lnk" href="http://opensource.org/licenses/BSD-3-Clause">Licence</a>
```

## How it works
See what is kept and what is discarded from a typical web page: [Example image](https://corpus.tools/attachment/wiki/Justext/nlp_jusText_fi.jpg).

Read a description of the [jusText algorithm](https://corpus.tools/wiki/Justext/Algorithm).

## Installation
1. Make sure you have Python 3.11 or newer. Required packages are installed via pip automatically (or system-wide, e.g. python3-lxml and python3-html5-parser in Fedora).
2. Download, extract, install:
```
wget https://corpus.tools/raw-attachment/wiki/Downloads/justext-4.3.tar.gz
tar xzvf justext-4.3.tar.gz
cd justext-4.3/
pip install --user . #omit --user to install for all users
```

### Legacy installation using deprecated distutils
Python 3.6 & Python 2.7 compatible
```
wget https://corpus.tools/raw-attachment/wiki/Downloads/justext-4.2.5.tar.gz
tar xzvf justext-4.2.5.tar.gz
cd justext-4.2.5/
python3 setup.py install --user #omit --user to install for all users
```

## Quick start
```
wget -O page.html http://planet.python.org/
justext -s English page.html > cleaned-page.txt
```
For usage information see:
```
justext --help
```

## Python API
```
import justext
import requests
page = requests.get('https://planetpython.org/').text.encode('utf-8')

paragraphs = justext.justext(page, justext.get_stoplist('English'))
for paragraph in paragraphs:
    if paragraph['class'] 'good':
        print(paragraph['text'])

```

## Online demo
[https://nlp.fi.muni.cz/projects/justext/](Justext online demo)

## Parameter values by use
|  **Description >>>** | **very strict** | **strict**                                            | **balanced**                           | **permissive**                 | **BoilerNet2017**                                                                                            |
|---------------------:|-----------------|-------------------------------------------------------|----------------------------------------|--------------------------------|--------------------------------------------------------------------------------------------------------------|
| **PARAMETER vvv**    | Justext default | recommended for large languages, web crawling default | recommended for low resource languages | recommended for rare languages | optimal for the dataset |
| length_low           |              70 |                                                    70 |                                     50 |                             40 |                                                                                                           57 |
| length_high          |             200 |                                                   140 |                                    140 |                             90 |                                                                                                           98 |
| stopwords_low        |             0.3 |                                                   0.2 |                                    0.2 |                            0.2 |                                                                                                         0.16 |
| stopwords_high       |            0.32 |                                                   0.3 |                                    0.3 |                            0.3 |                                                                                                         0.25 |
| max_link_density     |             0.2 |                                                   0.4 |                                    0.4 |                           0.45 |                                                                                                         0.42 |
| max_good_distance    |               5 |                                                     5 |                                      5 |                             10 |                                                                                                            5 |
| max_heading_distance |             150 |                                                   150 |                                    200 |                            300 |                                                                                                          243 |

**BoilerNet2017** is the configuration optimal for the set of web pages created by Leonhardt et al. called "GoogleTrends-2017" for [the paper](https://dl.acm.org/doi/abs/10.1145/3366424.3383547) on their neural boilerplate removal tool [BoilerNet](https://github.com/mrjleo/boilernet).

## Acknowledgements
This software has been developed at the [Natural Language Processing Centre](https://nlp.fi.muni.cz/en/nlpc) of [Masaryk University](https://www.muni.cz/) in Brno with financial support from [PRESEMT](http://presemt.eu/) and [Lexical Computing Ltd.](https://www.sketchengine.eu/). It also relates to [Jan Pomikálek's PhD thesis](https://is.muni.cz/th/45523/fi_d/phdthesis.pdf).


## Licence
Justext is licensed under the [BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)
