# AutoPrognosis: Automated Clinical Prognostic Modeling via Bayesian Optimization

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

AutoPrognosis is a system for automating the design of ensembles of predictive modeling pipelines tailored for applications related to clinical prognosis. Each pipeline comprises various algorithms such as
  - Imputation and data processing algorithms.
  - Feature processing algorithms.
  - Classification algorithms.

The system operates using a Bayesian optimization algorithm that relies on structured kernel learning to solve the high-dimensional pipeline optimization problem. Technical details can be found in our [ICML paper](https://icml.cc/Conferences/2018/Schedule?showEvent=2050).
