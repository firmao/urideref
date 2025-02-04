import requests
import json

def assess_ontology(ontology_uri):
    url = "https://foops.linkeddata.es/assessOntology"
    headers = {
        "accept": "application/json;charset=UTF-8",
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = json.dumps({"ontologyUri": ontology_uri})
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}", "details": response.text}

def fetch_ontology_list(file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to fetch the ontology list. Status code: {response.status_code}")
        return []

def process_ontologies(file_url):
    ontology_list = fetch_ontology_list(file_url)
    
    for idx, ontology_uri in enumerate(ontology_list, start=1):
        if ontology_uri.strip():  # Ensure it's not an empty line
            result = assess_ontology(ontology_uri.strip())
            output_filename = f"ontology_assessment_{idx}.json"
            with open(output_filename, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4)
            print(f"Saved: {output_filename}")

# Example usage
file_url = "https://example.com/ontology_list.txt"  # Replace with actual URL
process_ontologies(file_url)
