Things you'll need:

1. An active deployment of an OpenAI model (I am using gpt-4o-mini)
2. A python package manager (this project is compatible with `uv` and `pip`)

Codebase:

`main2.ipynb`

Expected input format:

Excel sheet with the same headersSame as the ones in `LM Applications 20250502.xlsx` (uploaded on the esynergy sharepoint folder on Teams)

Steps to run the code:

1. Copy the `.env.sample` file and paste it as `.env`
2. Replace the 'XXXXXXX' with relevant values
3. The relevant values can be obtained from the Azure OpenAI deployment page
   ENDPOINT_URL - Under the 'Endpoint' box
   AZURE_OPEN_AI_API_KEY - Under the 'Endpoint' box
   DEPLOYMENT_NAME_1 - The name you gave to the deployment when you deployed the model (if you didn't it'll be the name of the model e.g. gpt-4o-mini)
   API_VERSION - The API version is also included in the ENPOINT_URL. Include the 'preview' (e.g. "2024-12-01-preview")
4. Ensure all env variables are enclosed by inverted commas
5. Create a virtual environment using `python3 -m venv .venv` or `uv venv` in the root directory of the project and enter the virtual environment
6. Activate the venv: Windows command `.venv/Scripts/Activate` or `.venv/Scripts/Activate.ps1`; Mac command `source .venv/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` or `uv sync` to install the dependencies
8. Navigate to `main2.ipynb` and in the first cell, change the values of the following 2 variables: `file_to_save_processed` and `file_to_import_unprocessed`
9. Run each cell individually

In case something breaks and you can't figure out why, feel free to email me!
