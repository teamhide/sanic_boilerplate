class Converter:
    def __init__(self):
        pass

    def model_to_entity(self, model, entity):
        return entity(**model.to_dict())

    def entity_to_model(self, entity, model):
        return model(**entity.__dict__)

    def dto_to_dict(self, dto):
        return dto.__dict__
