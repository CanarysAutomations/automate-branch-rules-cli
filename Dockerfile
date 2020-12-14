FROM python:3.8-slim
RUN apt-get update -y
RUN pip install --upgrade pip
ADD requirements.txt /requirements.txt
ADD header.txt /header.txt
ADD automate-branch-rules.py /automate-branch-rules.py
ADD config.py /config.py
ADD CODEOWNERS /CODEOWNERS
ADD codeowners.py /codeowners.py
RUN pip install -r /requirements.txt
CMD ["python","/automate-branch-rules.py"]
