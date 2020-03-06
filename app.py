from os.path import dirname, join
from ariadne import QueryType
from ariadne.asgi import GraphQL

from ariadne_extensions import federation

query_type = QueryType()
manager = federation.FederatedManager(
    schema_sdl_file=join(dirname(__file__), 'schema.graphql'),
    query=query_type,
)


class User:
    id = "45AOE5U6AU452E5A8"
    userId = "UHOH45"
    email = "me@test.com"
    firstName = "Brent"
    lastName = "Weeks"


@query_type.field('me')
def resolve_me(*_):
    return User()


user_type = federation.FederatedObjectType('User')


@user_type.resolve_reference
def resolve_reference(presentation, *_):
    return User()


manager.add_types(user_type)

schema = manager.get_schema()

app = GraphQL(schema, debug=True)
