import json

from flask_restplus import Resource, fields, Namespace
from flask_restplus.errors import abort

# Timestamp,RSI10,%K200,%K30,EMA10


ns = Namespace(
    "christmas_data",
    description=""
)

response = ns.model(
    "christmas_data",
    {
        "Timestamp": fields.Integer,
        "RSI10": fields.Float,
        "%K200": fields.Float,
        "%K30": fields.Float,
        "EMA10": fields.Float,
    }
)


with open('data.json') as json_file:
    data = json.load(json_file)


@ns.route("/<webpage_id>")
@ns.param("webpage_id", "Webpage id")
class UserResource(Resource):
    @ns.marshal_with(response)
    def get(self, webpage_id):
        try:
            return data[webpage_id]
        except Exception:
            abort(code=404, message="Webpage id not found")
