import json

from flask_restplus import Resource, fields, Namespace
from flask_restplus.errors import abort


ns = Namespace(
    "missingdata",
    description=""
)

response = ns.model(
    "phishing_data",
    {
        "PopUpWindow": fields.Integer,
        "SubmitInfoToEmail": fields.Integer,
        "IframeOrFrame": fields.Integer,
        "MissingTitle": fields.Integer,
        "ImagesOnlyInForm": fields.Integer,
        "SubdomainLevelRT": fields.Integer,
        "UrlLengthRT": fields.Integer,
        "PctExtResourceUrlsRT": fields.Integer,
        "AbnormalExtFormActionR": fields.Integer,
        "ExtMetaScriptLinkRT": fields.Integer,
        "PctExtNullSelfRedirectHyperlinksRT": fields.Integer,
        "CLASS_LABEL": fields.Integer,
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
