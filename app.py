import uvicorn
from fastapi import FastAPI

app = FastAPI()


simple_res = [
    {"alfa": "beta"},
    {"gamma": "delta"},
    {"epsilon": "zeta"},
    {"eta": "theta"},
    {"iota": "kappa"},
    {"lambda": "mu"},
    {"nu": "xi"},
    {"omicron": "pi"},
    {"rho": "sigma"},
    {"tau": "upsilon"},
    {"phi": "chi"},
    {"psi": "omega"},
    {"digamma": "san"}
]


@app.get("/")
def hello_world():
    return simple_res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
