from Bio.PDB import PDBParser
import os

def parse_pdb(file_path: str):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("structure", file_path)

    atoms = []
    chains = set()
    residues = set()

    for model in structure:
        for chain in model:
            chains.add(chain.get_id())
            for residue in chain:
                residues.add(residue.get_resname())
                for atom in residue:
                    atom_data = {
                        "atom_name": atom.get_name(),
                        "residue_name": residue.get_resname(),
                        "x": atom.get_coord()[0],
                        "y": atom.get_coord()[1],
                        "z": atom.get_coord()[2]
                    }
                    atoms.append(atom_data)

    pdb_data = {
        'atoms': len(atoms),
        'chains': list(chains),
        'residues': list(residues),
        'size': os.path.getsize(file_path)  # Tamaño del archivo PDB
    }

    return pdb_data
