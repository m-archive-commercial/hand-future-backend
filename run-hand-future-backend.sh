source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 3001 --workers 4