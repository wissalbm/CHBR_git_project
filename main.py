# Import the logging configuration




import sys
import time

from ClassicalDataBase.script.classicalDB import label_vectors_classicalDB, create_cassicalDB_step1, \
    create_cassicalDB_step2
from GeneralScripts.convert_type_file import excel_to_csv, csv_to_excel
from GeneralScripts.empty_folder import empty_folder
from HypotheticalDatabase.scripts.createHypDB import count_nbre_appartenance, trie_appartenanceFile, assign_weights, \
    generate_vector, reorder_primitives_by_membership, map_vector_failure, create_HDB_file, label_HDB
from pretreatment.scripts.Creation_Vector_primitives import generate_vectors, add_header_to_vectorsFile

# Redirecting console output to the readme.txt file
sys.stdout = open('readme.txt', 'w')


# Input files
sourceFile_primitive = "sourceFiles/primitives.xlsx"
sourceFile_Failures = "sourceFiles/Failures.xlsx"

sourceFile_primitives_CSV = "sourceFiles/primitives.csv"
sourceFile_Failures_CSV = "sourceFiles/failures.csv"

#pretraitement
vecteurcsv = "pretreatment/files/vecteurs.csv"
vectorstatutcsv = "pretreatment/files/vectorstatutcsv.csv"
vecteurcsv_withEntete =  "pretreatment/files/vecteurcsv_withEntete.csv"
vectorstatutcsv_withEntete = "pretreatment/files/vectorstatutcsv_withEntete.csv"

vector_xsl_withEntete =  "pretreatment/files/vector_xsl_withEntete.xlsx"
vectorstatut_xsl_withEntete= "pretreatment/files/vectorstatut_xsl_withEntete.xlsx"

#classicalDB
classicalDB_statut =  "ClassicalDataBase/result/classicalDB_statut.csv"
classicalDB = "ClassicalDataBase/result/classicalDB.csv"
classicalDB_xsl = "ClassicalDataBase/result/classicalDB_xsl.xlsx"

#HypotheticalDatabase
membership_primitives = "HypotheticalDatabase/files/primitives_membership.csv"
primitives_membership_trie = "HypotheticalDatabase/files/primitives_membership_trie.csv"
weight_primitive = "HypotheticalDatabase/files/weight_primitive.csv"
vector_HBR = "HypotheticalDatabase/files/vector_HBR.csv"
vector_HBR_tri_membership = "HypotheticalDatabase/files/vector_HBR_tri_membership.csv"
HypotheticalDatabaseFile_primitiveNames = "HypotheticalDatabase/result/HDB_File_structure.csv"
HypotheticalDatabase_File_primitivevalues = "HypotheticalDatabase/files/HDB_File_primitivevalues.csv"
HypotheticalDatabaseFile_withlabel = "HypotheticalDatabase/result/HDB_File_labled.csv"






if __name__ == "__main__":
    start_time_Preprocessing = time.time()  #calcul execution Time

    print("=================================================================")
    print("|                Hello! PH_CBR Program                          |")
    print("=================================================================")

    excel_to_csv(sourceFile_primitive, sourceFile_primitives_CSV)
    excel_to_csv(sourceFile_Failures, sourceFile_Failures_CSV)
    #reset folders
    empty_folder("HypotheticalDatabase/files")
    empty_folder("ClassicalDataBase/result")
    empty_folder("HypotheticalDatabase/files")
    empty_folder("HypotheticalDatabase/result")

    #pretraitement
    print("Step1: preatraitement phase")
    print ("    - generate 2 files containt 100 vectors   ")
    print ("           1- containt with the value of the 30 primitives  (aleatoir generation")
    print("            Constraints: 23 float and 7 boolen & 70% normal (21 values) - 30% abnormal (9 value)")
    print("            2- containt the statut of the 30 primitives (0 abnormal | 1 normal) ")

    generate_vectors(sourceFile_primitives_CSV, vecteurcsv, vectorstatutcsv)
    print ("files named: vecteurcsv.csv & vectorstatutcsv generated with success")
    add_header_to_vectorsFile(vecteurcsv, vecteurcsv_withEntete)
    add_header_to_vectorsFile(vectorstatutcsv, vectorstatutcsv_withEntete)
    print("Head Added : FN1,FN2,FN3,FN4,FN5,FN6,FN7,FN8,FN9,FN10,FN11,FN12,FN13,FN14,FN15,FN16,FN17,FN18,FN19,FN20,FN21,FN22,FN23,FB1,FB2,FB3,FB4,FB5,FB6,FB7")
    csv_to_excel(vectorstatutcsv_withEntete, vectorstatut_xsl_withEntete)
    csv_to_excel(vecteurcsv_withEntete, vector_xsl_withEntete)

    #classicalDB
    print("Step2: Create classical DB")
    label_vectors_classicalDB(sourceFile_Failures_CSV, vectorstatutcsv_withEntete, classicalDB_statut)
    create_cassicalDB_step1(vecteurcsv_withEntete, classicalDB)
    csv_to_excel(classicalDB, classicalDB_xsl)
    create_cassicalDB_step2(classicalDB, classicalDB_statut)

    #HypotheticalDatabase
    print("Step3: Create Hypothetical DB")

    count_nbre_appartenance(classicalDB_statut, membership_primitives)
    print("file nbre_appartenance generated with success")
    trie_appartenanceFile(membership_primitives, primitives_membership_trie)
    print("sorted file nbre_appartenance  generated with success")
    print("assign_weights file generated with success: from failures.csv, calculate the number of appearance of failures ")
    assign_weights(sourceFile_Failures_CSV, weight_primitive)

    generate_vector(vector_HBR, 100)
    print("100 vectors generated, they startes by FN14,FN18,FB5")
    reorder_primitives_by_membership(vector_HBR, primitives_membership_trie, vector_HBR_tri_membership)
    print("scheduling according to the number of appearances successfully completed")
    map_vector_failure(vector_HBR_tri_membership, sourceFile_Failures_CSV, HypotheticalDatabaseFile_primitiveNames)
    print("assignment of fault names to vectors successfully completed")
    create_HDB_file(classicalDB, vector_HBR_tri_membership, HypotheticalDatabase_File_primitivevalues)
    print("HypotheticalDatabase_File_primitivevalues generated with success")

    label_HDB(HypotheticalDatabaseFile_primitiveNames,HypotheticalDatabase_File_primitivevalues, HypotheticalDatabaseFile_withlabel)
    print("HypotheticalDatabase created with label !finish")



   #










    print ("well done ! good work")














    # Restoring the standard output to the console
    sys.stdout.close()
    sys.stdout = sys.__stdout__

    #end execution time
    end_time_Preprocessing = time.time()
    execution_time_Preprocessing = end_time_Preprocessing - start_time_Preprocessing
    print(f"execution time : {execution_time_Preprocessing} secondes")
