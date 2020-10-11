FROM python:3.8-slim
RUN apt-get update -y
RUN pip install --upgrade pip
ADD requirements.txt /home/requirements.txt
ADD github-branch-protector.py /home/github-branch-protector.py
ADD config.py /home/config.py
ADD CODEOWNERS /home/CODEOWNERS
ADD codeowners.py /home/codeowners.py
RUN pip install -r /home/requirements.txt
CMD ["python","/home/github-branch-protector.py"]