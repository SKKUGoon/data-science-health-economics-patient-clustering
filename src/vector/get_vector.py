from qdrant_client import QdrantClient
import pandas as pd
import numpy as np
from typing import Tuple


def get_inpatient_vectors(client: QdrantClient, collection_name: str, year: int) -> Tuple[pd.DataFrame]:
    print("loading inpatient vectors for year", year)

    # Data is too big. Divide the data by year
    vectors = client.scroll(
        collection_name=collection_name,
        limit=80000,  # Adjust limit based on your data size
        with_vectors=True,  # Include embedding vectors,
        scroll_filter={
            "must": [
                {
                    "key": "year", 
                    "match": {"value": year}
                }
            ]
        }
    )[0]

    # Meta data & Vector data
    meta = []
    vector = []

    for i in vectors:
        meta.append(
            [
                i.id, 
                i.payload['patient_id'], 
                i.payload['visit_date'],
                i.payload['patient_type'], 
                i.payload['patient_sex'],  
                i.payload['patient_age'],  
                i.payload['patient_major_code'], 
                i.payload['patient_minor_code'],
                i.payload['patient_prescription']
            ]
        )
        vector.append(i.vector)

    return pd.DataFrame(meta), np.array(vector)


def get_outpatient_vectors(client: QdrantClient, collection_name: str, year: int) -> Tuple[pd.DataFrame]:
    print("loading outpatient vectors for year", year)

    # Data is too big. Divide the data by year
    vectors = client.scroll(
        collection_name=collection_name,
        limit=80000,  # Adjust limit based on your data size
        with_vectors=True,  # Include embedding vectors,
        scroll_filter={
            "must": [
                {
                    "key": "year", 
                    "match": {"value": year}
                }
            ]
        }
    )[0]

    # Meta data & Vector data
    meta = []
    vector = []

    for i in vectors:
        meta.append([
            i.id, i.payload['patient_id'], 
            i.payload['visit_date'], 
            i.payload['patient_type'], 
            i.payload['patient_sex'], 
            i.payload['patient_age'], 
            i.payload['patient_major_code'], 
            i.payload['patient_minor_code'], 
            i.payload['patient_prescription']
        ])
        vector.append(i.vector)

    return pd.DataFrame(meta), np.array(vector)


def get_inpatient_vectors_ing(client: QdrantClient, collection_name: str, year: int) -> Tuple[pd.DataFrame]:
    print("loading inpatient vectors for year", year)

    # Data is too big. Divide the data by year
    vectors = client.scroll(
        collection_name=collection_name,
        limit=80000,  # Adjust limit based on your data size
        with_vectors=True,  # Include embedding vectors,
        scroll_filter={
            "must": [
                {
                    "key": "year", 
                    "match": {"value": year}
                }
            ]
        }
    )[0]

    # Meta data & Vector data
    meta = []
    vector = []

    for i in vectors:
        meta.append(
            [
                i.id, 
                i.payload['patient_id'], 
                i.payload['visit_date'],
                i.payload['patient_type'], 
                i.payload['patient_sex'],  
                i.payload['patient_age'],  
                i.payload['patient_major_code'], 
                i.payload['patient_minor_code'],
                i.payload['patient_medicine_ingredients']
            ]
        )
        vector.append(i.vector)

    return pd.DataFrame(meta), np.array(vector)


def get_outpatient_vectors_ing(client: QdrantClient, collection_name: str, year: int) -> Tuple[pd.DataFrame]:
    print("loading outpatient vectors for year", year)

    # Data is too big. Divide the data by year
    vectors = client.scroll(
        collection_name=collection_name,
        limit=80000,  # Adjust limit based on your data size
        with_vectors=True,  # Include embedding vectors,
        scroll_filter={
            "must": [
                {
                    "key": "year", 
                    "match": {"value": year}
                }
            ]
        }
    )[0]

    # Meta data & Vector data
    meta = []
    vector = []

    for i in vectors:
        meta.append([
            i.id, i.payload['patient_id'], 
            i.payload['visit_date'], 
            i.payload['patient_type'], 
            i.payload['patient_sex'], 
            i.payload['patient_age'], 
            i.payload['patient_major_code'], 
            i.payload['patient_minor_code'], 
            i.payload['patient_medicine_ingredients']
        ])
        vector.append(i.vector)

    return pd.DataFrame(meta), np.array(vector)