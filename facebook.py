from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig
# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/default/horoscopebot/")
MODEL_PATH = "models/dialog"
action_endpoint = EndpointConfig(url="https://horoscopebot2105.herokuapp.com/webhook")
agent = Agent.load(MODEL_PATH, interpreter=interpreter)
input_channel = FacebookInput(
        fb_verify="this_is_sparta",
        fb_secret="28c8e3b3f240d2d3c7d05cc5fee7706d",
        fb_access_token="EAAKfRRrqZCqsBAOGV6NwxzSz3bUV5RGsLFIztsYG5VCQIf2OaEkWUcMXosISDQu8u27q9m3MGSaHJ8VssZBR4ogZBCadWbYEzlCzZCVZCk5EGBbwsLePeN827Ucy5NrZAxWgTiG5M7N12c1WiVYCv5QetLIZAvYZA2cFT2LwLYCGgaPQMUFsQsXk"

)

s = agent.handle_channels([input_channel], int(os.environ.get('PORT',
5004)), serve_forever=True)