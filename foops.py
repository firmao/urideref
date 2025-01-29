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

# Example usage
ontology_uri = "https://w3id.org/okn/o/sd"
result = assess_ontology(ontology_uri)
print(json.dumps(result, indent=4))
