# Week 2 Assessment

Welcome to the second week of the Galvanize Data Science Immersive!

* Time: 60 minutes
* Open book
* Individual

## Python version
Take this assessment in **Python 3**.  To check which version of Python is installed natively, type `python --version` in the terminal.  If it's Python 2, activate the Python 3 environment you made earlier in the course:  
```
$ source activate py3
```

## Assignment

The goal of this assignment is to fill in each function stub in `assessment.py` according to its docstring and make the associated test pass. The repository structure is below for reference. `assessment.py` is under `src` directory.

There are 10 questions in `assessment.py` over these topics in this order:

* general Python (4 questions)
* pandas (3 questions)
* SQL (3 questions)

We recommend skimming over all the questions and solving the ones that you are most confident about first.

**Running Unit Tests**

 * You can run the tests with this command from the root directory (assessment-2/):    

    `make test`

 * If you do not have py.test, you may see Import errors. Run the following command in case you see such errors:    

    `pip install pytest`     

 * `.` refers to passing test, `E` is an error in the code and `F` is a failure. So something that looks like this: `....EFFFFFF` means 4 tests passed, one has an error and 6-11 fail.
 
 * It may be helpful to use `less` to page through your test results: `make test | less`. You can browse through your test results one page at a time using the space bar. Press `q` to exit `less`.

## Repository Structure

The repository has the following folder structure:

        assessment-2
        ├── Makefile
        ├── README.md
        ├── src
        │   ├── __init__.py
        │   ├── assessment.py
        ├── data
        │   ├── people.txt
        │   ├── housing.sql
        |   |-- buy.csv
        |   |-- rent.csv
        ├── test
            ├── __init__.py
            └── unittests.py


* At the end of 60 minutes, don't forget to `add`, `commit` and `push` followed by submitting a pull request.

**Feel free to use any online resources like python documentation and tutorials, your notes, readings and exercises.**

Good luck!
