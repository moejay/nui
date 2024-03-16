
fe-deps:
	cd frontend && npm install
fe: fe-deps
	cd frontend && npm run dev

be-deps:
	source venv/bin/activate && pip3 install -r requirements.txt
be: be-deps
	source venv/bin/activate && uvicorn main:app --reload