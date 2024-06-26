# Import the logging configuration




import sys
import time

from PSK_vector.segmentation.scripts.generate_values_to_subDB import regroupe_according_Feature, \
    regroupe_according_Panne, create_values_forFeature, generate_value_forGroup_features, \
    generate_value_forGroup_pannes, nettoyer_tous_les_csv, appliquer_compter_occurences_sur_dossiers_pannes, \
    appliquer_compter_occurences_sur_dossiers_feature
from ClassicalDataBase.script.classicalDB import label_vectors_classicalDB, create_cassicalDB_step1, \
    create_cassicalDB_step2
from GeneralScripts.convert_type_file import excel_to_csv, csv_to_excel
from GeneralScripts.empty_folder import empty_folder
from GeneralScripts.pretretmatet_CBR import remove_header_and_save, remove_header_and_last_column
from HypotheticalDatabase.scripts.createHypDB import count_nbre_appartenance, trie_appartenanceFile, assign_weights, \
    generate_vector, reorder_primitives_by_membership, map_vector_failure, create_HDB_file, label_HDB
from PSK_vector.segmentation.scripts.segmentation import extract_failures, create_HCB, remplir_vecteur_failure, \
    extract_feature, remplir_vecteur_feature, create_CB_H_LPF, process_files, groupe_primitive_valueByName
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
data_without_label = 'ClassicalDataBase/result/data_without_label.csv'
data_without_header = 'ClassicalDataBase/result/data_without_header.csv'

#HypotheticalDatabase
membership_primitives = "HypotheticalDatabase/files/primitives_membership.csv"
primitives_membership_trie = "HypotheticalDatabase/files/primitives_membership_trie.csv"
weight_primitive = "HypotheticalDatabase/files/weight_primitive.csv"
vector_HBR = "HypotheticalDatabase/files/vector_HBR.csv"
vector_HBR_tri_membership = "HypotheticalDatabase/files/vector_HBR_tri_membership.csv"
HypotheticalDatabaseFile_primitiveNames = "HypotheticalDatabase/result/HDB_File_structure.csv"
HypotheticalDatabase_File_primitivevalues = "HypotheticalDatabase/files/HDB_File_primitivevalues.csv"
HypotheticalDatabaseFile_withlabel = "HypotheticalDatabase/result/HDB_File_labled.csv"

#segmentationFiles
failure_list = "PSK_vector/segmentation/failure_list.csv"
output_folder = "PSK_vector/segmentation/sub_databases"
feature_list = "PSK_vector/segmentation/feature_list.csv"
source_folder_CB_H_LPF = 'PSK_vector/segmentation/sub_databases/CB_H/withPanne'
destination_folder_CB_H_LPF = 'PSK_vector/segmentation/sub_databases/CB_H_LPF'
directoryResultSegmentation = "PSK_vector/segmentation/sub_databases/CB_H_LPF/withpanne"
file_p = "PSK_vector/segmentation/sub_databases/CB_H_LPF/withpanne/p1_FB1_withpanne.csv"
CBRFile = "ClassicalDataBase/result/data_without_header.csv"
primlist = "PSK_vector/segmentation/primlist.csv"
vecteurResult = 'PSK_vector/segmentation/vecteur.csv'




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
    empty_folder("PSK_vector/segmentation/sub_databases")
    empty_folder("PSK_vector / segmentation / result")
    empty_folder("PSK_vector / segmentation / courbes_Histogrammes")
    empty_folder("courbe_result_good")
    empty_folder("PSK_vector / segmentation / _primlist")

    #pretraitement
    print("Step1: preatraitement phase")
    print ("    - generate 2 files containt 1000 vectors   ")
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

    generate_vector(vector_HBR, 1000)
    print("1000 vectors generated, they startes by FN14,FN18,FB5")
    reorder_primitives_by_membership(vector_HBR, primitives_membership_trie, vector_HBR_tri_membership)
    print("scheduling according to the number of appearances successfully completed")
    map_vector_failure(vector_HBR_tri_membership, sourceFile_Failures_CSV, HypotheticalDatabaseFile_primitiveNames)
    print("assignment of fault names to vectors successfully completed")
    create_HDB_file(classicalDB, vector_HBR_tri_membership, HypotheticalDatabase_File_primitivevalues)
    print("HypotheticalDatabase_File_primitivevalues generated with success")

    label_HDB(HypotheticalDatabaseFile_primitiveNames,HypotheticalDatabase_File_primitivevalues, HypotheticalDatabaseFile_withlabel)
    print("HypotheticalDatabase created with label !finish")


   #cration of a New target case_calcul of PSK
    print ("Step4: create of a New target case: PSK ")
    print("We will do two methods to create PSK ")
    print("1- Feature possibility distributions (for a given failure pk): pM,k(fM)")
    print("        Sub-step 1 : From H-CB")
    print("              - Create case base where cases are labeled with the selected failure: CB_H_LP")
    print("              - Create case base where cases are NOT labeled with the selected failure CB_H_L/P")
    extract_failures(sourceFile_Failures_CSV, failure_list)

    vecteur_failure = remplir_vecteur_failure(failure_list)
    create_HCB(HypotheticalDatabaseFile_primitiveNames, output_folder,vecteur_failure)

    print("CB_H_L/P & CB_H_LP : all failures created with success")

    print("        Sub-step 2 : From CB_H_LP")
    print("              - Create case base where cases are labeled with the selected failure: CB_H_LPF")
    print("              - Create case base where cases are NOT labeled with the selected failure CB_H_LP/F")
    extract_feature(sourceFile_primitives_CSV, feature_list)
    vecteur_feature = remplir_vecteur_feature(feature_list)
    create_CB_H_LPF(source_folder_CB_H_LPF, vecteur_feature, destination_folder_CB_H_LPF)
    print("CB_H_LPF & CB_H_LP/F : all feature created with success")

    #preprocessing classiclDB file to extract values
    remove_header_and_last_column(classicalDB, data_without_label)
    remove_header_and_save(data_without_label, data_without_header)
    process_files(file_p, CBRFile,primlist)
    print("Values vector affected with success")
    groupe_primitive_valueByName(primlist, vecteurResult)
    print("Vectors created with success")

    print("2- Failure possibility distribution (for a given feature): p. / fm(pk) ")
    extract_feature(sourceFile_primitives_CSV, feature_list)
    vecteur_feature = remplir_vecteur_feature(feature_list)

    print("Affect value to to sub-databases___to plot")


    # create data for calculate curves of cas1 & cas 2
    # Appel de la fonction pour regrouper les fichiers Feature
    base_dir = "PSK_vector/segmentation/sub_databases/CB_H_LPF/withpanne"
    groupe_files_byFeatures = "PSK_vector/segmentation/sub_databases/groupe/Feature"
    regroupe_according_Feature(base_dir, groupe_files_byFeatures)

    # Appel de la fonction pour regrouper les fichiers Panne
    base_dir = "PSK_vector/segmentation/sub_databases/CB_H_LPF/withpanne"
    groupe_files_bypannes = "PSK_vector/segmentation/sub_databases/groupe/Panne"
    regroupe_according_Panne(base_dir, groupe_files_bypannes)

    # Appel de la fonction pour créer les valeurs aléatoires des Feature
    primitivesFile = "sourceFiles/primitives.csv"
    generatesVectors = "sourceFiles/randomValue_forFeatureVector.csv"
    create_values_forFeature(primitivesFile, generatesVectors)

    # Cas 1 : extract primitive value primitive in panne
    FeatureGroup = "PSK_vector/segmentation/sub_databases/groupe/Feature"
    generate_value_forGroup_features(FeatureGroup)

    # cas 2 : extract primitive value selon la panne with primitive
    PanneGroup = "PSK_vector/segmentation/sub_databases/groupe/Panne"
    generate_value_forGroup_pannes(PanneGroup)

    # netoyer la colonne val dans tous les fichiersFeature
    folder_path_Feature = "PSK_vector/segmentation/sub_databases/groupe/Feature"
    nettoyer_tous_les_csv(folder_path_Feature)

    # netoyer la colonne val dans tous les fichiers Panne
    folder_path_Panne = "PSK_vector/segmentation/sub_databases/groupe/Panne"
    nettoyer_tous_les_csv(folder_path_Panne)

    # création des fichiers de données pour feature
    folder_path_feature = "PSK_vector/segmentation/sub_databases/groupe/Feature"
    appliquer_compter_occurences_sur_dossiers_feature(folder_path_feature)

    # création des fichiers de données pour pannes
    folder_path_Panne = "PSK_vector/segmentation/sub_databases/groupe/Panne/"
    output_folder_panne = "PSK_vector/segmentation/sub_databases/groupe/Panne/courbefiles_pannes/"
    appliquer_compter_occurences_sur_dossiers_pannes(folder_path_Panne, output_folder_panne)



    print ("well done ! good work")









    # Restoring the standard output to the console
    sys.stdout.close()
    sys.stdout = sys.__stdout__

    #end execution time
    end_time_Preprocessing = time.time()
    execution_time_Preprocessing = end_time_Preprocessing - start_time_Preprocessing
    print(f"execution time : {execution_time_Preprocessing} secondes")
