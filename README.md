# Introduction to Python Programming
This repository contains a collection of Jupyter/IPython Notebooks introducing programming concepts in Python. The notebooks are intended to guide students in learning the basic functionality of programming in Python, and some of the most frequently used modules. 

First, make sure you have setup the programming environment correctly by reading the 'Getting Started' guide, after that you are ready to start coding, and working with the notebooks. Review the lecture notes and begin by working through the core notebooks (0-13), and then have a look at the bonus material.  

## Table of contents

### Lecture:
* [Course Lecture](python_course.pdf)

### Notebooks:
0. [Introduction to Jupyter Notebooks](00_introduction_to_jupyter_notebooks.ipynb)
1. [Hello World - first program](01_hello_world.ipynb)
2. [Datatypes, strings, numbers and variables](02_datatypes_strings_numbers_and_variables.ipynb)
3. [Lists, tuples, and sets](03_lists_tuples_and_sets.ipynb)
4. [If statements, and conditional logic](04_if_statements.ipynb)
5. [Loops, and user input](05_while_loops_and_user_input.ipynb)
6. [Dictionaries](06_dictionaries.ipynb)
7. [Functions introduction](07_introduction_to_functions.ipynb)
8. [More Functions](08_some_more_functions.ipynb)
9. [Classes and Object Oriented Programming](09_classes_and_OOP.ipynb)
10. [Handling Exceptions](10_exceptions.ipynb)
11. [Interfacing with external files](11_external_files.ipynb)
12. [Numpy library](12_numpy_library.ipynb)
13. [Matplotlib Library](13_matplotlib_library.ipynb)

### Bonus notebooks:
* [Bonus - Coding Style PEP8](bonus_coding_style_PEP8.ipynb)
* [Bonus - Databases and data persistence](bonus_databases_and_persistence.ipynb)
* [Bonus - Importing modules](bonus_importing_modules.ipynb)
* [Bonus - The Zen Of Python](bonus_the_zen_of_python.ipynb)



## Getting started
### 1. Install Python
If you have not yet installed Python the **Anaconda** distribution by [**Continuum Analytics**](http://www.continuum.io/) is highly recommended. Anaconda is a completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing. Anaconda includes an easy-to-use installer for almost every platform, drastically reducing the burden of setting up the environment. In addition it comes packaged with the most useful Python libraries.

Anaconda python can be downloaded from this webpage: [**Anaconda Python**](https://store.continuum.io/cshop/anaconda/)

### 2. Download the tutorial notebooks
If you are familiar with git version control and have git installed then you can download the relevant course notebooks by doing a git clone:

    git clone https://github.com/williamgrimes/python_in_a_notebook.git

Otherwise navigate to the following webpage: 

https://github.com/williamgrimes/python_in_a_notebook.git

And select `Clone or download`, then download the zip file and extract.

### 3. Running Jupyter Notebooks
Navigate to the directory of the unzipped or cloned course files, and open a _Terminal_, and type the following command:

    jupyter notebook

The notebook will launch in a browser from the present working directory.

### 4. Start learning
You are now setup to start working your way through the numbered notebooks in the Jupyter Notebook browser. Start with an introduction to Jupyter by selecting `00_introduction_to_jupyter_notebooks.ipynb` and work through in order.

If you are still curious after working through all the notebooks have a look at the extra notebooks for useful extra information.

## Basic Requirements
If you have installed the Anaconda 3.x distribution as described above you will have met the basic requirements necessary to begin working, otherwise having the following installed is a basic requirement for doing this course:

* Python 3.x (2.x would work as well)
* IPython 4.x (with **notebook support**) or Jupyter: 
    * `pip install ipython[notebook]` (OR)
    * `pip install jupyter`

N.B. these coursenotebooks are written in **Python 3**, if you are running Python 2, you might want to consider adding Python 3 to your system. If you are not sure which version of Python you are running then open a  _Terminal_, and type the following command:

    python -V

### Acknowledgements
This repository was edited from `python-in-a-notebook` by [Valerio Maggio](https://github.com/leriomaggio/python-in-a-notebook).

## License and Sharing Material
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
