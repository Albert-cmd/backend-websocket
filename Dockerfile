FROM python:3.9
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
COPY requirements.txt ./requirements.txt
COPY ./ ./
RUN pip install opencv-contrib-python-headless
RUN pip install numpy
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]