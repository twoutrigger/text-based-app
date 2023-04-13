from flask_restful import Resource
from models.question import QuestionModel


class Question(Resource):
    def get(self, name):
        question = QuestionModel.find_by_name(name)
        if question:
            return question.json()
        return {'message': 'Question not found; add question using POST'}, 404

    def post(self, name):
        if QuestionModel.find_by_name(name):
            return {'message': "A question with name {} already exists.".format(name)}, 400

        question = QuestionModel(name)
        try:
            question.save_to_db()
        except:
            return {"message": "An error occurred creating the question."}, 500

        return question.json(), 201
    
    def delete(self, name):
        question = QuestionModel.find_by_name(name)
        if question:
            question.delete_from_db()

        return {'message': "A question with name {} is deleted".format(name)}, 200


class QuestionList(Resource):
    def get(self):
        return {'questions': list(map(lambda x: x.json(), QuestionModel.query.all()))}