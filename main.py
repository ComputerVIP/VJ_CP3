"""
Math Problem Email Sender

SETUP INSTRUCTIONS FOR ANY COMPUTER:

1. Install Python (3.7 or newer) from python.org

2. Install SendGrid package in terminal/command prompt:
   pip install sendgrid

3. Set up your SendGrid API key in terminal:
   
   Windows:
   set SENDGRID_API_KEY=your_actual_api_key_here
   
   Mac/Linux:
   export SENDGRID_API_KEY="your_actual_api_key_here"

4. Run the program:
   python main.py

Note: You need a SendGrid account with a verified sender email address.
Go to SendGrid Settings > Sender Authentication to verify your email.
"""

import re
import os
import sys
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To

def create_math_problem():
    """Get math problem components from user input"""
    print("Let's create a math problem!")
    print("Available operations: + (addition), - (subtraction), * (multiplication), / (division)")
    
    # Get first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get operation
    while True:
        operation = input("Enter the operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Please enter a valid operation: +, -, *, or /")
    
    # Get second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            if operation == '/' and num2 == 0:
                print("Cannot divide by zero. Please enter a different number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Format numbers to remove unnecessary decimals
    if num1.is_integer():
        num1 = int(num1)
    if num2.is_integer():
        num2 = int(num2)
    
    problem = f"{num1} {operation} {num2}"
    return problem

def is_valid_email(email):
    """Basic email validation using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def send_math_problem_email(problem):
    """Send a math problem via email using SendGrid"""
    # Get recipient email from user
    print("\nWho should receive this math problem?")
    while True:
        to_email = input("Enter the recipient's email address: ").strip()
        if is_valid_email(to_email):
            break
        else:
            print("Please enter a valid email address.")
    
    # Check if SendGrid API key is available
    sendgrid_key = os.environ.get('SENDGRID_API_KEY')
    if not sendgrid_key:
        print("Error: SENDGRID_API_KEY environment variable is not set.")
        print("Please set your SendGrid API key to send emails.")
        return False
    
    # Get sender email from user
    print("\nNote: The sender email must be verified in your SendGrid account.")
    print("Common options:")
    print("- Use a verified email from your SendGrid Single Sender Verification")
    print("- Use an email from your verified domain")
    
    while True:
        from_email = input("Enter the sender email address (must be verified in SendGrid): ").strip()
        if is_valid_email(from_email):
            break
        else:
            print("Please enter a valid email address.")
    
    # Create email content
    subject = "Math Problem for You!"
    text_content = f"""Hello!

Here's a math problem for you to solve:

{problem} = ?

Please reply with your answer!

Best regards,
Your Math Problem Generator
"""
    
    # Set up SendGrid
    sg = SendGridAPIClient(sendgrid_key)
    
    message = Mail(
        from_email=Email(from_email),
        to_emails=To(to_email),
        subject=subject,
        plain_text_content=text_content
    )
    
    try:
        response = sg.send(message)
        print(f"Email sent successfully to {to_email}")
        print(f"Math problem sent: {problem}")
        print(f"Status code: {response.status_code}")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        if "403" in str(e) or "Forbidden" in str(e):
            print("\nThis is likely because:")
            print("1. The sender email is not verified in your SendGrid account")
            print("2. Your API key doesn't have 'Mail Send' permissions")
            print("\nTo fix this:")
            print("- Go to SendGrid Settings > Sender Authentication")
            print("- Verify the sender email or set up domain authentication")
            print("- Ensure your API key has 'Full Access' or 'Mail Send' permissions")
        return False

def main():
    """Main program function"""
    print("=== Math Problem Email Sender ===")
    print("This program lets you create a math problem and send it via email to anyone you choose.")
    print()
    
    # Get the math problem from user input
    problem = create_math_problem()
    
    print(f"\nYour math problem: {problem}")
    print("Preparing to send email...")
    
    # Send the email
    success = send_math_problem_email(problem)
    
    if success:
        print(f"\n✓ Math problem sent successfully!")
    else:
        print("\n✗ Failed to send math problem.")

if __name__ == "__main__":
    main()