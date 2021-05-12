# airtable-streamlit

Access Airtable data via Streamlit  
For demo purpose

## Instructions

Requirements

- Poetry
- Python 3.9

### To install dependencies

```{bash}
poetry install
```

### To add Airtable API Key

```{bash}
cp .streamlit/secrets.example.toml .streamlit/secrets.toml
```

Then, add the key in the file. You may request the key for the demo by requesting access to this table https://airtable.com/shrgCbVCeTbLNjLA4.

### To run Streamlit app

```{bash}
poetry run streamlit run airtable-streamlit.py
```
