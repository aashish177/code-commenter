import ast
import openai
import os

class CodeParser(ast.NodeTransformer):
    """ AST-based parser to extract function details from Python code."""
    def __init__(self, ai_client):
        self.client = ai_client #OpenAI API Client

    def generate_comment(self, function_details):
        """
        Generate a Python docstring using OpenAI
        """

        prompt = f"Write a concise Python docstring for function:\n\n"
        prompt += f"def {function_details['name']}({', '.join(function_details['args'])}):\n"

        response = self.client.chat.completions.create(
            model = "gpt-3.5-turbo", # Change model if needed
            messages = [{"role": "user", "content": prompt}],
            max_tokens = 100
        )

        result = response.choices[0].message.content.strip()
        print(result) 
        return result

    def visit_FunctionDef(self, node):    
        """ 
        Extract details from each function in the code. 
        """
        function_details = {
            "name": node.name, # Function name
            "args": [arg.arg for arg in node.args.args], # Function arguments
            "lineno": node.lineno # Line number in the code
        }
        
        #Generate a docstring using OpenAI
        docstring = self.generate_comment(function_details)
        
        # Insert docstring only if it's missing
        if not ast.get_docstring(node):
            node.body.insert(0, ast.Expr(value=ast.Constant(value=docstring)))

        return node

def insert_docstrings_in_code(code:str):
    """
    Parses code, generates docstrings and inserts them
    """
    api_key = os.getenv("OPENAI_API_KEY")

    client = openai.Client(api_key=api_key)
    tree = ast.parse(code)

    parser = CodeParser(client)
    new_tree = parser.visit(tree)
    updatedCode = ast.unparse(new_tree) # Converts AST back to source code s

    return updatedCode

if __name__ == "__main__":
    sample_code = """
def add(a, b):
    return a + b
    
def subtract(a, b):
    return a - b
"""
    updatedCode = insert_docstrings_in_code(sample_code)
    print(updatedCode) 