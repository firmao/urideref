# URI dereferenceable
This demonstrates how to make URIs dereferenceable and generate RDF content dynamically by querying a triple store in Python using Flask and SPARQL.

A URI (Uniform Resource Identifier) is dereferenceable if it can be used to retrieve a resource over the web, typically via HTTP or HTTPS. To make a URI dereferenceable, follow these steps:

1. Assign a URI to a Resource
A URI should represent a specific resource, such as a webpage, an image, a document, or even a piece of data in a knowledge graph. Ensure the URI is well-formed and unique.
2. Configure a Web Server
Set up a web server (such as Apache, Nginx, or any other web server) to host the resource.
The web server should be configured to handle HTTP/HTTPS requests for that URI.
3. Map the URI to a Resource
Map the URI to the resource you want to serve. This can be a file (e.g., example.com/resource.jpg) or dynamic content generated by the server.
4. Respond with Appropriate HTTP Status Codes
200 OK: If the resource exists and can be directly retrieved, return the content with a 200 status code.
301/302 Redirect: If the URI is meant to point to another URI, configure an HTTP redirect.
303 See Other: If the URI represents a non-information resource (e.g., a concept, not a document), use a 303 redirect to another URI that provides more information about the resource.
5. Return Useful Metadata (Optional)
In the HTTP headers or within the response body, include metadata that describes the resource. For Linked Data, this could be RDF, JSON-LD, or other machine-readable formats.
Example for Linked Data Dereferencing:
If a URI represents a concept (e.g., a person or a place in a knowledge graph), it should redirect to a document that describes the resource.
For instance, if the URI http://example.com/person/123 represents a person, the server might return a 303 redirect to http://example.com/person/123.html, which provides human-readable information about that person.
Summary:
To make a URI dereferenceable, ensure it can be resolved to an actual resource by configuring a web server to respond to HTTP/HTTPS requests for that URI, and return appropriate status codes and content.

## Running the code (simple one):
```
pip install Flask SPARQLWrapper rdflib
```
Run the script: ```python first.py```.

Open a browser and go to ```http://localhost:5000/person/1``` to see the dereferencing in action.

On GitHub's codespace, add ```/person/1``` to the URL.

# With a triple store:
## Explanation for derefTStore.py:
**SPARQLWrapper**: This library sends SPARQL queries to the triple store (a SPARQL endpoint, in this case). We use the ```CONSTRUCT``` query to retrieve RDF triples related to a person and return the data in Turtle format.

**SPARQL Query**: The query dynamically constructs RDF triples about a person (name, age, and occupation) from the triple store using the ```foaf:name, ex:age, and ex:occupation``` properties.

**SPARQL Endpoint**: The SPARQL_ENDPOINT variable points to your triple store. In this example, it is assumed you are using a local instance of a triple store (e.g., GraphDB, Blazegraph, or Fuseki) at ```http://localhost:7200/repositories/my-repo```.

**Returning Turtle Format**: The query results are returned in Turtle format, and the Flask app sends them back with the appropriate ```MIME type (text/turtle)```.

## Triple Store Setup:
For this to work, you need a triple store with data already loaded, and the person data should follow the foaf and ex ontologies. 

For example, you can load RDF data like this into your triple store:
```
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ex: <http://example.com/> .

<http://example.com/person/1> a foaf:Person ;
    foaf:name "John Doe" ;
    ex:age 30 ;
    ex:occupation "Engineer" .

<http://example.com/person/2> a foaf:Person ;
    foaf:name "Jane Smith" ;
    ex:age 25 ;
    ex:occupation "Doctor" .
```
## Running the Code:
Ensure your triple store is running and contains the relevant RDF data.

Run the script: ```python derefTStore.py```.

Visit ```http://localhost:5000/person/1/info``` to see the RDF data for person 1 in Turtle format, dynamically fetched from the triple store.

On GitHub's codespace, add ```/person/1/info``` to the URL.

We use as reference the W3C specification: [https://www.w3.org/2001/tag/doc/httpRange-14/2007-05-31/HttpRange-14](https://www.w3.org/2001/tag/doc/httpRange-14/2007-05-31/HttpRange-14)


