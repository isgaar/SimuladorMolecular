from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Configuración de plantillas
templates = Jinja2Templates(directory="app/templates")

# Crear el enrutador
router = APIRouter()

# Ruta para renderizar index.html
@router.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Ruta para renderizar renderonline.html
@router.get("/library/renderonline.html")
async def render_online(request: Request):
    return templates.TemplateResponse("library/renderonline.html", {"request": request})
