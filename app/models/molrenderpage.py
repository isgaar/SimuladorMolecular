from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
from app.services.pdb_service import parse_pdb  # Función para procesar archivos PDB

# Crear el enrutador para PDB
router = APIRouter()

@router.post("/upload", response_class=JSONResponse)
async def upload_pdb(file: UploadFile = File(...)):
    try:
        # Directorio temporal para guardar el archivo subido
        temp_dir = Path("app/uploads")
        temp_dir.mkdir(parents=True, exist_ok=True)
        file_path = temp_dir / file.filename

        # Guarda el archivo en el sistema
        with file_path.open("wb") as f:
            f.write(await file.read())

        # Procesa el archivo PDB
        pdb_data = parse_pdb(str(file_path))

        # Lee el contenido del archivo para enviarlo al cliente
        with file_path.open("r") as f:
            pdb_content = f.read()

        return {
            "filename": file.filename,
            "pdb_data": pdb_data,  # Información procesada
            "pdb_content": pdb_content,  # Contenido del archivo PDB
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {e}")

