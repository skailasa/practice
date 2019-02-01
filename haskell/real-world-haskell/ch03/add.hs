-- Haskell allows functions to be written
-- as a series of equations ... 
sumList (x:xs) = x + sumList xs
sumList []     = 0
