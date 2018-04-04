# Assessment #1

Welcome to your first assessment.  This assessment does not count towards your course performance, it is only used by your instructors to gauge your strengths and weaknesses so they can provide you a better learning experience throughout the immersive program.

This assessment has **two parts**: a coding part (`assessment.py`) and a math/concept part (`math_assessment.txt`). You will have 120 minutes to complete the entire assessment, after which you will submit a pull request so that your work can be assessed.

* Time: 120 minutes
* Open book
* Individual

### Python version
Take this assessment in **Python 3**.  To check which version of Python is installed natively, type `python --version` in the terminal.  If it's Python 2, activate the Python 3 environment you made in the Precourse or Week 0:  
```
$ source activate py3
```
If you're running Anaconda's distribution of Python 2 natively and haven't made this environment before, it's easy to do though the download takes a few minutes.  In terminal type:
```
$ conda create -n py3 python=3 anaconda
```        
Only create the Python 3 environment if you **don't** have Python 3 installed.  Please ask for help if any of this is confusing or you're not sure.


## Instructions for Git/Github

The first step in taking this assessment (and all those to follow later) is to **fork this repository to your own github account**.  Your fork will retain private status, and be visible only to you through your account.

After forking this repository to your own account, **clone your copy** to your laptop using the git client in your terminal.  For example, when cloning a forked copy of this assessment, user `madrury` used the command:

```
$ git clone https://github.com/madrury/dsi-assessment-day1.git
```

This will copy the repository on your computer so that you can edit the files.  When you are finished with the assessment, **add** the `assessment.py` and `math_assessment.txt` to your git staging area, **commit** them, and then **push** them up to your Github account.  Finally, when you can see your modified files on your Github page, issue a **pull request** on Github to merge them into the gSchool repo (so they can be graded).  The git commands will look like this:  
```
$ git add src/assessment.py math/math_assessment.txt
$ git commit -m "<Your Name> Assessment 1 solutions"
$ git push origin master
```
Please ask for help from an instructor if you need help forking on Github, cloning and pushing with git from terminal, or issuing a pull request on Github.  


### SQL
The last part of the coding section asks for SQL queries on the markets SQL database.  The SQL queries that you will submit for grading should be returned as strings in the relevant functions in `assessment.py`.  However you may wish (it is not required) to test your queries in sqlite3 or postgreSQL first.

The databases (`markets.sqlite` for sqlite3, and `markets.sql` for postgreSQL) are located in the `data` directory. 

#### If you want to use sqlite3 (easiest)
Navigate to the `dsi-assessment-day1/data` directory in terminal.  
At the terminal, type:
```
$ sqlite3 markets.sqlite
```
Now you can try your queries.

#### If you want to use postgreSQL
Navigate to the `dsi-assessment-day1/data` directory in terminal.
The directions depend on your operating system (MacOs or Linux). 

##### Mac directions
On your Dock, go to Applications, find the Postgres.app icon and click it.
Then in the window that opens up click on "Open psql."  The psql terminal should open.  Then in that terminal create an empty markets database:  
```
# CREATE DATABASE markets;
# \q
```
Now load the provided file (`markets.sql`) into psql by typing in terminal:
```
$ psql markets < markets.sql
```
Now you should be able to open the database you just made:
```
$ psql markets
```
Now you can try your queries.

##### Linux directions
Create an empty markets database by typing these commands in terminal: 
```
$ sudo -i -u postgres
$ createdb markets
$ exit
```
Now load the provided file (`markets.sql`) into psql by typing in terminal:
```
$ psql markets < markets.sql
```
Now you should be able to open the database you just made:
```
$ psql markets
```
Now you can try your queries.  

Once again, testing these queries in sqlite3 or postgreSQL is *optional*.  These SQL instructions are provided for your convenience.

## The Assessment

The repository has the following folder structure:

    assessment-day1
    ├── Makefile
    ├── README.md
    ├── src
    │   ├── __init__.py
    │   ├── assessment.py
    ├── data
    │   ├── alice.txt
    │   ├── markets.sqlite
    │   ├── markets.sql
    ├── test
    │   ├── __init__.py
    │   └── unittests.py
    └── math
        ├── math_assessment.pdf
        └── math_assessment.txt

There are 21 questions over these topics in this order: 

In `src/assessment.py`  
* general Python (4 questions)
* probability (1 question)
* numpy (2 questions)
* pandas (2 questions)
* SQL (3 questions)  

In `math/math_assessment.txt`  
* Math (9 questions)

**There are two parts to this assessment!  Please complete both!**

1. `src/assessment.py` contains function stubs for you to fill in. The goal is to make the tests pass. There are 12 problems in the file.

 * **Running Unit Tests**

 * This section (`src/assessment.py`) can be tested using the unit tests. You can run the tests with this command from the root directory (dsi-assessment-day1/):    

    `py.test`

 * If you do not have py.test, you may see Import errors. Run the following commands in case you see such errors:    

    `pip install pytest`     

 * `.` refers to passing test, `E` is an error in the code and `F` is a failure. So something that looks like this: `....EFFFFFF` means 4 tests passed, one has an error and 6-11 fail.
 * It can be helpful to press enter a bunch of times between each time you run the test so that it's easy to find the beginning of your most recent results.    


2. The questions for the math portion of the assessment are in
  `math/math_assessment.pdf`. Put your answers in `math_assessment.txt`.
  There are no automated tests for this portion of the assessment.

* At the end of 120 minutes, submit a pull request.

**Feel free to use any online resources like python documentation and tutorials, your notes, readings and exercises.**

Good luck!
