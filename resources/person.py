from flask_restful import Resource
from models.person import PersonModel


class PersonRegister(Resource):

    def post(self):

        ## need to connect this to the chatbot
        # data = UserRegister.parser.parse_args()
        data = {'person_name': "Jim", 'phone_number': "12345678"}

        if PersonModel.find_by_name(data['person_name']):
            return {"message": "A person with that name already exists"}, 400

        person = PersonModel(data['person_name'], data['phone_number'])
        person.save_to_db()

        return {"message": "Person created successfully."}, 201