FROM python:3.8-slim
RUN apt-get update -y
RUN pip install --upgrade pip
ADD requirements.txt /home/requirements.txt
ADD branch-rules.py /home/branch-rules.py
ADD config.py /home/config.py
RUN pip install -r /home/requirements.txt
CMD ["python","/home/branch-rules.py"]