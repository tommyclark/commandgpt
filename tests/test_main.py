import unittest
from unittest.mock import patch
from langchain.llms.fake import FakeListLLM
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from commandgpt import main, parse_arguments

class TestMain(unittest.TestCase):

    def setUp(self):
        responses = ["Action: Python REPL\nAction Input: How to list all files in a directory?", 
                     "Final Answer: <generated_bash_command>"]        
        llm = FakeListLLM(responses=responses)
        self.agent = initialize_agent(load_tools(["python_repl"]), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    @patch('commandgpt.getPromptedLLMChain')
    @patch('subprocess.call')
    def test_question_only(self, mock_call, mock_llm):
        mock_llm.return_value = self.agent
        question = "How to list all files in a directory?"
        args = ['-q', question]
        parsed_args = parse_arguments(args)
        
        with patch('builtins.print') as mock_print:
            main(parsed_args)
            
            mock_print.assert_called_with("<generated_bash_command>")
            mock_call.assert_not_called()

    @patch('commandgpt.getPromptedLLMChain')
    @patch('commandgpt.get_input', return_value='y')
    @patch('subprocess.call')
    def test_question_with_run_flag(self, mock_call, mock_input, mock_llm):
        mock_llm.return_value = self.agent
        question = "How to list all files in a directory?"
        args = ['-q', question, '-r']
        parsed_args = parse_arguments(args)

        main(parsed_args)
        mock_call.assert_called_with("<generated_bash_command>", shell=True)
        
    @patch('commandgpt.getPromptedLLMChain')
    @patch('commandgpt.get_input', return_value='n')
    @patch('subprocess.call')
    def test_question_with_run_flag_user_cancels(self, mock_call, mock_input, mock_llm):
        mock_llm.return_value = self.agent
        question = "How to list all files in a directory?"
        args = ['-q', question, '-r']
        parsed_args = parse_arguments(args)

        main(parsed_args)
        mock_call.assert_not_called()

if __name__ == '__main__':
    unittest.main()

