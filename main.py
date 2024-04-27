import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from models.UserbotModels.UserbotModel import UserbotModel
from routes.CandidateRoutes.candidate import candidate_router
from routes.CandidateVacancyRoutes.candidate_vacancy import candidate_vacancy_router
from routes.CandidateRoutes.candidates import candidates_router
from routes.PDFRoutes.pdf import pdf_router
from routes.UserbotRoutes.userbot import userbot_router
from routes.VacancyRoutes.vacancies import vacancies_router
from routes.VacancyRoutes.vacancy import vacancy_router
from userbot.userbot import init_message

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vacancy_router)
app.include_router(candidate_router)
app.include_router(pdf_router)
app.include_router(candidates_router)
app.include_router(vacancies_router)
app.include_router(candidate_vacancy_router)
app.include_router(userbot_router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Gigachat HR",
        version="1.0.00",
        summary="Gigachat HR - API для упрощения работы HR",
        # description="",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5.9.0/swagger-ui.css",
    )


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
