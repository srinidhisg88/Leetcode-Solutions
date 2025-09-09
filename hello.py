"""
Hello World module for the LeetCode Solutions repository.
Provides a welcoming message and information about the repository.
"""

def hello():
    """
    Display a welcoming hello message for the LeetCode Solutions repository.
    
    Returns:
        str: A greeting message with repository information
    """
    message = """
    Hello! Welcome to the LeetCode Solutions Repository! 🎉
    
    This repository contains Python solutions for various LeetCode problems.
    The solutions are organized by problem categories:
    
    📁 Categories:
    • Arrays
    • Trees
    • Strings  
    • Dynamic Programming
    • Graph
    • Backtracking
    • Greedy
    • Linked Lists
    • Binary Search
    • Bit Manipulation
    • Stack
    • Two Pointers and Sliding Window
    
    Happy coding and problem solving! 🚀
    """
    return message

def greet_user(name=None):
    """
    Provide a personalized greeting.
    
    Args:
        name (str, optional): User's name for personalized greeting
        
    Returns:
        str: Personalized greeting message
    """
    if name:
        return f"Hello, {name}! Ready to solve some LeetCode problems? 💪"
    else:
        return "Hello there! Ready to solve some LeetCode problems? 💪"

if __name__ == "__main__":
    # Display the welcome message when run directly
    print(hello())
    print(greet_user())