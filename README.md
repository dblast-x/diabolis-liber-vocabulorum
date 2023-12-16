# *Diabolis Liber Vocabulorum*

### Steps:

**--Test--**
1. [ x ] Make parser to improve the original text with flaws and pass it to an edited file.
    - [ x ] Write it to a file

**--Prod.--**
1. [ x ] Develop the search algorithm
    - [ x ] Parse the book and create the dictionary to use as the 'Liber Vocabulorum'
    e.g :                                               <br>
        {                                               <br>
            "A": {"Aword": "Lorem Ipsum"},              <br>
            "B": {"Bword": "Lorem Ipsum"},              <br>
            "C": {"Cword": "Lorem Ipsum"},              <br>
            "N": {"Nword": "Lorem Ipsum"},              <br>
        }                                               <br>
        + The book may relay on a Database:
        e.g:                                <br>
            | Letter -> one to many --> Word|s -> unique --> Meaning <br>

2. [  ] Create the actual program to query the data to the user.
3. [  ] Pass it to Django.


# Database:

### SQL :: Benefits >>
    - Relationship
    - Experience working with a particular DBMS || SQLite3
    - ...
 
### JSON :: Benefits >>
    - It's already a dictionary :v
    - Portabble
    - Editable
