type BookID = Int
type BookTitle = String
type BookAuthors = [String]

data BookInfo = Book BookID BookTitle BookAuthors
                deriving (Show)

data MagazineInfo = Magazine Int String [String]
                    deriving (Show)

-- Type and Value constructors can/normally do, have the same
-- name in Haskell
-- Can alias common types to make more descriptive.
type CustomerID = Int
type ReviewBody = String

data BookReview = BookReview BookInfo CustomerID ReviewBody
                  deriving (Show)

-- Can also use synonyms for more verbose types
type BookRecord = (BookInfo, BookReview)

-- Can pattern match on algebraic datatypes
bookID (Book id _ _) = id
bookTitle (Book _ title _) = title
bookAuthors (Book _ _ authors) = authors

myInfo = Book 12345 "Algebra of Programming"
         ["Richard Bird", "Oege de Moor"]

myReview = BookReview myInfo 1 "It was OK"
