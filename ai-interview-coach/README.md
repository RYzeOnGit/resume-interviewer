# AI Interview Coach

An intelligent interview preparation system built with LangGraph and LangChain that provides personalized interview coaching through role-based questioning, answer evaluation, and constructive feedback.

## Features

- **Role-based Interviewing**: Tailored questions based on specific job roles
- **Intelligent Question Generation**: Dynamic question creation using AI
- **Answer Evaluation**: Comprehensive assessment of responses
- **Constructive Feedback**: Detailed feedback to improve interview performance
- **Conversational Flow**: Natural interview-like experience

## Project Structure

```
ai-interview-coach/
├── .env                    # Environment variables
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── requirements.txt        # Python dependencies
└── src/
    ├── main.py            # Main application entry point
    ├── nodes/             # LangGraph nodes
    │   ├── ask_role.py    # Role selection node
    │   ├── generate_question.py  # Question generation node
    │   ├── get_answer.py  # Answer collection node
    │   ├── evaluate_answer.py    # Answer evaluation node
    │   └── feedback.py    # Feedback generation node
    └── utils/             # Utility functions
        └── __init__.py    # Package initialization
```

## Setup

1. **Create Conda Environment**:
   ```bash
   conda create -n interview-coach python=3.11 -y
   conda activate interview-coach
   ```

2. **Install Dependencies**:
   ```bash
   pip install langgraph langchain openai python-dotenv
   ```

3. **Environment Configuration**:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to `.env`

4. **Run the Application**:
   ```bash
   python src/main.py
   ```

## Usage

The AI Interview Coach provides an interactive interview experience:

1. **Role Selection**: Choose your target job role
2. **Question Generation**: AI generates relevant questions
3. **Answer Input**: Provide your responses
4. **Evaluation**: Get detailed assessment of your answers
5. **Feedback**: Receive constructive improvement suggestions

## Dependencies

- `langgraph`: For building conversational AI workflows
- `langchain`: For LLM integration and chain management
- `openai`: OpenAI API client
- `python-dotenv`: Environment variable management

## License

MIT License 