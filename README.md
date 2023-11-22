# *Diabolis Liber Vocabulorum*

### Steps:

**--Test--**
1. [ x ] Make parser to improve the original text with flaws and pass it to an edited file.
    - [ x ] Write it to a file

**--Prod.--**
1. [ x ] Develop the search algorithm
    - [  ] Parse the book and create the dictionary to use as the 'Liber Vocabulorum'
    e.g :
        {
            "A": {"Aword": "Lorem Ipsum"},
            "B": {"Bword": "Lorem Ipsum"},
            "C": {"Cword": "Lorem Ipsum"},
            "N": {"Nword": "Lorem Ipsum"},
        }
        + The book may relay on a Database:
        e.g:
            | Letter -> one to many --> Word|s -> unique --> Meaning


# Database:

### SQL :: Benefits >>
    - Relationship
    - Experience working with a particular DRMS || MariaDB
    - ...
 
### JSON :: Benefits >>
    - It's already a dictionary :v
    - Portabble
    - Editable

