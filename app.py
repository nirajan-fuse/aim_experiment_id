import sqlite3

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/api")
async def get_experiment_id(exp_name: str):
    conn = sqlite3.connect(".aim/run_metadata.sqlite")
    cursor = conn.cursor()

    query = """
    SELECT DISTINCT uuid 
    FROM experiment 
    WHERE name = ?
    """

    cursor.execute(query, (exp_name,))
    result = cursor.fetchone()

    if result is None:
        uuid = None
    else:
        uuid = result[0]

    conn.close()

    return {"experiment-id": uuid}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
