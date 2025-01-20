"""
File: datalake_service.py
Project: VitalEdge LangChain
Description: Handles document retrieval from Datalake using its API. 

Author: Sam Seatt
Date: [Insert Date]

Features:

Usage:
    Import this module and call `/studies/variants_by_study/(id: int)` 
    to retrieve relevant documents.

Notes:
- .
"""

import httpx
from config import Config

class DatalakeService:
    """
    Handles datalake search requests to the VitalEdge Datalake microservice.
    """

    async def search_variants(self, study_id: int) -> list:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{Config.DATALAKE_API_URL}/studies/variants_by_study/103"
            )
            print(f"DatalakeService.search_variants returned response: {response.json()}")
            response.raise_for_status()
            return response.json().get("results", [])
