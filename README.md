RUNNING Local LLM(MISTRAL) USING OLLAMA TO READ PDF'S
=====================================================


Install required packages by running this command in an virtual environment
---------------------------------------------------------------------------
pip install -r requirements.txt


Run populate_database.py to load the pdf and store its vector embeddings in the chromadb
----------------------------------------------------------------------------------------
python populate_database.py


Run query.py to ask questions
-----------------------------
python query.py


To Install Ollama
-----------------
Install ollama at https://ollama.com/ 

Run these commands in separate terminal
=======================================
To install mistral llm
----------------------
ollama pull mistral

Host the server locally
-----------------------
ollama serve

To kill ollama run this command
-------------------------------
Get-Process | Where-Object {$_.ProcessName -like '*ollama*'} | Stop-Process