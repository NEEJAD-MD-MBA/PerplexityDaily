"""Perplexity Agent implementation."""

import requests
from typing import Dict, Any
from .base_agent import BaseAgent
from config import Config


class PerplexityAgent(BaseAgent):
    """Agent that uses Perplexity AI API."""
    
    def __init__(self, api_key: str = None, model: str = None):
        """
        Initialize the Perplexity agent.
        
        Args:
            api_key: Perplexity API key
            model: Model to use (default: llama-3.1-sonar-small-128k-online)
        """
        super().__init__("Perplexity", api_key or Config.PERPLEXITY_API_KEY)
        self.model = model or Config.DEFAULT_MODEL_PERPLEXITY
        self.api_url = "https://api.perplexity.ai/chat/completions"
    
    def send_message(self, message: str, context: Dict[str, Any] = None) -> str:
        """
        Send a message to Perplexity and get a response.
        
        Args:
            message: The message to send
            context: Optional context information
            
        Returns:
            The agent's response
        """
        try:
            # Add user message to history
            self.add_to_history("user", message)
            
            # Prepare messages
            messages = []
            if context:
                system_message = self._build_system_message(context)
                messages.append({"role": "system", "content": system_message})
            
            # Add conversation history
            messages.extend(self.conversation_history)
            
            # Prepare request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 2000
            }
            
            # Call Perplexity API
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            
            # Extract response
            result = response.json()
            assistant_message = result["choices"][0]["message"]["content"]
            
            # Add assistant response to history
            self.add_to_history("assistant", assistant_message)
            
            return assistant_message
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Error communicating with Perplexity: {str(e)}"
            print(error_msg)
            return error_msg
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            print(error_msg)
            return error_msg
    
    def _build_system_message(self, context: Dict[str, Any]) -> str:
        """
        Build a system message from context.
        
        Args:
            context: Context information
            
        Returns:
            System message string
        """
        parts = []
        
        if "role" in context:
            parts.append(f"You are a {context['role']}.")
        
        if "task" in context:
            parts.append(f"Your task is to: {context['task']}")
        
        if "constraints" in context:
            parts.append(f"Constraints: {context['constraints']}")
        
        return " ".join(parts) if parts else "You are a helpful AI assistant with access to real-time information."
