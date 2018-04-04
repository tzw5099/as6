# In count_characters(string) some attractive alternative solutions are:

    d = dict()
    for char in string:
        d[char] = d.get(char, 0) + 1

    from collections import Counter
    d = Counter(string)


# In word_count(filename) the "with open(filename) as f"

    automatically closes the file when the "with block" completes, exceptions included.
    If a file is opened and not explicitly closed in a function it will still be closed if
    the function completes successfully since the file variable will be deleted once it goes
    out of scope and the file will be closed\; however, exceptions thrown in the function could
    cause the file variable to persist in the stack trace, causing the file to remain open...

# In cookie_jar(a, b) we use the following probability theory rational
    
     Pr(randomly choose Jar A) = Pr(randomly choose Jar B) = 0.5
     Pr(randomly draw cholocate cookie | Jar A) = a
     Pr(randomly draw cholocate cookie | Jar B) = b
     Pr(randomly draw cholocate cookie AND Jar A) = a * Pr(randomly choose Jar A)
     Pr(randomly draw cholocate cookie AND Jar B) = b * Pr(randomly choose Jar B)
     Pr(randomly draw cholocate cookie) = sum_X Pr(randomly draw cholocate cookie AND Jar X)
                             = a * Pr(randomly choose Jar A) + b * Pr(randomly choose Jar B) 
     Pr(Jar A | randomly draw cholocate cookie) = 
             Pr(randomly draw cholocate cookie AND Jar A)/Pr(randomly draw cholocate cookie)
     a*Pr(randomly choose Jar A) / ( a*Pr(randomly choose Jar A) + b*Pr(randomly choose Jar A) )


# In data_frame_work(df, colA, colB, colC)

     We do not need to return anything becaue df is passed by reference
     and changes to df will be persistant in df after the function completes

