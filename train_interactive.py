import logging

from rasa_core import utils,train
from rasa_core.training import interactive
from rasa_core.interpreter import NaturalLanguageInterpreter

logger = logging.getLogger(__name__)

def train_agent():
    return train.train_dialogue_model(domain_file="horoscope_domain.yml",
                    stories_file="data/stories.md",
                    output_path="models/dialogue",
                    policy_config='policy_config.yml')
if __name__=='__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
    nlu_model_path = "./models/nlu/default/horoscopebot/"
    interpreter = NaturalLanguageInterpreter.create(nlu_model_path)
    agent = train_agent()
    interactive.run_interactive_learning(agent)




