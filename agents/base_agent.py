"""Base agent class for all AI agents."""

from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseAgent(ABC):
    """Abstract base class for AI agents."""
    
    def __init__(self, name: str, api_key: str):
        """
        Initialize the base agent.
        
        Args:
            name: Name of the agent
            api_key: API key for the agent's service
        """
        self.name = name
        self.api_key = api_key
        self.conversation_history: List[Dict[str, str]] = []
    
    @abstractmethod
    def send_message(self, message: str, context: Dict[str, Any] = None) -> str:
        """
        Send a message to the agent and get a response.
        
        Args:
            message: The message to send
            context: Optional context information
            
        Returns:
            The agent's response
        """
        pass
    
    def add_to_history(self, role: str, content: str):
        """
        Add a message to the conversation history.
        
        Args:
            role: Role of the message sender (user/assistant)
            content: Content of the message
        """
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get the conversation history."""
        return self.conversation_history
