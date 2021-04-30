# niteru

[![PyPI version](https://badge.fury.io/py/niteru.svg)](https://badge.fury.io/py/niteru)
[![Python CI](https://github.com/ninoseki/niteru/actions/workflows/test.yml/badge.svg)](https://github.com/ninoseki/niteru/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/ninoseki/niteru/badge.svg?branch=main)](https://coveralls.io/github/ninoseki/niteru?branch=main)

This package provides a set of functions to measure the similarity between HTMLs.

**Note**: This is a fork of [html-similarity](https://github.com/matiskay/html-similarity).

## Key differences

- Type hints
  - All functions have proper type hints
- Dependency free
  - Works along with plain Python

## Installation

```bash
pip install niteru
```

## How it works

### Structural Similarity

Uses sequence comparison of the html tags to compute the similarity.

We do not implement the similarity based on tree edit distance because it is slower than sequence comparison.

### Style Similarity

Extracts CSS classes of each html document and calculates the jaccard similarity of the sets of classes.

### Joint Similarity (Structural Similarity and Style Similarity)

The joint similarity metric is calculated as::

```python
k * structural_similarity(html1, html2) + (1 - k) * style_similarity(html1, html2)
```

All the similarity metrics take values between 0.0 and 1.0.

### Recommendations for joint similarity

Using `k=0.3` gives better results. The style similarity gives more information about the similarity rather than the structural similarity.

## Examples

Here is an example:

```python
html1 = '''
<h1 class="title">First Document</h1>
<ul class="menu">
  <li class="active">Documents</li>
  <li>Extra</li>
</ul>
 '''

html2 = '''
<h1 class="title">Second document Document</h1>
<ul class="menu">
  <li class="active">Extra Documents</li>
</ul>
'''

from niteru import style_similarity, structural_similarity, similarity

style_similarity(html1, html2) # => 1.0
structural_similarity(html1, html2) # => 0.8571428571428571
similarity(html1, html2) # => 0.9285714285714286
```
