from SPARQLWrapper import SPARQLWrapper, JSON

def execute_sparql_query(query):
    endpoint = "https://api.kg.odissei.nl/datasets/odissei/odissei-kg-acceptance/sparql"
    
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    
    try:
        results = sparql.query().convert()
        return results["results"]["bindings"]
    except Exception as e:
        print(f"Error executing SPARQL query: {e}")
        return None

if __name__ == "__main__":
    sample_query = """
    prefix schema: <http://schema.org/>
    Select * Where {
        ?s a schema:Book
    }
    """
    
    results = execute_sparql_query(sample_query)
    if results:
        for result in results:
            print(result)
