import random
import csv
import pandas as pd



#generate 100 vectors, each vector contain 21 truth value (70%) and 9 falseValue (30%)
def generate_vectors(sourceFile_primitives_CSV, vecteurcsv, vectorstatutcsv):
    def generate_V1(Vstatut):
        V1 = []

        with open(sourceFile_primitives_CSV, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row_idx, row in enumerate(reader):
                if 0 <= row_idx <= 22:
                    lower_limit = float(row['Lower_Limit'])
                    upper_limit = float(row['Upper_Limit'])

                    if Vstatut[row_idx] == 1:
                        value = random.uniform(lower_limit, upper_limit)
                    else:
                        value = random.uniform(lower_limit, upper_limit)
                elif 23 <= row_idx <= 31:
                    if Vstatut[row_idx] == 1:
                        value = row['TruthValue']
                    else:
                        value = row['FalseValue']

                V1.append(value)

        return V1

    def generate_Vstatut():
        Vstatut = [1] * 21 + [0] * 9
        random.shuffle(Vstatut)
        return Vstatut

    vectors = []
    Vstatuts = []  # Store Vstatut for each vector

    for i in range(1, 101):
        Vstatut = generate_Vstatut()
        Vi = generate_V1(Vstatut)
        vectors.append(Vi)
        Vstatuts.append(Vstatut)

    with open(vecteurcsv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(vectors)



    # Write Vstatuts to a CSV file
    with open(vectorstatutcsv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(Vstatuts)

#generate primitives names ,FN1,FN2,FN3,FN4,FN5,FN6,FN7,FN8,FN9,FN10,FN11,FN12,FN13,FN14,FN15,FN16,FN17,FN18,FN19,FN20,FN21,FN22,FN23,FB1,FB2,FB3,FB4,FB5,FB6,FB7
def generate_vector_strings():
    # Initialize the vector
    vector = []

    # Generate FN strings
    for i in range(1, 24):
        fn_string = f"FN{i}"
        vector.append(fn_string)

    # Generate FB strings
    for j in range(1, 8):
        fb_string = f"FB{j}"
        vector.append(fb_string)

    return vector

#add the entete to the victor file
def add_header_to_vectorsFile(input_file, output_file):
    # Generate the vector of strings
    header_vector = generate_vector_strings()

    # Open the input CSV file and read its contents
    with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Add the header vector to the beginning of the data
    data.insert(0, header_vector)

    # Write the updated data to the output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


