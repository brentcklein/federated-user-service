from os.path import dirname, join
from ariadne import QueryType, load_schema_from_path
from ariadne.asgi import GraphQL

from ariadne.contrib.federation import FederatedObjectType, make_federated_schema

query_type = QueryType()


class User:
    id = "45AOE5U6AU452E5A8"
    userId = "UHOH45"
    email = "me@test.com"
    firstName = "Brent"
    lastName = "Weeks"


@query_type.field('me')
def resolve_me(*_):
    return User()


user_type = FederatedObjectType('User')


@user_type.reference_resolver
def resolve_reference(_, _info, representation):
    return User()


type_defs = load_schema_from_path('schema.graphql')
schema = make_federated_schema(type_defs, query_type, user_type)

app = GraphQL(schema, debug=True)
