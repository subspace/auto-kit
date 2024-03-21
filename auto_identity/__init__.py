"""
Auto Identity Module

This module provides functionalities for managing digital identities within the Auto SDK, 
including key generation, Auto ID management, and Auto ID registration and verification.
"""

from .key_management import generate_rsa_key_pair, generate_ed25519_key_pair, load_private_key, load_public_key

__version__ = '0.1.0'

__all__ = [
    "generate_rsa_key_pair", 
    "generate_ed25519_key_pair", 
    "load_private_key",
    "load_public_key",
]
