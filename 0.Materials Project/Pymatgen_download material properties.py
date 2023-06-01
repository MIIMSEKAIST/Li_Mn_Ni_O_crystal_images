from pymatgen import MPRester
from pymatgen.io.cif import CifParser
from pprint import pprint
from pandas import DataFrame

#Pymatgen version: 2020.3.3
m= MPRester(MAPI_KEY)
data = m.query(criteria={"elements": {"$all": ["Li", "Mn", "Ni", "O"]}, "nelements": 4},
               properties=["material_id", "pretty_formula", "crystal_system", "spacegroup.symbol", "band_gap", "e_above_hull"])

df = DataFrame(data, columns=["material_id","pretty_formula", "crystal_system", "spacegroup.symbol","band_gap", "e_above_hull"])
print (df.to_csv('LMNO.csv', index=False)) 



