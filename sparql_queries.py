from SPARQLWrapper import SPARQLWrapper, JSON


def get_all_with_prefix(prefix):
    sparql = SPARQLWrapper("http://localhost:3030/project_dataset/sparql")
    sparql.setQuery("""
        SELECT DISTINCT * WHERE {
          ?sub ?pred ?obj .
           FILTER(strStarts(str(?pred),"""+prefix+""")) .
        }
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    return results

#print(get_all_with_prefix('"http://xmlns.com/foaf/0.1"'))