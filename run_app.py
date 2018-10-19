from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-459588579221-459221765748-460475051943-26b411bae77c79a02d92b605bb6f0837', #app verification token
							'xoxb-459588579221-459324807507-X3W6RLvcR8YZOZRJjHrKr0WB', # bot verification token
							'So8OQlX74957owMFUXWQW2hJ', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))