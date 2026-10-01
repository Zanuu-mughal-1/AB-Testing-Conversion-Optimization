# A/B Testing & Conversion Optimization

A statistically rigorous conversion experiment with uplift calculation, pooled two-proportion z-test, confidence intervals and a business recommendation.

## Skills demonstrated
- A/B testing
- Hypothesis testing
- Two-proportion z-test
- Confidence intervals
- Conversion uplift
- Experiment analysis

## Repository structure
- `data/` — local dataset so the project runs without downloading anything
- `src/main.py` — complete reproducible pipeline
- `outputs/` — generated metrics, tables and visualizations
- `notebook.ipynb` — notebook launcher
- `requirements.txt` — Python dependencies
- `LINKEDIN_POST.md` — concise project description for LinkedIn

## Run
```bash
pip install -r requirements.txt
python src/main.py
```

The random seed is fixed where applicable, so results are reproducible.
