import os
import glob
import pandas as pd


# Directory with files
os.chdir(r"C:\Users\USUARIO\Desktop\Rafaela\Down")

# Extension of the file that will be used
# Can be change to csv 
extension = 'xlsx'

# Save all the name files
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Concat all the data files
combined_csv = pd.concat([pd.read_excel( f, keep_default_na=True) for f in all_filenames ],sort=False)
print("Dados armazenados! \n")

# Create the file
print('Combinando dados e criando arquivo \n')
combined_csv.to_excel( "combinado.xlsx", index=False, encoding='utf-8-sig')
print('Dados combinado')