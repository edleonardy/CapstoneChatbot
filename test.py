from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
message = "can you tell me about the course c13022?"
result = interpreter.parse(message)
print(json.dumps(result, indent=2))