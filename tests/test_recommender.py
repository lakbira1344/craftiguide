import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.recommender import recommend_service

def test_ecommerce():
    result = recommend_service("Je veux vendre des produits en ligne")
    assert result["service"] == "Site e-commerce"
    assert result["score"] > 0

def test_vitrine():
    result = recommend_service("Je veux présenter mon entreprise")
    assert result["service"] == "Site vitrine"

def test_vide():
    result = recommend_service("")
    assert result["ambiguous"] is True
    assert result["service"] is None

def test_trop_court():
    result = recommend_service("Bonjour")
    assert result["ambiguous"] is True

def test_aucun_mot():
    result = recommend_service("Je ne sais pas quoi faire")
    assert result["score"] == 0