from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parents[2]

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

router = APIRouter(
    tags=["Pages"]
)


@router.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "PocketSmart AI",
        },
    )


@router.get("/login", include_in_schema=False)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "title": "Login - PocketSmart AI",
        },
    )


@router.get("/register", include_in_schema=False)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={
            "title": "Register - PocketSmart AI",
        },
    )


@router.get("/dashboard", include_in_schema=False)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "title": "Dashboard - PocketSmart AI",
        },
    )


@router.get("/home-planner", include_in_schema=False)
def home_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home_planner.html",
        context={
            "title": "Home Planner - PocketSmart AI",
        },
    )


@router.get("/party-planner", include_in_schema=False)
def party_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="party_planner.html",
        context={
            "title": "Party Planner - PocketSmart AI",
        },
    )


@router.get("/jewelry-planner", include_in_schema=False)
def jewelry_planner(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={
            "title": "Jewelry Planner - PocketSmart AI",
        },
    )