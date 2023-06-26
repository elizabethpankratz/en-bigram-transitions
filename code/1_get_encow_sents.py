# -*- coding: utf-8 -*-

# Infile: None.
# Outfile: encow_sents.csv

from SeaCOW import Query, ConcordanceLoader
import pandas as pd

# ======================================================

CORPUS        = 'encow16a-nano'
QUERY         = '<s/> within <div bpc="a"/> within <doc bdc="a"/>' # 350k sents, about 10 min runtime

# ======================================================


def conduct_query(cql_string, corpus):
  """
  Queries the given corpus.
  
  Args:
    cql_string: string in CQL format
    corpus: string representing the corpus to query ('decow16a-nano', 'decow16b', 'encow16a', 'encow16a-nano')
  Returns:
    List of dicts containing the concordances.
  """
  
  q = Query()
  q.corpus          = corpus  
  q.string          = cql_string
  q.attributes      = ['word']
  q.structures      = ['s']
  q.references      = ['doc.url', 'doc.id', 'doc.bdc', 'div.bpc']
  q.container       = 's'
  q.set_deduplication()
  
  p                 = ConcordanceLoader()
  p.full_structure  = True     # Convert token attributes to dicts as well, otherwise |-separated. 
  q.processor       = p
  q.run()
  
  return p.concordance


# Conduct the query.
concs = conduct_query(QUERY, CORPUS)

print(concs)

# Extract the information from each match as long as the match isn't empty.
conc_data = [
  {
    'sent': " ".join([x['word'] for x in conc['match'] if isinstance(x, dict)]),
    'doc.id': conc['meta']['doc.id'],
    'doc.url': conc['meta']['doc.url'],
    'doc.bdc': conc['meta']['doc.bdc'],
    'div.bpc': conc['meta']['div.bpc'],
  } for conc in concs]

# Convert list of dicts to df, save.
conc_df = pd.DataFrame(conc_data)
conc_df.to_csv('encow_sents.csv', index=False, encoding='UTF-8')
