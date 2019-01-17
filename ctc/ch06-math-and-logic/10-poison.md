# Poison

1000 bottles of soda, 10 test strips - can be used infinitely as long as
they haven't tested positive, any amount of drops can be placed. Can only
test a given strip once a day, takes 7 days for results. Find poisoned
bottles in the least amount of time.

Attempt divide equally into groups of n where n is the number of test strips.
test n bottles (1 from each group) per day and send for results. When they've
arrived test next n (updating n if is positive obviously).