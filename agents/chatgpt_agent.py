"""ChatGPT Agent implementation."""

import openai
from typing import Dict, Any
from .base_agent import BaseAgent
from config import Config


class ChatGPTAgent(BaseAgent):
    """Agent that uses OpenAI's ChatGPT API."""
    
    def __init__(self, api_key: str = None, model: str = None):
        """
        Initialize the ChatGPT agent.
        
        Args:
            api_key: OpenAI API key
            model: Model to use (default: gpt-4)
        """
        super().__init__("ChatGPT", api_key or Config.OPENAI_API_KEY)
        self.model = model or Config.DEFAULT_MODEL_CHATGPT
        self.client = openai.OpenAI(api_key=self.api_key)
    
    def send_message(self, message: str, context: Dict[str, Any] = None) -> str:
        """
        Send a message to ChatGPT and get a response.
        
        Args:
            message: The message to send
            context: Optional context information
            
        Returns:
            The agent's response
        """
        try:
            # Add user message to history
            self.add_to_history("user", message)
            
            # Prepare system message if context is provided
            messages = []
            if context:
                system_message = self._build_system_message(context)
                messages.append({"role": "system", "content": system_message})
            
            # Add conversation history
            messages.extend(self.conversation_history)
            
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            
            # Extract response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to history
            self.add_to_history("assistant", assistant_message)
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"Error communicating with ChatGPT: {str(e)}"
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
        
        return " ".join(parts) if parts else "You are a helpful AI assistant."
