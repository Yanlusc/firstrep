for i in range(1, 5):
    # The following line are equivalent to each other
    # oe = 'odd' if i % 2 else 'even'
    # oe = 'even' if (i % 2 == 0) else 'odd'
    oe = ''
    # The following `if` statements are equivalent to each other
    # if not (i%2):
    if (i % 2) == 0:
        oe = 'even'
    else:
        oe = 'odd'
    print(f'{i} is {oe}')

    # reminder
    # `if i%2` is trying to do `if TRUE`
    # and `TRUE=1`
    # and `i%2=1`(TRUE)  [is 1 true?]
    # and `i%2=0`(FALSE) [is 0 true?]
    # and `i%2=5`(FALSE) [is 5 true?]
