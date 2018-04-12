# Assessment

You will have 120 minutes to complete the assignment at which time you will be asked to submit a pull request.

* Time: 120 minutes
* Open book
* Individual

## Python version  
Take this assessment in **Python 3**.  To check which version of Python is installed natively, type `python --version` in the terminal.  If it's Python 2, activate the Python 3 environment you made earlier in the course:  
```
$ source activate py3
```

## Assignment

There are two parts to this assessment:

1. `src/assessment.py` contains function stubs for you to fill in. The goal is to make the tests pass. There are 10 problems.

   **Running Unit Tests**

 * You can run the tests with this command from the root directory (assessment-3/):    

   `make test`

 * If you do not have py.test, you may see Import errors. Run the following commands in case you see such errors:    

    * `pip install pytest`     

 * It can be helpful to press enter a bunch of times between each time you run the test so that it's easy to find the beginning of your most recent results.    

 * If you'd like to try your functions yourself, you can do this in ipython:

   ```python
   from src import assessment as a
   print(a.roll_the_dice())
   ```

   After you modify `assessment.py` you can update it in ipython with the `importlib` module:
   ```python
   import importlib
   importlib.reload(a)
   ```

 * During the assessment you may import any modules you find helpful.
 * If you'd like to try running your sql query directly, run this in the terminal:
   ```
   sqlite3 data/sqlite.db
   ```

2. `src/math_assessment.txt` contains math questions. Write in your answers in the file. There are 9 problems.


**Feel free to use any online resources like python documentation and tutorials, your notes, readings and exercises.**

Good luck!
