# FastAPI dependency-injection providers.
# get_db(): yields a SQLAlchemy AsyncSession per request.
# get_vector_client(): returns a singleton Qdrant AsyncClient.
# get_current_user(): validates JWT and returns the AuthUser (week 6).
# get_analyst_user(): depends on get_current_user, asserts role in {admin, analyst}.
