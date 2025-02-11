import requests
import json
import csv

def assess_ontology(ontology_uri):
    url = "https://foops.linkeddata.es/assessOntology"
    headers = {
        "accept": "application/json;charset=UTF-8",
        "Content-Type": "application/json;charset=UTF-8"
    }
    data = json.dumps({"ontologyUri": ontology_uri})
    
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 200:
        #return response.json().get("overall_score", "No score available")
        return response.json()
    else:
        return "Error"

def fetch_ontology_list(file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        print(f"Failed to fetch the ontology list. Status code: {response.status_code}")
        return []

def process_ontologies(file_url):
    ontology_list = fetch_ontology_list(file_url)
    results = []
    
    for idx, ontology_uri in enumerate(ontology_list, start=1):
        if ontology_uri.strip():  # Ensure it's not an empty line
            fileEval = assess_ontology(ontology_uri.strip())
            score = fileEval.get("overall_score", "No score available")
            var_f = fileEval.get("overall_score", "No score available")
            var_a = fileEval.get("overall_score", "No score available")
            var_i = fileEval.get("overall_score", "No score available")
            var_r = fileEval.get("overall_score", "No score available")
            output_filename = f"ontology_assessment_{idx}.json"
            with open(output_filename, "w", encoding="utf-8") as f:
                json.dump(fileEval, f, indent=4)
            #results.append([output_filename, score])
            results.append([ontology_uri.strip(), var_f, var_a, var_i, var_r, score])
            print(f"Saved: {output_filename}")
    
    # Save results as a table in a CSV file
    with open("ontology_assessment_summary.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["File Name", "F", "A", "I", "R", "Overall Score"])
        writer.writerows(results)
    print("Saved: ontology_assessment_summary.csv")

# Example usage
file_url = "https://raw.githubusercontent.com/firmao/urideref/refs/heads/main/ontology_list2.txt"  # Replace with actual URL
process_ontologies(file_url)
