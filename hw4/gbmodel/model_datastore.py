from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ department, coursenumber, quarter , year , instructor ,review ]
    where department, coursenumber, quarter , year , instructor and review are Python strings
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['department'],entity['coursenumber'],entity['quarter'],entity['year'],entity['instructor'],entity['review']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cloud-f21-mazin-ashfaq-ashfaq')

    def select(self):
        query = self.client.query(kind = 'HW4')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self, department, coursenumber, quarter, year, instructor, review):
        key = self.client.key('HW4')
        rev = datastore.Entity(key)
        rev.update( {
            'department': department,
            'coursenumber' : coursenumber,
            'quarter' : quarter,
            'year' : year,
            'instructor' : instructor,
            'review' : review
            })
        self.client.put(rev)
        return True
