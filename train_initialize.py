from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.sklearn_policy import SklearnPolicy

if __name__=='__main__':
    utils.configure_colored_logging(loglevel="DEBUG")

    training_data_file = './data/stories.md'
    model_path = './models/dialogue'
    agent = Agent("horoscope_domain.yml",policies=[MemoizationPolicy(max_history = 2),KerasPolicy()])
    training_data = agent.load_data(training_data_file)
    agent.train(training_data)
    agent.persist(model_path)