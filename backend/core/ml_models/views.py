from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.ml_models.ml.recommendation_model import RecommendationModel

class ProductRecommendationView(APIView):
    def get(self, request, product_id):
        review_text = request.query_params.get('features')

        if not review_text:
            return Response(
                {"error": "Review text is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            model = RecommendationModel()
            model.load_model()

            prediction = model.predict(review_text)

            return Response({'prediction': prediction[0]}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"Error in parsing or predicting: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
