install:
	pip install -e .

test:
	pytest tests

run:
	python main.py

run_app:
	uvicorn app.app:app --reload --host 127.0.0.1 --port 8000

run_gradio:
	python app/gradio_app.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
