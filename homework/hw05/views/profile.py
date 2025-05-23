import json

from flask import Response, request
from flask_restful import Resource

from models.user import User


def get_path():
    return request.host_url + "api/posts/"


class ProfileDetailEndpoint(Resource):

    def __init__(self, current_user):
        self.current_user = current_user

    def get(self):
        # TODO: Add GET logic...

        # TODO: add the ability to handle the "limit" query parameter:

        # data = [item.to_dict(user=self.current_user) for item in profile]
        return Response(json.dumps(self.current_user.to_dict()), mimetype="application/json", status=200)

        # return Response(
        #     json.dumps({}),
        #     mimetype="application/json",
        #     status=200,
        # )


def initialize_routes(api, current_user):
    api.add_resource(
        ProfileDetailEndpoint,
        "/api/profile",
        "/api/profile/",
        resource_class_kwargs={"current_user": current_user},
    )
