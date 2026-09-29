import base64
import hashlib
import hmac
import json
import time

from .config import get_settings


def hash_password(password: str) -> str:
    """Hash a password using PBKDF2-HMAC-SHA256."""

    salt = hashlib.sha256(
        str(time.time_ns()).encode()
    ).hexdigest()[:32]

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        200_000,
    ).hex()

    return f"pbkdf2_sha256$200000${salt}${password_hash}"


def verify_password(
    password: str,
    stored_hash: str,
) -> bool:

    try:
        algorithm, iterations, salt, expected_hash = (
            stored_hash.split("$")
        )

        if algorithm != "pbkdf2_sha256":
            return False

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt.encode("utf-8"),
            int(iterations),
        ).hex()

        return hmac.compare_digest(
            password_hash,
            expected_hash,
        )

    except (ValueError, TypeError):
        return False


def _urlsafe_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def _urlsafe_decode(data: str) -> bytes:
    padding = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(
        data + padding
    )


def create_access_token(user_id: str) -> str:
    """Create a signed access token."""

    settings = get_settings()

    header = {
        "alg": "HS256",
        "typ": "JWT",
    }

    payload = {
        "sub": str(user_id),
        "exp": int(time.time())
        + (
            settings.access_token_expire_minutes
            * 60
        ),
    }

    header_part = _urlsafe_encode(
        json.dumps(
            header,
            separators=(",", ":"),
        ).encode()
    )

    payload_part = _urlsafe_encode(
        json.dumps(
            payload,
            separators=(",", ":"),
        ).encode()
    )

    message = (
        f"{header_part}.{payload_part}"
    ).encode()

    signature = hmac.new(
        settings.secret_key.encode(),
        message,
        hashlib.sha256,
    ).digest()

    signature_part = _urlsafe_encode(
        signature
    )

    return (
        f"{header_part}."
        f"{payload_part}."
        f"{signature_part}"
    )


def decode_access_token(token: str) -> dict | None:
    """Verify and decode an access token."""

    try:
        header_part, payload_part, signature_part = (
            token.split(".")
        )

        message = (
            f"{header_part}.{payload_part}"
        ).encode()

        expected_signature = hmac.new(
            get_settings().secret_key.encode(),
            message,
            hashlib.sha256,
        ).digest()

        actual_signature = _urlsafe_decode(
            signature_part
        )

        if not hmac.compare_digest(
            actual_signature,
            expected_signature,
        ):
            return None

        payload = json.loads(
            _urlsafe_decode(
                payload_part
            )
        )

        if payload.get("exp", 0) < int(time.time()):
            return None

        if not payload.get("sub"):
            return None

        return payload

    except (
        ValueError,
        TypeError,
        json.JSONDecodeError,
    ):
        return None