from os.path import dirname, join
from ariadne import QueryType, ObjectType, load_schema_from_path
from ariadne.asgi import GraphQL

from ariadne.contrib.federation import FederatedObjectType, make_federated_schema

user_type = FederatedObjectType('User')


@user_type.field('id')
def resolve_id(*_):
    return "some stuff"


@user_type.field('fullName')
def resolve_fullname(obj, *_):
    return "Full Name"


type_defs = load_schema_from_path('schema.graphql')
schema = make_federated_schema(type_defs, user_type)

app = GraphQL(schema, debug=True)
