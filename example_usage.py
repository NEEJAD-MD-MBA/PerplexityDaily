"""Example usage of the Multi-Agent Coordination System."""

from coordinator import AgentCoordinator
from config import Config


def example_1_simple_usage():
    """Example 1: Simple usage with a basic goal."""
    print("\n" + "="*60)
    print("EXAMPLE 1: Simple Usage")
    print("="*60 + "\n")
    
    coordinator = AgentCoordinator()
    
    goal = "Build a simple blog platform with user authentication and markdown support"
    
    results = coordinator.build_and_deploy_web_app(goal)
    
    if results['success']:
        print("\n✓ Successfully generated application plan!")
        print(f"Number of steps completed: {len(results['steps'])}")
        
        # Save results
        coordinator.save_results_to_file(results, "blog_platform_plan.json")
    else:
        print("\n✗ Failed to generate application plan")
        print(f"Error: {results.get('error', 'Unknown error')}")


def example_2_with_context():
    """Example 2: Using agents with specific context."""
    print("\n" + "="*60)
    print("EXAMPLE 2: Direct Agent Usage with Context")
    print("="*60 + "\n")
    
    from agents import ChatGPTAgent, PerplexityAgent
    
    # Initialize agents
    chatgpt = ChatGPTAgent()
    perplexity = PerplexityAgent()
    
    # Use Perplexity for research
    research_context = {
        "role": "technology researcher",
        "task": "research the best Python web frameworks for building APIs",
        "constraints": "Focus on production-ready frameworks with good documentation"
    }
    
    research_query = "What are the best Python web frameworks for building REST APIs in 2024?"
    research_result = perplexity.send_message(research_query, research_context)
    
    print("Research Result:")
    print("-" * 60)
    print(research_result[:500] + "..." if len(research_result) > 500 else research_result)
    print()
    
    # Use ChatGPT for planning
    planning_context = {
        "role": "senior software architect",
        "task": "design a REST API architecture",
        "constraints": "Use modern best practices and scalable design"
    }
    
    planning_query = f"""Based on this research:
{research_result}

Design a REST API architecture for a task management application."""
    
    planning_result = chatgpt.send_message(planning_query, planning_context)
    
    print("\nPlanning Result:")
    print("-" * 60)
    print(planning_result[:500] + "..." if len(planning_result) > 500 else planning_result)


def example_3_conversation_history():
    """Example 3: Using conversation history for context."""
    print("\n" + "="*60)
    print("EXAMPLE 3: Using Conversation History")
    print("="*60 + "\n")
    
    from agents import ChatGPTAgent
    
    agent = ChatGPTAgent()
    
    # First message
    response1 = agent.send_message("What is Flask?")
    print("Q: What is Flask?")
    print(f"A: {response1[:200]}...\n")
    
    # Follow-up question using history
    response2 = agent.send_message("What are its main advantages?")
    print("Q: What are its main advantages?")
    print(f"A: {response2[:200]}...\n")
    
    # View conversation history
    print("Conversation History:")
    print("-" * 60)
    for i, msg in enumerate(agent.get_history(), 1):
        print(f"{i}. {msg['role']}: {msg['content'][:100]}...")
    
    # Clear history
    agent.clear_history()
    print("\nHistory cleared.")


def main():
    """Run all examples."""
    print("\n" + "="*60)
    print("MULTI-AGENT COORDINATION SYSTEM - EXAMPLES")
    print("="*60)
    
    # Validate configuration
    if not Config.validate():
        print("\nWarning: Some API keys are not configured.")
        print("Examples will not work properly without valid API keys.")
        print("Please configure your .env file with valid API keys.")
        return
    
    # Run examples
    try:
        # Example 1: Full coordination
        # Uncomment to run (takes several minutes)
        # example_1_simple_usage()
        
        # Example 2: Direct agent usage
        # Uncomment to run (requires API keys)
        # example_2_with_context()
        
        # Example 3: Conversation history
        # Uncomment to run (requires API keys)
        # example_3_conversation_history()
        
        print("\n" + "="*60)
        print("Examples are commented out by default.")
        print("Uncomment the examples you want to run in this file.")
        print("="*60 + "\n")
        
    except KeyboardInterrupt:
        print("\n\nExamples interrupted by user.")
    except Exception as e:
        print(f"\nError running examples: {str(e)}")


if __name__ == "__main__":
    main()
