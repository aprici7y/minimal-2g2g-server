FROM python:3.10.12 
# Or any preferred Python version.
WORKDIR /code 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python" , "-u" ,"main.py"] 
# Or enter the name of your unique directory and parameter set.