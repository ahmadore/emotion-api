# Emotion Detecction APi

This code is written in Python. To use the code you'll need the following:

- Python 2.7
- A recent version of [NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/)
- [scikit-learn](http://scikit-learn.org/stable/index.html)
- [OpenCV-Python](http://opencv.org/)
- [Matplotlib](http://matplotlib.org/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
git clone https://github.com/ahmadore/emotion-api.git #clone the project repo
cd /emotion-api #change working directory to project folder
pip install -r requirements.txt # install project dependencies
```

## Start Server

```
python web/main.py #to run server
```

## Usage

Lunch your favorite browser and go to [local-host](http://localhost:5000)

To classify emotions, you can either use

1. Use query-string in the following endpoint:
   endpoint: localhost:5000/classify-query?age=Number&pulse_rate=Number
   method: GET

2. Use Json-object in the following endpoint:
   enpoint: locahost:5000/classify-json
   method: POST
   data: {age: number, pulse_rate:number}

### NB

If you host the project on a remote server, then replace the localhost part of the url with your server IP, or domain name

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
