"""Multi-agent coordinator for web application development and deployment."""

import json
from typing import Dict, Any, List, Optional
from agents import ChatGPTAgent, PerplexityAgent


class AgentCoordinator:
    """Coordinates multiple AI agents to accomplish complex tasks."""
    
    def __init__(self):
        """Initialize the coordinator with available agents."""
        self.chatgpt = ChatGPTAgent()
        self.perplexity = PerplexityAgent()
        self.task_history: List[Dict[str, Any]] = []
    
    def build_and_deploy_web_app(self, user_goal: str) -> Dict[str, Any]:
        """
        Coordinate agents to build and deploy a web application.
        
        Args:
            user_goal: The user's ultimate goal for the web application
            
        Returns:
            Dictionary containing the results of the operation
        """
        print(f"\n{'='*60}")
        print(f"Starting web application build and deployment process")
        print(f"Goal: {user_goal}")
        print(f"{'='*60}\n")
        
        results = {
            "goal": user_goal,
            "steps": [],
            "success": False,
            "output": {}
        }
        
        try:
            # Step 1: Use Perplexity to research and gather requirements
            print("Step 1: Researching requirements and best practices...")
            research_context = {
                "role": "research specialist with access to current web development trends",
                "task": f"research the best technologies, frameworks, and deployment strategies for building a web application with this goal: {user_goal}",
                "constraints": "Focus on modern, production-ready solutions"
            }
            
            research_query = f"""Research and provide recommendations for building a web application with the following goal:
{user_goal}

Please provide:
1. Recommended technology stack (frontend, backend, database)
2. Best practices for this type of application
3. Deployment considerations and hosting options
4. Security considerations
5. Scalability recommendations"""
            
            research_results = self.perplexity.send_message(research_query, research_context)
            results["steps"].append({
                "step": "research",
                "agent": "Perplexity",
                "output": research_results
            })
            print(f"✓ Research completed\n")
            
            # Step 2: Use ChatGPT to plan the architecture
            print("Step 2: Planning application architecture...")
            architecture_context = {
                "role": "senior software architect",
                "task": f"design a detailed architecture for a web application based on the research",
                "constraints": "Create a clear, implementable plan"
            }
            
            architecture_query = f"""Based on this research:
{research_results}

Design a detailed architecture for a web application with this goal:
{user_goal}

Please provide:
1. System architecture diagram (described in text)
2. Component breakdown
3. API design
4. Data model
5. Implementation roadmap"""
            
            architecture_plan = self.chatgpt.send_message(architecture_query, architecture_context)
            results["steps"].append({
                "step": "architecture",
                "agent": "ChatGPT",
                "output": architecture_plan
            })
            print(f"✓ Architecture planned\n")
            
            # Step 3: Use ChatGPT to generate implementation details
            print("Step 3: Generating implementation details...")
            implementation_context = {
                "role": "expert full-stack developer",
                "task": "create detailed implementation instructions",
                "constraints": "Be specific and provide code examples where appropriate"
            }
            
            implementation_query = f"""Based on this architecture:
{architecture_plan}

Provide detailed implementation instructions including:
1. Project structure and file organization
2. Key code snippets for critical components
3. Configuration files needed
4. Environment setup instructions
5. Step-by-step build process"""
            
            implementation_details = self.chatgpt.send_message(implementation_query, implementation_context)
            results["steps"].append({
                "step": "implementation",
                "agent": "ChatGPT",
                "output": implementation_details
            })
            print(f"✓ Implementation details generated\n")
            
            # Step 4: Use Perplexity to verify deployment best practices
            print("Step 4: Verifying deployment strategy...")
            deployment_context = {
                "role": "DevOps engineer with current cloud deployment knowledge",
                "task": "verify and enhance the deployment strategy",
                "constraints": "Ensure production-ready deployment"
            }
            
            deployment_query = f"""Review this implementation plan:
{implementation_details}

Verify and provide:
1. Deployment checklist
2. CI/CD pipeline recommendations
3. Monitoring and logging setup
4. Backup and disaster recovery
5. Cost optimization tips"""
            
            deployment_strategy = self.perplexity.send_message(deployment_query, deployment_context)
            results["steps"].append({
                "step": "deployment",
                "agent": "Perplexity",
                "output": deployment_strategy
            })
            print(f"✓ Deployment strategy verified\n")
            
            # Step 5: Use ChatGPT to create final comprehensive guide
            print("Step 5: Creating comprehensive deployment guide...")
            final_context = {
                "role": "technical documentation specialist",
                "task": "synthesize all information into a clear, actionable guide",
                "constraints": "Make it easy to follow for developers of various skill levels"
            }
            
            final_query = f"""Synthesize all the previous steps into a comprehensive guide for building and deploying the web application.

Research: {research_results[:500]}...
Architecture: {architecture_plan[:500]}...
Implementation: {implementation_details[:500]}...
Deployment: {deployment_strategy[:500]}...

Create a final guide with:
1. Executive Summary
2. Quick Start Guide
3. Detailed Implementation Steps
4. Deployment Instructions
5. Maintenance and Scaling Guide"""
            
            final_guide = self.chatgpt.send_message(final_query, final_context)
            results["steps"].append({
                "step": "final_guide",
                "agent": "ChatGPT",
                "output": final_guide
            })
            print(f"✓ Comprehensive guide created\n")
            
            # Compile final output
            results["output"] = {
                "research": research_results,
                "architecture": architecture_plan,
                "implementation": implementation_details,
                "deployment": deployment_strategy,
                "final_guide": final_guide
            }
            results["success"] = True
            
            # Save to history
            self.task_history.append(results)
            
            print(f"\n{'='*60}")
            print(f"Process completed successfully!")
            print(f"{'='*60}\n")
            
        except Exception as e:
            error_msg = f"Error during coordination: {str(e)}"
            print(f"\n❌ {error_msg}\n")
            results["error"] = error_msg
        
        return results
    
    def get_task_history(self) -> List[Dict[str, Any]]:
        """Get the history of completed tasks."""
        return self.task_history
    
    def save_results_to_file(self, results: Dict[str, Any], filename: str):
        """
        Save results to a JSON file.
        
        Args:
            results: Results dictionary to save
            filename: Output filename
        """
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Results saved to {filename}")
        except Exception as e:
            print(f"Error saving results: {str(e)}")
