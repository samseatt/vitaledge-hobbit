"""
File: datalake_service.py
Project: VitalEdge Hobbit
Description: Handles document retrieval from Datalake using its API. 

Author: Sam Seatt
Date: [Insert Date]

Features:

Usage:
    Import this module and call `` 
    to retrieve ?.

Notes:
- .
"""

import httpx
from config import Config

class DatalakeService:
    """
    Handles Datalake API interactions.
    """

    async def get_all_subjects(self) -> list:
        """
        Fetch all subjects from the Datalake API.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{Config.DATALAKE_API_URL}/subjects")
            response.raise_for_status()
            return response.json()

    async def get_subject_studies(self, subject_id: int) -> list:
        """
        Fetch all studies for a specific subject from the Datalake API.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{Config.DATALAKE_API_URL}/subjects/{subject_id}/studies"
            )
            response.raise_for_status()
            return response.json()
