from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.stem_cells import router as stem_cells_router
from routers.blood_cells import router as blood_cells_router
from routers.bonemarrow import router as bonemarrow_router
from routers.biopsy_tissue import router as tissue_router
from routers.pheripheral_blood import router as peripheral_blood_router
from routers.saliva import router as saliva_router


app = FastAPI(title="Bio Nexsus API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


# Mount routers
app.include_router(stem_cells_router)
app.include_router(blood_cells_router)
app.include_router(bonemarrow_router)
app.include_router(tissue_router)
app.include_router(peripheral_blood_router)
app.include_router(saliva_router)
