# Contributing to PerplexityDaily

Thank you for your interest in contributing to PerplexityDaily! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain a professional environment

## How to Contribute

### Reporting Bugs

If you find a bug:

1. Check if it's already reported in [GitHub Issues](https://github.com/NEEJAD-MD-MBA/PerplexityDaily/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages and logs

### Suggesting Features

For feature requests:

1. Check existing issues and discussions
2. Create a new issue with:
   - Clear use case description
   - Expected behavior
   - Why this feature would be useful
   - Possible implementation approach

### Pull Requests

#### Before You Start

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Add your API keys
   ```

3. Run tests to ensure everything works:
   ```bash
   python test_basic.py
   ```

#### Making Changes

1. Make your changes in your feature branch
2. Follow the existing code style:
   - Use meaningful variable names
   - Add docstrings to functions and classes
   - Keep functions focused and small
   - Add comments for complex logic

3. Test your changes:
   ```bash
   python test_basic.py
   python -m py_compile your_file.py
   ```

4. Update documentation:
   - Update README.md if needed
   - Add docstrings to new functions
   - Update CHANGELOG.md (if exists)

#### Submitting Pull Request

1. Commit your changes:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

2. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Create a Pull Request:
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template with:
     - What changes you made
     - Why you made them
     - How to test them
     - Any breaking changes

4. Wait for review:
   - Respond to feedback
   - Make requested changes
   - Keep the PR focused on one feature/fix

## Code Style Guidelines

### Python Code

- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use type hints where appropriate

Example:
```python
def send_message(self, message: str, context: Dict[str, Any] = None) -> str:
    """
    Send a message to the agent.
    
    Args:
        message: The message to send
        context: Optional context information
        
    Returns:
        The agent's response
    """
    pass
```

### Documentation

- Use clear, concise language
- Provide examples where helpful
- Keep README.md up to date
- Document breaking changes

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Provide detailed description if needed
- Reference issues with #issue_number

Good examples:
```
Add support for custom models in agents

Update README with deployment instructions

Fix TypeError in coordinator.build_and_deploy_web_app
Closes #42
```

## Testing

### Running Tests

```bash
python test_basic.py
```

### Adding Tests

When adding new features:

1. Add corresponding tests to `test_basic.py`
2. Ensure tests pass locally
3. Tests should be clear and maintainable

## Project Structure

```
PerplexityDaily/
├── agents/              # Agent implementations
│   ├── base_agent.py   # Base class for all agents
│   ├── chatgpt_agent.py
│   └── perplexity_agent.py
├── templates/          # HTML templates
├── app.py             # Flask web application
├── main.py            # CLI application
├── coordinator.py     # Agent coordination logic
├── config.py          # Configuration management
└── test_basic.py      # Tests
```

## Areas for Contribution

We welcome contributions in these areas:

### High Priority
- Additional agent implementations (Claude, Gemini, etc.)
- Enhanced error handling and retry logic
- Rate limiting and quota management
- Caching for API responses
- More comprehensive tests

### Medium Priority
- UI/UX improvements for web interface
- Additional deployment platform support
- Performance optimizations
- Better logging and monitoring

### Nice to Have
- Docker compose setup
- Integration with CI/CD tools
- CLI autocomplete
- Configuration wizard
- Plugin system for custom agents

## Getting Help

If you need help:

1. Check existing documentation
2. Search closed issues
3. Ask in GitHub Discussions
4. Create a new issue with the "question" label

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (if created)
- Mentioned in release notes
- Credited in the project

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open an issue with the "question" label if you have any questions about contributing!

Thank you for making PerplexityDaily better! 🚀
