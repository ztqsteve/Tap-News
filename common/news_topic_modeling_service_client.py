import pyjsonrpc

URL = "http://localhost:6060"

client = pyjsonrpc.HttpClient(url=URL)

def classify(text):
    topic = client.classify(text)
    print("Topic: %s" % str(topic))
    return topic
