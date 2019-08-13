from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase.load("knowledge_base_data.json")

        knowledge_base.set_representation_function_of_object(
            "hotel", lambda obj: obj["name"] + " (" + obj["city"] + ")"
        )

        super().__init__(knowledge_base)
