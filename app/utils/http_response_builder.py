from fastapi.responses import JSONResponse


class HttpResponseBuilder:

    @classmethod
    async def build_success_response(cls, data: dict, meta: dict = {}, status_code: int = 200):
        response = {
            'data': data,
            'meta': meta,
            'success': True,
            'status_code': status_code
        }
        return JSONResponse(response)

    @classmethod
    async def build_error_response(cls, message, status_code=400):
        response = {
            "error": [{"message": message}],
            "success": False,
            "status_code": status_code,
        }
        return JSONResponse(response, status_code=status_code)
