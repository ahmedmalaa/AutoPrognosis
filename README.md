# AutoPrognosis: Automated Clinical Prognostic Modeling via Bayesian Optimization with Structured Kernel Learning 

Note that this code is not for public release.

[AutoPrognosis](https://icml.cc/Conferences/2018/Schedule?showEvent=2050): a system for
automating the design of predictive modeling pipelines tailored for
clinical prognosis. AUTOPROGNOSIS optimizes ensembles of pipeline
configurations efficiently using a novel batched Bayesian optimization
(BO) algorithm that learns a low-dimensional decomposition of the
pipelines high-dimensional hyperparameter space in concurrence with
the BO procedure.

See <project_dir>/doc/install.md for installation instructions

## Usage

```
python3 autoprognosis.py -i <data.csv> --target <response variable> -o <outdir>  [ -n <num_sample> --it <num_iterations> ]
```

The results are in two json files: <outdir>/result.json and <outdir>report.json. They can be shown with:

```
python3 autoprognosis_report.py -i <outdir>
```

See also jupyter notebooks tutorial_autoprognosis.ipynb

## References
[1]: [AutoPrognosis: Automated Clinical Prognostic Modeling via Bayesian Optimization with Structured Kernel Learning](https://arxiv.org/abs/1802.07207)
