from fastapi import FastAPI

app=FastAPI(title="Floorplan AI")

@app.get("/")
def root():
    return {"status":"ok"}
