# AutoPrognosis: Automated Clinical Prognostic Modeling via Bayesian Optimization

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

AutoPrognosis is a system for automating the design of ensembles of predictive modeling pipelines tailored for applications related to clinical prognosis. Each pipeline comprises various algorithms such as
  - Imputation and data processing algorithms.
  - Feature processing algorithms.
  - Classification algorithms.

The system operates using a Bayesian optimization algorithm that relies on structured kernel learning to solve the high-dimensional pipeline optimization problem. Technical details can be found in our [ICML paper](https://icml.cc/Conferences/2018/Schedule?showEvent=2050). An explanation of our algorithm can also be found in this [video presentation](https://www.youtube.com/watch?v=d1uEATa0qIo).

### Installation

Please refer to < /doc/install.md > for installation instructions.

### Usage

You can use AutoPrognosis through its command line interface as follows

```sh
$ python3 autoprognosis.py -i <data.csv> --target <response variable> -o <outdir>  [ -n <num_sample> --it <num_iterations> ]
```
Once the above command is executed, the results can be found in two json files: <outdir>/result.json and <outdir>report.json. They can be shown with:

```sh
$ python3 autoprognosis_report.py -i <outdir>
```
A tutorial on how to use AutoPrognosis API can also be found in this [Jupyter notebook](https://github.com/ahmedmalaa/AutoPrognosis/blob/master/alg/autoprognosis/tutorial_autoprognosis_api.ipynb).

### Known issues
Acquisition function LCB generates excesive warnings
```sh
$ The set cost function is ignored! LCB acquisition does not make sense with cost.
```
This issue results from interfacing with GPyOpt's acquisition functions. The issue can be ignored.

### Citation

If you use our code in your research, please cite:
```sh
@inproceedings{alaa2018autoprognosis,
  title={AutoPrognosis: Automated Clinical Prognostic Modeling via Bayesian Optimization with Structured Kernel Learning},
  author={Alaa, Ahmed and Schaar, Mihaela},
  booktitle={International Conference on Machine Learning},
  pages={139--148},
  year={2018}
}
```

### References

[1] A. M. Alaa and M. van der Schaar, [AutoPrognosis: Automated Clinical Prognostic Modeling via Bayesian Optimization with Structured Kernel Learning](http://proceedings.mlr.press/v80/alaa18b.html), ICML 2018.

[2] A. M. Alaa and M. van der Schaar, [Prognostication and Risk Factors for Cystic Fibrosis via Automated Machine Learning](https://www.nature.com/articles/s41598-018-29523-2), Nature Scientific Reports, 2018.

[3] A. M. Alaa and M. van der Schaar, [Cardiovascular Disease Risk Prediction using Automated Machine Learning: A Prospective Study of 423,604 UK Biobank Participants](https://www.ncbi.nlm.nih.gov/pubmed/31091238), PLOS ONE, 2019.




