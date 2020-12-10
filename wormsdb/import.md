# Importing WORMS to SQLLITE 

## Import tools tested 

-- Libreoffice 
-- sqllitebrowser (worked for the smaller tables, not for taxon) 
-- csvkit, with the command **csvsql --tabs --quoting=3 --db sqlite:///worms2.db --no-constraints --insert taxon.txt ** 

The latter imported the entire table, resulting in the expected number of records

