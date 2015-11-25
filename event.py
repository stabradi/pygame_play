def Event:
    def __init__(self):
        self.listeners = []
    def subscribe(self, handler):
        self.listeners.append(handler)
    def publish(self,event=None):
        for l in self.listeners:
            l(event)
