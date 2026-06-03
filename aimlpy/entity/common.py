from pydantic import BaseModel


# ── Generic success/error response ───────────────────────────────────────────
class SuccessResponse(BaseModel):
    message: str
    success: bool = True


class ErrorResponse(BaseModel):
    message: str
    success: bool = False