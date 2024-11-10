# AI-Outreach-Agents

Example Url: 
 
First run in screenshot folder

        npm i 

and in main folder

        pip install -r requirements.txt


Then run the json_loads.sh with parameter the url


        bash json_loads.sh URL
        

Then index.json and color.json will be generted

Now you need to in main folder run 

        python -m http.server
        
in a new terminal in screenshot run 

        node index.js http://localhost:8000/


