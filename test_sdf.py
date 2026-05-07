from rdkit import Chem

suppl = Chem.SDMolSupplier(r"D:\data\CMNPD_1.0_2d.sdf")

for i, mol in enumerate(suppl):
    if mol is not None:
        smiles = Chem.MolToSmiles(mol)
        print(smiles)
    if i > 10:
        break