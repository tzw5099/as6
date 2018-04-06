# Python Assignment

The goal of this assignment is to familiarize yourself with some advanced python features so that you can write cleaner, more efficient code.

## Part 0: Fork and clone the repo

You should make your own copy of the repository so that you can edit it.

1. Create a fork of this repo by clicking on the **Fork** link in the upper right.
2. Checkout your personal copy of the repo: `git clone https://github.com/<username>/dsi-python-intro`
3. Navigate to the repo directory: `cd dsi-python-intro`
4. One pair member should create a branch for today's work: `git checkout -b pair`, then `git push -u origin pair`
5. Add your partner's repo as a remote as described [here](https://github.com/gSchool/dsi-welcome/blob/master/notes/using_git.md)

### How to submit?
1. `git add filename` for all the files you want to add.
2. `git commit -m "Message describing what you did"`
3. `git push <remote-name> pair`
  - `<remote-name>` will either be `origin` or `<partner-name>`
4. Now if you go to your personal copy on github, your changes should be there: `https://github.com/<username>/dsi-python-intro`

Ideally, you should regularly run steps 1-3. This will save your work as you go. And if you ever goof things up, you will have all the history, you can revert any file to how it was at any previous commit!

## Part 1: Fill in some functions

In this part, you will fill in the functions in `functions.py` according to their docstrings. We've written some test code for you in `test_functions.py`.

The tests are written with the `nose` module and you can run the tests in the command line:

```shell
nosetests
```

Don't forget to run the pep8 style checker.

```shell
pycodestyle functions.py
```


## Part 2: Efficiency

The file `efficiency.py` contains some poorly written code. It's your job to fix it up. It all works correctly, but it could be made more efficient.

For each function, you should try running it and timing it to see how well it does. We've created the data for you to use. The `word_dict` is saved as a pickle object, which is a way of saving a python object so you can reload it easily.

There are two data files, `alice.txt` and `articles.txt`. We recommend running with `alice.txt` first as it's smaller and most of the inefficient code will take an unreasonably long time on the larger file (though you can verify this for yourself and just do Ctrl-C when you're ready to give up). After you make the code more efficient, try it with the larger file.

We're also going to be using `timeit` to get a measure of how long the function takes.

Here's how you can run it in ipython:

```python
In [1]: import pickle

In [2]: import efficiency

In [3]: word_dict = pickle.load(open("data/word_dict.pkl", 'rb'))

In [4]: timeit efficiency.find_new_words(open("data/alice.txt"), word_dict)
1 loops, best of 3: 21 s per loop
```

Whenever you change the code in `efficiency.py` make sure to run this command in ipython:

```python
In [5]: import importlib

In [6]: importlib.reload(efficiency)
```

For `list_of_words` and `find_new_words` you should be able to get a *big* improvement with a minor change. For `get_average_score` and `find_high_valued_words`, the speedup will be less impressive.

**For each function, do the following:**

1. Run `timeit` to get a measure of how well the original version does. Make note of this value.
2. Make your change to the file.
3. Run `timeit` again and make note of the improved runtime.
4. Write a comment next to each function with the runtime speedup and an explanation of why your version is faster.

**These are all very small changes and may be tricky to spot. If you can't find the issue in 5-10 minutes, ask a neighbor or instructor for a hint.**


## Part 3: A Python Script

You are given two files which contain reviews from two different sources. The files are in the `data` folder: `reviews1.txt` and `reviews2.txt`.

Take a look at the data. In the command line, this is especially useful if you have large files:

```shell
head data/reviews1.txt
```

Or even just look at the first line:

```shell
head -n 1 data/reviews 1.txt
```

The line `il-Yamo   5` means that restaurant `Yamo` was given a rating of `5` by user `il`. Don't read too much into the review values, this was randomly generated "data". All of the places are local favorites :)

You would like to know for each restaurant their average rating from each source. You will create a file with lines like this: `yamo,3.25,2.2`. The lines should be in *sorted order*. Make sure that you match the names even if their capitalization isn't the same. If a restaurant is in one file, but not the other, you should still include it and give a reasonable value for the missing number. You can see an example output in `example_out.csv`.

You should write a python script which can be run on the command line like this:

```shell
python script.py data/reviews1.txt data/reviews2.txt out.csv
```

Notes:

1. Use functions to make your code clean and easy to read. Nothing besides import statements and the main block (`if __name__ == '__main__':`) should be outside of functions.
2. Use the `argparse` module for getting input (it's a little cleaner than just using `sys.argv`). Look at the [documentation](https://docs.python.org/dev/library/argparse.html) to figure out how to use it.
3. Use a `defaultdict` for storing all the restaurant reviews.
4. For extra credit, use the `re` module for parsing the line ([documentation](https://docs.python.org/2/library/re.html)).
5. You can compare your result to ours with: `diff out.csv example_out.csv`
