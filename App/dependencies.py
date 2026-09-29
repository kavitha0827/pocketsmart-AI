from fastapi import (
    Cookie,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy import select
from sqlalchemy.orm import Session

from .auth import decode_access_token
from .database import get_db
from .models import User


def get_current_user(
    access_token: str | None = Cookie(
        default=None
    ),
    db: Session = Depends(get_db),
) -> User:

    if not access_token:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    payload = decode_access_token(
        access_token
    )

    if not payload:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    try:

        user_id = int(
            payload["sub"]
        )

    except (
        KeyError,
        TypeError,
        ValueError,
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    user = db.scalar(
        select(User).where(
            User.id == user_id
        )
    )

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user