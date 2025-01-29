from rdflib import Graph

def load_graph(file_path):
    format = "trig" if file_path.endswith(".trig") else "turtle"
    graph = Graph()
    graph.parse(file_path, format=format)
    return graph

def compare_graph_properties(graph1, graph2):
    properties1 = set(p for s, p, o in graph1)
    properties2 = set(p for s, p, o in graph2)
    
    common_properties = properties1 & properties2
    unique_to_graph1 = properties1 - properties2
    unique_to_graph2 = properties2 - properties1
    different_properties = unique_to_graph1 | unique_to_graph2
    
    return {
        "common_properties": common_properties,
        "unique_to_graph1": unique_to_graph1,
        "unique_to_graph2": unique_to_graph2,
        "different_properties": different_properties
    }

# Example usage
graph1 = load_graph("https___tools.clariah.nl_data_.trig")
#graph2 = load_graph("https___w3id.org_odissei_ns_kg_graph_codelib_liss.trig")
graph2 = load_graph("https___w3id.org_odissei_ns_kg_graph_codelib_cbs.trig")

#graph1 = load_graph("odissei.ttl")
#graph2 = load_graph("odissei2.ttl")

comparison_result = compare_graph_properties(graph1, graph2)

print("Common Properties:")
for prop in comparison_result["common_properties"]:
    print(prop)

print("\nUnique to Graph 1:")
for prop in comparison_result["unique_to_graph1"]:
    print(prop)

print("\nUnique to Graph 2:")
for prop in comparison_result["unique_to_graph2"]:
    print(prop)

print("\nAll Different Properties:")
for prop in comparison_result["different_properties"]:
    print(prop)