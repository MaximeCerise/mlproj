docker build -t my-app -f Dockerfile .
docker run --name proj -d -p 8080:8080 -p 8501:8501 -p 8502:8502 maxcerise/mlproj:latest
docker exec proj /bin/bash -c "source pyenv/bin/activate && make run"
      