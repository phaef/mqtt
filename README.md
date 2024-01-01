#README


## Setup
This repository requires python virtual enviroments. 

Install python virtual enviroment
```
apt install python3.11-venv
```

Create virtual environment, source it and download required packages
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
### Sender + Receiver
```
python src/main.py 
```

### Sender only
```
python src/sender.py 
```

### Receiver only
```
python src/receiver.py 
```

## Deactivate virtual environment
The virtual enviroment can be deactivated easily by:
```deactivate```

and reactivated by:
```source .venv/bin/activate```
