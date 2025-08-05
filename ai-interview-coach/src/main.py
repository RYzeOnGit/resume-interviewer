#!/usr/bin/env python3
"""
AI Interview Coach - Main Application

This module serves as the entry point for the AI Interview Coach application.
It sets up the LangGraph workflow and provides an interactive interview experience.
"""

import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langchain_openai import ChatOpenAI

# Import nodes
from nodes.ask_role import ask_role
from nodes.generate_question import generate_question
from nodes.get_answer import get_answer
from nodes.evaluate_answer import evaluate_answer
from nodes.feedback import provide_feedback

# Load environment variables
load_dotenv()

# Define the state structure
class InterviewState(TypedDict):
    """State for the interview workflow."""
    role: str
    question: str
    answer: str
    evaluation: str
    feedback: str
    messages: list

def create_interview_graph():
    """Create the LangGraph workflow for the interview process."""
    
    # Initialize the graph
    workflow = StateGraph(InterviewState)
    
    # Add nodes
    workflow.add_node("ask_role", ask_role)
    workflow.add_node("generate_question", generate_question)
    workflow.add_node("get_answer", get_answer)
    workflow.add_node("evaluate_answer", evaluate_answer)
    workflow.add_node("feedback", provide_feedback)
    
    # Define the flow
    workflow.set_entry_point("ask_role")
    workflow.add_edge("ask_role", "generate_question")
    workflow.add_edge("generate_question", "get_answer")
    workflow.add_edge("get_answer", "evaluate_answer")
    workflow.add_edge("evaluate_answer", "feedback")
    workflow.add_edge("feedback", END)
    
    return workflow.compile()

def main():
    """Main function to run the AI Interview Coach."""
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("Please set your OpenAI API key in the .env file.")
        return
    
    print("🤖 Welcome to AI Interview Coach!")
    print("I'll help you prepare for your interviews with personalized coaching.")
    print("-" * 50)
    
    # Create and run the workflow
    app = create_interview_graph()
    
    # Initialize the state
    initial_state = {
        "role": "",
        "question": "",
        "answer": "",
        "evaluation": "",
        "feedback": "",
        "messages": []
    }
    
    # Run the interview workflow
    try:
        result = app.invoke(initial_state)
        print("\n✅ Interview session completed!")
        print("Thank you for using AI Interview Coach!")
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        print("Please check your configuration and try again.")

if __name__ == "__main__":
    main() 