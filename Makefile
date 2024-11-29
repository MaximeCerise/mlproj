run:
	uvicorn serving.api:app --reload --host 0.0.0.0 --port 8080 & \
	sleep 5 && \
	streamlit run webapp/app.py --server.port 8501