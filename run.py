from app import app

#podłoga - specjalne zmienne np. mówią o środowisku 
if __name__ == '__main__': # Ten if wykona sie tylko z pliku run.py
    app.run(debug=True)