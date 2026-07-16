.PHONY: install run

install:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/python -c "import fastapi, uvicorn, httpx; print('ok')"

run:
	.venv/bin/uvicorn app.main:app --reload

seed:
	.venv/bin/python scripts/seed_fake_data.py