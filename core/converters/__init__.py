class Converter:
    def __init__(self):
        pass

    def model_to_entity(self, model, entity):
        return entity(**model.to_dict())

    def entity_to_model(self, entity, model):
        return model(**entity.__dict__)
