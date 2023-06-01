from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifParser
from pprint import pprint
from pandas import DataFrame

MAPI_KEY =('')  #API Key
m= MPRester(MAPI_KEY)
from zipfile import ZipFile
data = m.query(criteria={"elements": {"$in": ["Li"], "$all": ["O", "Mn", "Ni"]}, "nelements": 4}, properties=['material_id','cif'])
d=-1
for d in data:
    d =+ 1
    poscar = Structure.from_str(data[d]["cif"], fmt="cif").to(fmt="poscar")
    print (poscar)


with ZipFile('Li ion_cif.zip', 'w') as f:
        for d in data:
            f.writestr('{}.cif'.format(d['material_id']), d['cif'])


