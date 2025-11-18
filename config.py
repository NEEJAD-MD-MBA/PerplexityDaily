"""Configuration management for the multi-agent coordination system."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Application configuration."""
    
    # API Keys
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY', '')
    
    # Flask Settings
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # Agent Settings
    DEFAULT_MODEL_CHATGPT = 'gpt-4'
    DEFAULT_MODEL_PERPLEXITY = 'llama-3.1-sonar-small-128k-online'
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        errors = []
        
        if not cls.OPENAI_API_KEY:
            errors.append("OPENAI_API_KEY is not set")
        if not cls.PERPLEXITY_API_KEY:
            errors.append("PERPLEXITY_API_KEY is not set")
        
        if errors:
            print("Warning: Missing configuration:")
            for error in errors:
                print(f"  - {error}")
            print("Some features may not work properly.")
        
        return len(errors) == 0
