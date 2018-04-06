# Individual exercise

In this exercise, you will learn how to use Unix commands to perform exploratory data analysis (EDA) from the command line.  This is an invaluable skill which will help you find problems in data sets and clean data more quickly.  Often, with a little cleverness, you can answer questions about your data without needing to resort to `Python`, `R`, and other heavier tools.

Unix is particularly adroit at handling text files because there are many commands which can operate on this format.  By extension, CSV files are also easy to manipulate.


## Getting help

What does the `man` command do?  Use `man` to learn how to use `man`.  Often, man-pages are still a useful source of information.


##  Customizing `bash`

You can custom the `bash` shell by creating aliases and shell scripts.  You will also need to modify environment variables so that commands are in your path.


### Aliases

In which dotfile, should you put BASH customizations such as aliases?  `~/.profile`, `~/.bash_profile`, or `~/.bashrc`?

I find the following aliases helpful:

```bashrc
alias h='history'
alias l='ls -GFh'
alias ll='ls -lFGh'
alias md5sum='md5'
```

Add this to your `~/.bashrc`.  You may need to modify `~/.bash_profile` to source `~/.bashrc`.  Whenever you change a dotfile, you will need to source it for the changes to take effect:

```bash
$ source ~/.bash_profile
```

What do these aliases do?

You can add other aliases for commands which you often perform, which will boost your productivity.


### Shell scripts

Often, I like to look at the beginning and end of a file.  A one-liner to do this is:

```bash
$ (head -n 5 ; echo "==========" ; tail -n 5) < some_file_of_interest
```

The expression between the parentheses will run in a sub-shell.  We use I/O redirection so the shell will read from `some_file_of_interest`.  Create an alias to do this.  Hint: leave off the `< some_file_of_interest` part.  Then you can run you alias as `inspect < some_file_of_interest`.  In this case, using an alias is not as clean as using a shell script because you have to specify I/O redirection and you have hard coded the number of lines to display.  Write a script `inspect.sh`.  Make sure you can pass the name of the file as an argument.  Optionally, support an extra argument to specify how many lines to display.  Don't forget to change the permissions so that your script is executable.


### Environment variables

It is good practice to store utility scripts in `~/bin`.  Create this directory and add it to your `PATH` so that you can use your scripts anywhere. Don't forget to source `~/.bash_profile` afterward.

For Python libraries, you will need to modify `PYTHONPATH`.  Other applications will also have environment variables which you need to configure, which should be explained in the relevant documentation.


##  Wikipedia data

Let's analyze some Wikipedia data using Unix tools.  But first some advice:  you will be working with a large file, so commands will take a while to run.  Consequently, test your scripts and commands on a small subset of the file so that you can get them working quickly.  When you working in an environment, like `bash` or regular expressions, where debugging tools are scarce, you should build up your code in small steps, testing each step along the way.  Document anything clever to make future maintenance easier.


### Getting started

Start by downloading the data using the command line:

```bash
$ wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles1.xml-p10p30302.bz2
```

*   What does the `wget` command do?  Could you also use `curl`?

*   What type of file is `enwiki-latest-pages-articles1.xml-p000000010p000030302.bz2`?  How can you figure out the a file's type? Often files come in different (compressed) archive formats. `tar` and `gzip` are common.  Unpack the file.

*   How big is it?  How many lines does it have?  What type of file is the uncompressed version of the file?

*   Would it be a good idea to load this file into an editor?


### Examining the file

Loading large files into an editor is a bad idea because it is time consuming and can crash your editor if you run out of memory.  Fortunately, Unix provides tools which work on arbitrarily large text files, including CSV.

*   What do the beginning and end of the file look like?  What commands did you use?

*   Examine the first couple pages of the file.  What do you notice about the structure?

*   Advanced:   if you want to look at just lines 636100 to 636120 how would you do it?  (Hint: use `sed`.)


### Exploratory analysis

Let's answer some basic questions about contributors.

*   The tag `<contributor>` ... `</contributor>` identifies a contributor.  How many are there?

*   How many users are identified by the tag `<username>`?

*   Who are the most common contributors by username? Hint: you will need to connect several commands via pipes.  `sed` or `perl` with the right regular expression will allow you to extract the name from between the `<username>` ... `</username>` tags.  `sed` uses an older version of REs so you will need to escape the parentheses on the capture group.

*   How many of the contributors are bots?

*   Advanced:   What are the other contributors -- i.e., those entries which have a `<contributor>` tag but not a nested `<username>` tag?  Hint: use `sed` or `perl`.  How many of these contributors are there?  Do they explain all of the missing contributors?
