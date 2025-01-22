from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.main_routes import router as main_routes
from app.models.molrenderpage import router as molrender_routes  # Importa el enrutador de molrenderpage.py

app = FastAPI()

# Configurar archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Registrar las rutas principales
app.include_router(main_routes)

# Registrar las rutas de PDB con un prefijo
app.include_router(molrender_routes, prefix="/pdb", tags=["PDB"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
