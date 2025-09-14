
# Front-end (Next.js) - Arsenic Regression Dashboard

This folder contains the front-end for the Arsenic Concentration Regression project, developed for a college assignment. The app is built with Next.js and TypeScript, and connects to the FastAPI back-end to display regression results and predictions in a simple dashboard layout.

## How to run locally

1. Install dependencies:
	yarn install
2. Start the development server:
	yarn dev
3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Features

- Simple and clean dashboard UI
- Uses [shadcn/ui](https://ui.shadcn.com/) component library for fast delivery, charts, and responsive design
- Consumes the FastAPI back-end for predictions and metrics
- Tabs for model info, prediction, residuals, and model comparison
- Theme switcher (light/dark/system)

## Editing and Customization

- Main page: `src/app/page.tsx`
- UI components: `src/components/`
- You can easily change the layout, colors, and add new features as needed.

## Notes

- Make sure the back-end API is running and accessible for the dashboard to work.
- The layout is intentionally simple, as the main focus of the project is to demonstrate multiple linear regression analysis.

---

Author: Marcos Dias
