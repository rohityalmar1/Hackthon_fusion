# GeoChangeAI

GeoChangeAI is a starter project for detecting changes between pairs of satellite or aerial images.

## Project layout

- `backend/` — FastAPI service and Python modules
- `frontend/` — Vite web client
- `data/sample_pairs/` — input image pairs for development
- `data/reference_masks/` — optional reference change masks
- `outputs/` — generated maps, masks, and reports
- `src/`, `tests/` — existing change detection implementation and tests

## Run the starter backend

```powershell
cd backend
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

## Run the starter frontend

```powershell
cd frontend
npm install
npm run dev
```
