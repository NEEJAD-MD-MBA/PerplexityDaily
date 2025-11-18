# System Architecture

This document describes the architecture of the Multi-Agent Web Application Builder.

## Overview

The system is designed as a modular, extensible platform that coordinates multiple AI agents to accomplish complex tasks. It follows a coordinator pattern where a central coordinator orchestrates the activities of specialized agents.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         User Interface                       │
│  ┌─────────────────────┐      ┌─────────────────────────┐  │
│  │   Web Interface     │      │   CLI Interface         │  │
│  │   (Flask/HTML)      │      │   (argparse)            │  │
│  └──────────┬──────────┘      └──────────┬──────────────┘  │
└─────────────┼─────────────────────────────┼─────────────────┘
              │                             │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │    Agent Coordinator        │
              │  (coordinator.py)           │
              └──────────────┬──────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐         ┌────▼────┐       ┌─────▼─────┐
    │Perplexity│        │ ChatGPT │       │  Future   │
    │  Agent   │        │  Agent  │       │  Agents   │
    └────┬─────┘        └────┬────┘       └───────────┘
         │                   │
         │                   │
    ┌────▼─────┐        ┌────▼─────┐
    │Perplexity│        │  OpenAI  │
    │   API    │        │   API    │
    └──────────┘        └──────────┘
```

## Core Components

### 1. Configuration Layer (`config.py`)

**Purpose**: Centralized configuration management

**Responsibilities**:
- Load environment variables
- Validate configuration
- Provide configuration to all components
- Default values for optional settings

**Key Features**:
- Environment-based configuration
- Validation on startup
- Type-safe configuration access

### 2. Agent Layer (`agents/`)

#### Base Agent (`base_agent.py`)

**Purpose**: Abstract base class for all agents

**Responsibilities**:
- Define agent interface
- Manage conversation history
- Provide common agent functionality

**Key Methods**:
- `send_message()`: Send message and get response
- `add_to_history()`: Track conversation
- `clear_history()`: Reset conversation
- `get_history()`: Retrieve conversation

#### ChatGPT Agent (`chatgpt_agent.py`)

**Purpose**: Interface with OpenAI's ChatGPT API

**Responsibilities**:
- Make API calls to OpenAI
- Handle responses and errors
- Manage context and system messages
- Format requests appropriately

**Specialization**: Architecture planning, code generation, documentation

#### Perplexity Agent (`perplexity_agent.py`)

**Purpose**: Interface with Perplexity AI API

**Responsibilities**:
- Make API calls to Perplexity
- Handle responses and errors
- Leverage real-time information access
- Format requests appropriately

**Specialization**: Research, current best practices, deployment strategies

### 3. Coordination Layer (`coordinator.py`)

**Purpose**: Orchestrate multiple agents to accomplish complex tasks

**Responsibilities**:
- Coordinate agent activities
- Manage task workflow
- Aggregate results
- Handle errors gracefully
- Track task history

**Key Workflow**:
1. Research (Perplexity) → Gather current best practices
2. Architecture (ChatGPT) → Design system
3. Implementation (ChatGPT) → Generate details
4. Deployment (Perplexity) → Verify strategy
5. Final Guide (ChatGPT) → Synthesize all information

### 4. Application Layer

#### Web Interface (`app.py`)

**Purpose**: Provide web-based user interface

**Responsibilities**:
- Serve web pages
- Handle API requests
- Manage sessions
- Return results

**Endpoints**:
- `GET /`: Main interface
- `POST /api/build`: Build application plan
- `GET /api/history`: Get task history
- `GET /api/download/<filename>`: Download results
- `GET /health`: Health check

#### CLI Interface (`main.py`)

**Purpose**: Provide command-line interface

**Responsibilities**:
- Parse command-line arguments
- Execute coordination workflow
- Display results
- Save output files

**Features**:
- Direct goal specification
- Interactive mode
- Custom output file
- Progress display

### 5. Presentation Layer (`templates/`)

**Purpose**: User interface for web application

**Responsibilities**:
- Render user interface
- Handle user input
- Display results
- Provide feedback

## Data Flow

### 1. Web Application Flow

```
User Input → Flask Route → Coordinator
                              ↓
                    Agent 1 (Research)
                              ↓
                    Agent 2 (Architecture)
                              ↓
                    Agent 3 (Implementation)
                              ↓
                    Agent 4 (Deployment)
                              ↓
                    Agent 5 (Final Guide)
                              ↓
                         JSON Result
                              ↓
                     Web Interface Display
```

### 2. CLI Flow

```
Command Args → Argument Parser → Coordinator
                                     ↓
                             Agent Workflow
                                     ↓
                              JSON Result
                                     ↓
                            Console Output
                                     ↓
                              File Save
```

## Design Patterns

### 1. Abstract Factory Pattern

The `BaseAgent` class serves as an abstract factory for creating different types of agents.

### 2. Coordinator Pattern

The `AgentCoordinator` orchestrates multiple agents to accomplish complex tasks.

### 3. Strategy Pattern

Different agents represent different strategies for accomplishing tasks (research vs. planning).

### 4. Template Method Pattern

The coordination workflow follows a template method pattern with defined steps.

## Extensibility

### Adding New Agents

1. Create a new agent class inheriting from `BaseAgent`
2. Implement the `send_message()` method
3. Add agent initialization in coordinator
4. Update documentation

Example:
```python
class ClaudeAgent(BaseAgent):
    def __init__(self, api_key: str = None):
        super().__init__("Claude", api_key)
        
    def send_message(self, message: str, context: Dict[str, Any] = None) -> str:
        # Implementation
        pass
```

### Adding New Workflows

1. Define a new method in `AgentCoordinator`
2. Specify agent coordination steps
3. Return structured results
4. Update API endpoints if needed

## Error Handling

### Strategy

1. **Graceful Degradation**: Continue with partial results if possible
2. **User Feedback**: Provide clear error messages
3. **Logging**: Log errors for debugging
4. **Retry Logic**: Can be added for transient failures

### Error Types

- Configuration errors (missing API keys)
- Network errors (API unavailable)
- API errors (rate limits, invalid requests)
- Processing errors (unexpected responses)

## Security Considerations

### 1. API Key Management

- Store in environment variables
- Never commit to version control
- Validate on startup
- Use secrets management in production

### 2. Input Validation

- Sanitize user input
- Validate request parameters
- Check file paths
- Prevent injection attacks

### 3. Output Sanitization

- Escape HTML in web interface
- Validate JSON responses
- Check file contents before saving

### 4. Rate Limiting

- Consider implementing rate limits
- Track API usage
- Handle quota exceeded gracefully

## Performance Considerations

### 1. API Calls

- Sequential calls for dependent steps
- Could be parallelized for independent research
- Caching can reduce redundant calls

### 2. Memory

- Conversation history grows over time
- Consider clearing or limiting history
- Store large results in files

### 3. Scalability

- Stateless design allows horizontal scaling
- Each instance is independent
- Use external storage for shared state

## Testing Strategy

### Unit Tests

- Test individual agent functionality
- Mock API responses
- Test configuration validation
- Test conversation history management

### Integration Tests

- Test coordinator workflow
- Test API endpoints
- Test CLI commands
- Test file operations

### End-to-End Tests

- Test complete user workflows
- Test error scenarios
- Test with real API keys (optional)

## Deployment Architecture

### Development

```
Local Machine
├── Python Environment
├── Environment Variables
└── Development Server
```

### Production (Example)

```
Load Balancer
├── App Instance 1
├── App Instance 2
└── App Instance 3
     ↓
External APIs
├── OpenAI
└── Perplexity
     ↓
File Storage
└── Results JSON files
```

## Future Enhancements

### Planned Features

1. **Caching Layer**: Redis for response caching
2. **Queue System**: Celery for async processing
3. **Database**: Store task history and results
4. **Authentication**: User accounts and API keys
5. **Rate Limiting**: Protect against abuse
6. **Monitoring**: Metrics and alerting
7. **Multi-tenancy**: Support multiple organizations

### Agent Improvements

1. **More Agents**: Claude, Gemini, Llama
2. **Specialized Agents**: Security, testing, documentation
3. **Agent Selection**: Automatic agent selection based on task
4. **Agent Learning**: Track which agents work best for which tasks

### Coordination Improvements

1. **Dynamic Workflows**: Adjust workflow based on requirements
2. **Parallel Execution**: Run independent steps in parallel
3. **Feedback Loops**: Allow agents to review each other's work
4. **Human in the Loop**: Allow user intervention during workflow

## Maintenance

### Code Organization

- Keep agents independent
- Maintain clear interfaces
- Document all public methods
- Use type hints consistently

### Documentation

- Keep architecture docs updated
- Document breaking changes
- Maintain API documentation
- Update examples regularly

### Monitoring

- Track API usage and costs
- Monitor error rates
- Log performance metrics
- Alert on failures

---

For more information, see:
- [README.md](README.md) - General documentation
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
