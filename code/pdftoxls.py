import os
import pdftables_api

def add_path(f, folder):
    return folder + '/' + f

# It returns all PDF files from a directory
def getPDFFiles(directory):
    PDFFiles = []
    for x in os.walk(directory):
        for pdf in x[2]:
            if os.path.splitext(pdf)[1] == '.pdf':
                full_path = add_path(pdf, x[0])
                PDFFiles.append(full_path)
        for folder in x[1]:
            other_files = [add_path(p, x[0]) for p in getPDFFiles(folder)]
            PDFFiles.extend(other_files)
    return PDFFiles

def main():
    # Get API Key from Environment variable
    api_key = os.environ.get('PDFTABLES_API_KEY')

    if api_key == None:
        print 'You need to set the API Key for PDF Tables.'
        return

    # Get the PDFTables API Client
    c = pdftables_api.Client(api_key)

    # Search all the folders in datos
    # For each PDF I find
    # Convert it into XLS with the same name
    for pdf in getPDFFiles('./datos/Solicitudes'):
        new_name = os.path.splitext(pdf)[0] + '.xlsx'
        new_csv_name = os.path.splitext(pdf)[0] + '.csv'
        print "PDF {} converted into {} and {}".format(pdf, new_name, new_csv_name)
        c.xlsx(pdf, new_name)
        c.csv(pdf, new_csv_name)

if __name__ == "__main__":
    main()
