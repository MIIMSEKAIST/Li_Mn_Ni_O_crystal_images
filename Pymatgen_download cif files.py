from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifParser
from pprint import pprint
from pandas import DataFrame

MAPI_KEY =  "mgpDznA4dUNKyF7O" #My API Key

#defining the material object
m= MPRester(MAPI_KEY)
#data = m.query(criteria={}, properties=["battery_id"])
#structure = m.get_structures(QUERY)
#pprint(data)

#"Li", "Ni", "Mn","Co", "Al", "Si", "Fe", "P","V","Mg","Si"
#pprint(m.get_data("Li2O", prop="structure"))
from zipfile import ZipFile
from pymatgen.core import Lattice, Structure, Molecule
# Get the data of all compounds containing either Li, Mn or Ni with O.
data = m.query(criteria={"elements": {"$in": ["Li"], "$all": ["O", "Mn", "Ni"]}, "nelements": 4}, properties=['material_id','cif'])
''''''
d=-1
for d in data:
    d =+ 1
    poscar = Structure.from_str(data[d]["cif"], fmt="cif").to(fmt="poscar")
    print (poscar)


with ZipFile('Li ion_cif.zip', 'w') as f:
        for d in data:
            # print (d)
            f.writestr('{}.cif'.format(d['material_id']), d['cif'])
#print (len(data))
#print (data)
'''
with ZipFile('Li ion_cif.zip', 'w') as f:
    for d in data:
        #print (d)
        f.writestr('{}.cif'.format(d['material_id']),d['cif'])
'''
#structure = m.get_data(data)
#print(structure)

#df = DataFrame(data, columns=["material_id","pretty_formula","unit_cell_formula", "formation_energy_per_atom", "crystal_system", "spacegroup.symbol", "nsites","volume", "density", "band_gap", "e_above_hull"])
#(print (df))
#print (df["unit_cell_formula"])

#Extract formula numbers from "pretty_formula"

#import re as re
#print(df)
#def find_number(text):
        #num = re.findall(r'[0-9]+',text)
        #return " ".join(num)


#df['cell']=df['pretty_formula'].apply(lambda x: find_number(x))

#print (df['cell'])
#print (df.to_csv('Li cathode materials data_V2.csv', index=False)) #save data in csv file



