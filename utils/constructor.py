
import pandas as pd

def create_html(data):
    pd.set_option('colheader_justify', 'center') 
    css_dir = "{{url_for('static', filename='css/df_style.css')}}"

    html_string = '''
    <html>
      <head><title>TESTE</title></head>
      <link rel="stylesheet" href="{css}">
      <body>
        {table}
      </body>
    </html>
    ''' 
    

    df = pd.DataFrame(data) 

    
    with open('utils/templates/site/index.html', 'w') as f:
        f.write(html_string.format(css=css_dir,table=df.to_html(classes='mystyle'))) 
        f.close()


    