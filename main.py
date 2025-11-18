"""Main application entry point for the multi-agent coordination system."""

import sys
import argparse
from coordinator import AgentCoordinator
from config import Config


def main():
    """Main function to run the coordination system."""
    parser = argparse.ArgumentParser(
        description="Multi-Agent Web Application Builder and Deployer"
    )
    parser.add_argument(
        "goal",
        nargs="?",
        help="The goal or description of the web application to build"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file to save results (JSON format)",
        default="results.json"
    )
    parser.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Run in interactive mode"
    )
    
    args = parser.parse_args()
    
    # Validate configuration
    print("\n" + "="*60)
    print("Multi-Agent Web Application Builder")
    print("="*60 + "\n")
    
    Config.validate()
    
    # Initialize coordinator
    coordinator = AgentCoordinator()
    
    # Get user goal
    goal = args.goal
    
    if args.interactive or not goal:
        print("\nInteractive Mode")
        print("-" * 60)
        print("Enter your web application goal (or 'quit' to exit):")
        goal = input("> ").strip()
        
        if goal.lower() in ['quit', 'exit', 'q']:
            print("Exiting...")
            return
    
    if not goal:
        print("Error: No goal provided. Use -h for help.")
        return 1
    
    # Process the request
    try:
        results = coordinator.build_and_deploy_web_app(goal)
        
        # Save results
        if args.output:
            coordinator.save_results_to_file(results, args.output)
        
        # Print summary
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"\nGoal: {goal}")
        print(f"Status: {'✓ Success' if results['success'] else '✗ Failed'}")
        print(f"Steps Completed: {len(results['steps'])}")
        
        if results['success']:
            print("\n" + "-"*60)
            print("FINAL GUIDE (Preview):")
            print("-"*60)
            final_guide = results['output'].get('final_guide', 'N/A')
            # Print first 1000 characters of the guide
            print(final_guide[:1000])
            if len(final_guide) > 1000:
                print("\n... (truncated, see full guide in output file)")
        
        print("\n" + "="*60 + "\n")
        
        return 0 if results['success'] else 1
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return 1
    except Exception as e:
        print(f"\nError: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
