from utils.data.conect import show
from utils.constructor import create_html
from utils.routes import app



def main():
    create_html(show()) # Creating a HTML with TinyDb data  
    
    

if __name__ == "__main__":
    main()
    
    app.run(debug=True, host='0.0.0.0') # Starting the server
    
   