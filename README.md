
# Project: Arsenic Concentration Regression (AV1)

This repository was developed for a college assignment and is divided into two main parts: **back-end** and **front-end**.

## Overview

- **Back-end:** Built with Python and FastAPI, responsible for data analysis and regression (multiple linear regression) using a real dataset. All main logic, endpoints, and data processing are here.
- **Front-end:** Built with Next.js (React + TypeScript). The layout is simple and functional, designed to display results and interact with the API. For more details about the front-end, check the `frontEnd` folder and its README inside.

## Structure

```
projeto-final/
├── backEnd/      # FastAPI backend, regression logic, API endpoints
├── frontEnd/     # Next.js frontend, simple dashboard and UI
```

## About the Back-end

The back-end implements multiple linear regression to analyze the relationship between arsenic concentration in nails and several predictors. It exposes endpoints for predictions, metrics, and model comparison. See `backEnd/README.md` for more technical details.

## About the Front-end

The front-end is a minimal Next.js app that consumes the API and presents the results in a dashboard. You can find more information and usage instructions in the `frontEnd` folder.

## How to Run

See each folder (`backEnd` and `frontEnd`) for setup and usage instructions. The back-end requires Python and FastAPI, the front-end requires Node.js and Next.js.

---

Author: Marcos Dias
