# Quick Start Guide

Get up and running with the Multi-Agent Web Application Builder in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- Perplexity API key ([Get one here](https://www.perplexity.ai/settings/api))

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/NEEJAD-MD-MBA/PerplexityDaily.git
cd PerplexityDaily
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Copy the example environment file:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```
OPENAI_API_KEY=sk-your-openai-key-here
PERPLEXITY_API_KEY=pplx-your-perplexity-key-here
```

## Usage

### Option 1: Web Interface (Recommended)

Start the web server:

```bash
python app.py
```

Open your browser to: `http://localhost:5000`

Enter your web application idea and click "Build Application Plan"!

### Option 2: Command Line

Run with a specific goal:

```bash
python main.py "Build a task management app with real-time collaboration"
```

The results will be saved to `results.json` by default.

### Option 3: Interactive Mode

```bash
python main.py -i
```

Enter your goal when prompted.

## Example Goals

Try these example goals to get started:

1. **Simple Blog**:
   ```
   Build a simple blog platform with user authentication and markdown support
   ```

2. **Task Manager**:
   ```
   Create a task management app with real-time collaboration features
   ```

3. **E-commerce**:
   ```
   Build an online store with product catalog, shopping cart, and payment integration
   ```

4. **Social Network**:
   ```
   Develop a social media platform for sharing photos with likes and comments
   ```

5. **API Service**:
   ```
   Create a REST API for a fitness tracking mobile app with user profiles and workout logs
   ```

## What Happens Next?

The system will:

1. **Research** (Perplexity Agent): Gather current best practices and technologies
2. **Architect** (ChatGPT Agent): Design the system architecture
3. **Implement** (ChatGPT Agent): Generate implementation details
4. **Deploy** (Perplexity Agent): Verify deployment strategy
5. **Guide** (ChatGPT Agent): Create a comprehensive implementation guide

The entire process takes 3-5 minutes depending on the complexity of your goal.

## Output

Results are saved in JSON format with:

- Research findings
- Architecture plan
- Implementation details
- Deployment strategy
- Comprehensive final guide

## Tips for Best Results

1. **Be Specific**: Include details about features, users, and requirements
2. **Mention Constraints**: If you have technology preferences, mention them
3. **Specify Scale**: Mention if you need to support many users or high traffic
4. **Include Integrations**: If you need specific third-party services, list them

### Good Goal Examples:

✅ "Build a real-time chat application using WebSockets with user authentication, message history, and mobile-responsive design"

✅ "Create a blog platform with markdown editor, image uploads, SEO optimization, and RSS feed"

### Less Effective Goals:

❌ "Make a website" (too vague)
❌ "Build something cool" (no direction)

## Troubleshooting

### API Key Issues

If you see "OPENAI_API_KEY is not set" or similar:

1. Check that `.env` file exists in the project root
2. Verify your API keys are correct
3. Make sure there are no extra spaces or quotes around the keys

### Module Not Found

If you see "No module named...":

```bash
pip install -r requirements.txt
```

### Port Already in Use

If port 5000 is in use, change it in `.env`:

```
PORT=8080
```

Then restart the app.

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
- Review [example_usage.py](example_usage.py) for programmatic usage

## Getting Help

- Check the [GitHub Issues](https://github.com/NEEJAD-MD-MBA/PerplexityDaily/issues)
- Read the documentation in README.md
- Open a new issue if you encounter problems

## License

MIT License - See LICENSE file for details

---

**Ready to build?** Start with the web interface or CLI and let the agents guide you! 🚀
