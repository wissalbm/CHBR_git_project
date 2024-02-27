=================================================================
|                Hello! PH_CBR Program                          |
=================================================================
The Excel file "sourceFiles/primitives.xlsx" has been converted to CSV as "sourceFiles/primitives.csv".
The Excel file "sourceFiles/Failures.xlsx" has been converted to CSV as "sourceFiles/failures.csv".
The files in the folder 'HypotheticalDatabase/files' have been deleted.
The files in the folder 'ClassicalDataBase/result' have been deleted.
The folder 'HypotheticalDatabase/files' is empty.
The files in the folder 'HypotheticalDatabase/result' have been deleted.
Step1: preatraitement phase
    - generate 2 files containt 100 vectors   
           1- containt with the value of the 30 primitives  (aleatoir generation
            Constraints: 23 float and 7 boolen & 70% normal (21 values) - 30% abnormal (9 value)
            2- containt the statut of the 30 primitives (0 abnormal | 1 normal) 
files named: vecteurcsv.csv & vectorstatutcsv generated with success
Head Added : FN1,FN2,FN3,FN4,FN5,FN6,FN7,FN8,FN9,FN10,FN11,FN12,FN13,FN14,FN15,FN16,FN17,FN18,FN19,FN20,FN21,FN22,FN23,FB1,FB2,FB3,FB4,FB5,FB6,FB7
CSV file converted to Excel successfully!
CSV file converted to Excel successfully!
Step2: Create classical DB
CSV file converted to Excel successfully!
Step3: Create Hypothetical DB
file nbre_appartenance generated with success
sorted file nbre_appartenance  generated with success
assign_weights file generated with success: from failures.csv, calculate the number of appearance of failures 
100 vecteurs ont été ajoutés au fichier HypotheticalDatabase/files/vector_HBR.csv.
100 vectors generated, they startes by FN14,FN18,FB5
Les primitives ont été réorganisées dans chaque ligne et sauvegardées dans HypotheticalDatabase/files/vector_HBR_tri_membership.csv.
scheduling according to the number of appearances successfully completed
Le mapping des pannes avec les vecteurs a été effectué avec succès.
assignment of fault names to vectors successfully completed
Le fichier HDB a été créé avec succès : HypotheticalDatabase/files/HDB_File_primitivevalues.csv
HypotheticalDatabase_File_primitivevalues generated with success
La dernière colonne a été copiée avec succès et enregistrée dans HypotheticalDatabase/result/HDB_File_labled.csv
HypotheticalDatabase created with label !finish
well done ! good work
