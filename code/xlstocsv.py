import csv
import sys, os, json, re, time
import subprocess

def add_path(f, folder):
    return folder + '/' + f

# It returns all XLSX files from a directory
def getXLSFiles(directory):
    XLSFiles = []
    for x in os.walk(directory):
        for xls in x[2]:
            if os.path.splitext(xls)[1] == '.xlsx':
                full_path = add_path(xls, x[0])
                XLSFiles.append(full_path)
        for folder in x[1]:
            other_files = [add_path(p, x[0]) for p in getXLSFiles(folder)]
            XLSFiles.extend(other_files)
    return XLSFiles

def csv_from_excel(fname, test_name):
    subprocess.Popen(["xlsx2csv " + fname + " --all -d '|' -i -p "
                      "'<New Sheet>' > " + test_name], shell=True)

    return

def main():
    for xlsx in getXLSFiles(sys.argv[1]):
        test_name = os.path.basename(xlsx).split('.')[0] + '.csv'
        lstSheets = csv_from_excel(xlsx, test_name)

        time.sleep(3) # system needs to wait a second to recognize the file was  written

        with open(test_name) as f:
            lines = f.readlines()
            firstSheet = True

            for line in lines:
                if line.startswith('<New Sheet>'):
                    if firstSheet:
                        sh_2_fname = line.replace('<New Sheet>', '').strip().replace(' - ', '_').replace(' ','_')
                        print(sh_2_fname)
                        sh2f = open(sh_2_fname+".csv", "w")
                        firstSheet = False
                    else:
                        sh2f.close()
                        sh_2_fname = line.replace('<New Sheet>', '').strip().replace(' - ', '_').replace(' ','_')
                        print(sh_2_fname)
                        sh2f = open(sh_2_fname+".csv", "w")
                else:
                    sh2f.write(line)
        sh2f.close()

if __name__ == "__main__":
    main()
