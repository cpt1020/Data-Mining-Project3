# Data Mining Project 3

This is a homework of Data Mining course (Fall 2022) at NCKU.

## Algorithms Implemented

- HITS
- PageRank
- SimRank

The following parameters can be set in `main.py`:

- Damping factor for PageRank
- Decay factor for SimRank
- Max iteration for the 3 algorithms
- Threshold to convergence for the 3 algorithms

### HITS

Formula implemented in this project:

$$
Authority(v)=\sum_{w\,\in\, parent(v)} Hub(w)\newline
\newline
Hub(v)=\sum_{w\,\in\, children(v)} Authority(w)
$$

### PageRank

Formula implemented in this project:

$$
PageRank(V_i) = \frac{d}{n} + (1-d) \times \sum_{l_{j,i}\in E} \frac {PageRank(P_j)}{Outdegree(P_j)}
$$

$$
\displaylines{
d:\ damping \ factor\\
n:\ number\  of\ vertex}
$$

### SimRank

Formula implemented in this project:

$$
S(a,b)= \frac{C}{\mid{I(a)}\mid\mid{I(b)}\mid}\sum_{i=1}^{\mid{I(a)}\mid} \sum_{j=1}^{\mid{I(b)}\mid} S(I_i(a), I_j(b))
$$

$$ 
\begin{aligned} S(a,b): similarity\ of\ node\ a\ and\ node\ b \\
C: decay\ factor \\
{I(a)}: parent\ of\ node\ a \end{aligned}
$$

## Getting Started

To run this program, please first `cd` to the directory of `main.py`, then use the following command:

```bash
python3 main.py
```

## Input File

Test data in the input folder were given from this course, includes `graph_1.txt`, `graph_2.txt`, `graph_3.txt`, `graph_4.txt`, `graph_5.txt`, `graph_6.txt`, and `ibm-5000.txt`.

Data generated from `IBM Quest Synthetic Data Generator` can also be used as input file. Just make sure the key word `ibm` is contained in the file name, for example `ibm-data.txt`.

## Results

Results of the 3 algorithms will be stored in the folder as the same name of the `graph_name` in the result folder.