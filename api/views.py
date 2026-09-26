from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

"""
API endpoint definitions for the Resume Assistant backend.

Handles requests for resumes, job postings, and analysis.
Updated 9.24.2026
Author: AndyVR
"""

@api_view(["GET"])
def health_check(request):
    return Response({
        "status": "success",
        "message": "Resume Assistant Backend is running!"
    })


@api_view(["POST"])
def test_connection(request):
    message = request.data.get("message")

    if not message:
        return Response(
            {
                "status": "error",
                "message": "A message is required."
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response({
        "status": "success",
        "received": message,
        "response": "Django backend received the POST request."
    })
