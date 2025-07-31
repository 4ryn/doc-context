from fastapi import FastAPI
from app.api.v1.webhook import router

# Create FastAPI app
app = FastAPI(
    title="Webhook API", 
    version="1.0.0",
    description="HackRX Webhook API"
)

# Include your webhook routes
app.include_router(router, prefix="/api/v1")

# Health check endpoints
@app.get("/")
def root():
    return {"message": "Webhook API is running", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "webhook-api"}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)