FROM python:3.13

# Set working directory
WORKDIR /Momentum_Strategies

# install dependecies
COPY ./requirements.txt /Momentum_Strategies
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip3 install jupyter

# Copy project files
COPY . /Momentum_Strategies

CMD ["jupyter", "notebook", "--ip=*", "--allow-root"]
