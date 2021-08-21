# Tabula documentation: https://tabula-py.readthedocs.io/en/latest/
# pip install tabula-py

import tabula

PDF = input("Enter the path of the file")
# Get the pdf file containing the table

page = input("Enter the page on which the table is found")
# Get the page no. on which the table is found

pdf_file = tabula.read_pdf(PDF, pages=int(page))
# Read PDF and extract table into dataframe variable

print(pdf_file)
# Preview dataframe

print("Is the above table the one you wish to convert? (Y/N)")

conf = input()

while (conf == "N") or (conf == "n"):
    print("What would you like to update?\n"
          "1. Path\n"
          "2. Page\n")
    update = input()

    #if update != '1' and update != '2':
        #print("Enter a valid option")
    # Check for invalid response

    if update == '1':
        PDF = input("Enter the path of the file")
    elif update == '2':
        page = input("Enter the page on which the table is found")

    pdf_file = tabula.read_pdf(PDF, pages=int(page))

    print(pdf_file)

    print("Is the above table the one you wish to convert? (Y/N)")

    conf = input()
# Allow user to change the table selected

print("What format would you like to convert it to?\n"
      "1.CSV\n"
      "2.JSON\n")

convert_to = input()

#if convert_to != '1' or convert_to != '2':
    #print("Enter a valid option")
# Check for invalid response

if convert_to == '1':
    tabula.convert_into(PDF, "converted.csv", output_format="csv", pages=int(page))
# Call CSV conversion func
elif convert_to == '2':
    tabula.convert_into(PDF, "converted.json", output_format="json", pages=int(page))
# Call JSON conversion func

print("Converted Successfully!")
