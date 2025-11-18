# PerplexityDaily - Multi-Agent Web Application Builder

A sophisticated coordination system that leverages multiple AI agents (Perplexity and ChatGPT) to help users build and deploy web applications efficiently.

## Overview

This system coordinates two powerful AI agents:
- **Perplexity Agent**: Researches current best practices, technologies, and deployment strategies with access to real-time information
- **ChatGPT Agent**: Plans architecture, generates implementation details, and creates comprehensive guides

Together, they provide end-to-end guidance for building and deploying web applications.

## Features

- 🤖 **Multi-Agent Coordination**: Intelligently coordinates Perplexity and ChatGPT agents
- 🔍 **Research-Driven**: Uses Perplexity to gather current best practices and technologies
- 🏗️ **Architecture Planning**: Uses ChatGPT for detailed system design
- 📝 **Implementation Guides**: Generates comprehensive, actionable implementation plans
- 🚀 **Deployment Strategy**: Provides production-ready deployment recommendations
- 🌐 **Web Interface**: User-friendly web UI for easy interaction
- 💻 **CLI Support**: Command-line interface for automation and scripting

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- API keys for:
  - OpenAI (ChatGPT)
  - Perplexity AI

### Setup

1. Clone the repository:
```bash
git clone https://github.com/NEEJAD-MD-MBA/PerplexityDaily.git
cd PerplexityDaily
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

Required environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key
- `PERPLEXITY_API_KEY`: Your Perplexity API key

Optional environment variables:
- `FLASK_ENV`: Environment (development/production)
- `FLASK_DEBUG`: Enable debug mode (True/False)
- `PORT`: Web server port (default: 5000)
- `HOST`: Web server host (default: 0.0.0.0)

## Usage

### Web Interface

Start the web server:
```bash
python app.py
```

Then open your browser to `http://localhost:5000`

Enter your web application goal and let the agents coordinate to create a comprehensive plan!

### Command Line Interface

Run with a specific goal:
```bash
python main.py "Build a task management app with real-time collaboration"
```

Run in interactive mode:
```bash
python main.py -i
```

Save results to a specific file:
```bash
python main.py "Build an e-commerce platform" -o ecommerce_plan.json
```

### API Endpoints

- `GET /`: Web interface
- `POST /api/build`: Build application plan (accepts JSON with `goal` field)
- `GET /api/history`: Get task history
- `GET /api/download/<filename>`: Download results file
- `GET /health`: Health check endpoint

## How It Works

1. **Research Phase** (Perplexity Agent):
   - Researches current technologies and best practices
   - Identifies optimal tech stack
   - Gathers security and scalability recommendations

2. **Architecture Phase** (ChatGPT Agent):
   - Designs system architecture
   - Creates component breakdown
   - Plans API design and data models

3. **Implementation Phase** (ChatGPT Agent):
   - Generates detailed implementation instructions
   - Provides code examples
   - Creates project structure

4. **Deployment Phase** (Perplexity Agent):
   - Verifies deployment strategy
   - Recommends CI/CD pipelines
   - Provides monitoring and cost optimization tips

5. **Final Guide** (ChatGPT Agent):
   - Synthesizes all information
   - Creates comprehensive, actionable guide
   - Includes quick start and detailed steps

## Project Structure

```
PerplexityDaily/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py       # Base agent class
│   ├── chatgpt_agent.py    # ChatGPT implementation
│   └── perplexity_agent.py # Perplexity implementation
├── templates/
│   └── index.html          # Web interface
├── app.py                  # Flask web application
├── main.py                 # CLI application
├── coordinator.py          # Agent coordination logic
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment file
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Example Use Cases

- **Startup MVP**: "Build a social media platform for pet owners"
- **Enterprise App**: "Create a CRM system with analytics dashboard"
- **E-commerce**: "Build an online marketplace with payment integration"
- **SaaS Product**: "Develop a project management tool with team collaboration"
- **Mobile App Backend**: "Create a REST API for a fitness tracking mobile app"

## Output Format

Results are saved in JSON format containing:
- Goal description
- Research findings
- Architecture plan
- Implementation details
- Deployment strategy
- Final comprehensive guide
- Step-by-step process log

## Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest
```

### Linting

```bash
# Install linting tools
pip install pylint black

# Run linter
pylint *.py agents/

# Format code
black *.py agents/
```

## Security Considerations

- Never commit API keys to version control
- Use environment variables for sensitive data
- Review generated deployment strategies for security best practices
- Follow the security recommendations provided by the agents

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Acknowledgments

- OpenAI for ChatGPT API
- Perplexity AI for their research-capable API
- The open-source community for the libraries used in this project