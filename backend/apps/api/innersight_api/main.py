# FastAPI app factory.
# Creates the FastAPI() instance, registers all routers (health, auth, users,
# suspects, investigations), configures CORS using CORS_ORIGINS from env,
# and wires up the OpenAPI schema at /docs.
