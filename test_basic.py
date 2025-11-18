"""Basic tests for the multi-agent coordination system."""

import sys
import os

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_imports():
    """Test that all modules can be imported."""
    try:
        import config
        from agents import BaseAgent, ChatGPTAgent, PerplexityAgent
        from coordinator import AgentCoordinator
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {str(e)}")
        return False


def test_config():
    """Test configuration module."""
    try:
        from config import Config
        
        # Test that Config class exists and has required attributes
        assert hasattr(Config, 'OPENAI_API_KEY')
        assert hasattr(Config, 'PERPLEXITY_API_KEY')
        assert hasattr(Config, 'validate')
        
        # Test validate method
        Config.validate()
        
        print("✓ Config module works correctly")
        return True
    except Exception as e:
        print(f"✗ Config test failed: {str(e)}")
        return False


def test_agent_initialization():
    """Test agent initialization."""
    try:
        from agents import ChatGPTAgent, PerplexityAgent
        
        # Test with dummy keys (won't make actual API calls)
        chatgpt = ChatGPTAgent(api_key="dummy_key")
        perplexity = PerplexityAgent(api_key="dummy_key")
        
        assert chatgpt.name == "ChatGPT"
        assert perplexity.name == "Perplexity"
        assert len(chatgpt.conversation_history) == 0
        assert len(perplexity.conversation_history) == 0
        
        print("✓ Agent initialization works correctly")
        return True
    except Exception as e:
        print(f"✗ Agent initialization test failed: {str(e)}")
        return False


def test_conversation_history():
    """Test conversation history management."""
    try:
        from agents import ChatGPTAgent
        
        agent = ChatGPTAgent(api_key="dummy_key")
        
        # Test adding to history
        agent.add_to_history("user", "Hello")
        agent.add_to_history("assistant", "Hi there!")
        
        assert len(agent.get_history()) == 2
        assert agent.get_history()[0]["role"] == "user"
        assert agent.get_history()[1]["role"] == "assistant"
        
        # Test clearing history
        agent.clear_history()
        assert len(agent.get_history()) == 0
        
        print("✓ Conversation history management works correctly")
        return True
    except Exception as e:
        print(f"✗ Conversation history test failed: {str(e)}")
        return False


def test_coordinator_initialization():
    """Test coordinator initialization."""
    try:
        from coordinator import AgentCoordinator
        
        coordinator = AgentCoordinator()
        
        assert coordinator.chatgpt is not None
        assert coordinator.perplexity is not None
        assert len(coordinator.task_history) == 0
        
        print("✓ Coordinator initialization works correctly")
        return True
    except Exception as e:
        print(f"✗ Coordinator initialization test failed: {str(e)}")
        return False


def test_flask_app():
    """Test Flask app initialization."""
    try:
        from app import app
        
        assert app is not None
        assert app.config.get('SECRET_KEY') is not None
        
        print("✓ Flask app initializes correctly")
        return True
    except Exception as e:
        print(f"✗ Flask app test failed: {str(e)}")
        return False


def run_all_tests():
    """Run all basic tests."""
    print("\n" + "="*60)
    print("RUNNING BASIC TESTS")
    print("="*60 + "\n")
    
    tests = [
        ("Import Test", test_imports),
        ("Config Test", test_config),
        ("Agent Initialization Test", test_agent_initialization),
        ("Conversation History Test", test_conversation_history),
        ("Coordinator Initialization Test", test_coordinator_initialization),
        ("Flask App Test", test_flask_app),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 60)
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "="*60)
    print("TEST RESULTS")
    print("="*60 + "\n")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status}: {test_name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
