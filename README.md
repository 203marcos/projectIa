# AV1 Project - Arsenic Analysis API

This repository contains a data analysis and regression project, with a main focus on the Python FastAPI back-end.

## Back-end structure

backEnd/
- data/                (CSV dataset: Dataset Projeto IA.csv)
- env/                 (Python virtual environment)
- helpers/             (utility functions: data reading, regression, etc)
- routes/              (API routes, main file: route.py)
- src/                 (FastAPI app initialization)
- test/                (unit tests)
- requirements.txt     (project dependencies)

## Main dependencies

- fastapi
- uvicorn
- numpy
- pandas
- pydantic

## How to run the back-end locally

1. Go to the backEnd folder:
	cd backEnd
2. Activate the virtual environment:
	source env/bin/activate
3. Install dependencies:
	pip install -r requirements.txt
4. Start the API (for route.py):
	uvicorn routes.route:app --reload

## Main endpoints

- GET /api/modelo : returns regression model metrics and coefficients
- POST /api/predizer : receives input and returns a prediction
- GET /api/residuos : returns the model residuals table
- GET /api/modelo-alternativo : returns metrics for an alternative model

## Notes

- CORS should be configured to allow your front-end domain (e.g., Vercel)
- The front-end consumes the API via HTTP requests

---

Author: Marcos Dias
