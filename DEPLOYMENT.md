# Deployment Guide

This guide covers deploying the Multi-Agent Web Application Builder to various platforms.

## Quick Start (Local Development)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Run the application:
```bash
# Web interface
python app.py

# CLI
python main.py "Your application goal"
```

## Production Deployment

### Option 1: Heroku

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Deploy:
```bash
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your_key
heroku config:set PERPLEXITY_API_KEY=your_key
git push heroku main
```

### Option 2: AWS Elastic Beanstalk

1. Install EB CLI:
```bash
pip install awsebcli
```

2. Initialize and deploy:
```bash
eb init -p python-3.8 multi-agent-builder
eb create multi-agent-env
eb setenv OPENAI_API_KEY=your_key PERPLEXITY_API_KEY=your_key
eb deploy
```

### Option 3: Docker

1. Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

2. Build and run:
```bash
docker build -t multi-agent-builder .
docker run -p 5000:5000 \
  -e OPENAI_API_KEY=your_key \
  -e PERPLEXITY_API_KEY=your_key \
  multi-agent-builder
```

### Option 4: Digital Ocean App Platform

1. Create `app.yaml`:
```yaml
name: multi-agent-builder
services:
- name: web
  github:
    repo: your-username/PerplexityDaily
    branch: main
  run_command: gunicorn app:app
  envs:
  - key: OPENAI_API_KEY
    scope: RUN_TIME
    type: SECRET
  - key: PERPLEXITY_API_KEY
    scope: RUN_TIME
    type: SECRET
```

2. Deploy via Digital Ocean dashboard

### Option 5: Google Cloud Run

1. Create `Dockerfile` (see Docker section)

2. Deploy:
```bash
gcloud run deploy multi-agent-builder \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=your_key,PERPLEXITY_API_KEY=your_key
```

## Environment Variables

Required:
- `OPENAI_API_KEY`: Your OpenAI API key
- `PERPLEXITY_API_KEY`: Your Perplexity API key

Optional:
- `FLASK_ENV`: Set to `production` for production deployments
- `FLASK_DEBUG`: Set to `False` for production
- `PORT`: Port to run the server on (default: 5000)
- `HOST`: Host to bind to (default: 0.0.0.0)

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **HTTPS**: Always use HTTPS in production
3. **Rate Limiting**: Consider implementing rate limiting for the API endpoints
4. **Authentication**: Add authentication for production use
5. **Input Validation**: The system validates inputs, but review for your use case
6. **Monitoring**: Set up logging and monitoring for production

## Scaling

### Horizontal Scaling
- The application is stateless and can be scaled horizontally
- Use a load balancer to distribute traffic
- Each instance maintains its own conversation history

### Vertical Scaling
- Increase memory for longer conversation histories
- Increase CPU for faster processing

### Caching
- Consider caching API responses for common queries
- Implement Redis for shared caching across instances

## Monitoring

### Health Check
The application provides a health check endpoint:
```
GET /health
```

### Logging
- Application logs to stdout
- Configure log aggregation (e.g., CloudWatch, Stackdriver)

### Metrics to Monitor
- API response times
- Agent coordination success rate
- Memory usage
- Request count and error rates

## Cost Optimization

1. **API Usage**: Monitor and optimize API calls to OpenAI and Perplexity
2. **Caching**: Cache results for similar queries
3. **Rate Limiting**: Prevent abuse with rate limiting
4. **Resource Allocation**: Right-size your compute resources

## Backup and Recovery

1. **Results Storage**: Save important results to persistent storage
2. **Configuration Backup**: Keep environment variables backed up securely
3. **Disaster Recovery**: Document recovery procedures

## Support and Maintenance

1. **Updates**: Keep dependencies updated
2. **API Changes**: Monitor for API changes from OpenAI and Perplexity
3. **Security Patches**: Apply security patches promptly
4. **User Feedback**: Collect and act on user feedback

## Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Verify API keys are correctly set
   - Check API key permissions and quotas

2. **Connection Timeouts**:
   - Increase timeout values in agent implementations
   - Check network connectivity

3. **Memory Issues**:
   - Clear conversation history regularly
   - Increase memory allocation

4. **Rate Limiting**:
   - Implement exponential backoff
   - Use API rate limit headers

For more help, check the GitHub issues or open a new issue.
