"""Unit tests for custom exceptions."""
import pytest
from exceptions import (
    PromptTooLongError,
    DimensionTooSmallError,
    NoImagesGeneratedError,
    ImageGenerationError,
    APIError,
)


class TestCustomExceptions:
    """Test suite for custom exception classes."""

    def test_prompt_too_long_error(self):
        """Test PromptTooLongError can be raised and caught."""
        with pytest.raises(PromptTooLongError):
            raise PromptTooLongError()

    def test_dimension_too_small_error(self):
        """Test DimensionTooSmallError can be raised and caught."""
        with pytest.raises(DimensionTooSmallError):
            raise DimensionTooSmallError()

    def test_no_images_generated_error(self):
        """Test NoImagesGeneratedError can be raised and caught."""
        with pytest.raises(NoImagesGeneratedError):
            raise NoImagesGeneratedError()

    def test_api_error(self):
        """Test APIError can be raised and caught."""
        with pytest.raises(APIError):
            raise APIError()

    def test_image_generation_error_with_message(self):
        """Test ImageGenerationError stores message and model index."""
        error = ImageGenerationError("Test error message", model_index=2)
        assert str(error) == "Test error message"
        assert error.model_index == 2

    def test_image_generation_error_defaults(self):
        """Test ImageGenerationError defaults model_index to 0."""
        error = ImageGenerationError("Test")
        assert error.model_index == 0

    def test_prompt_too_long_error_inheritance(self):
        """Test PromptTooLongError inherits from AppCommandError."""
        assert issubclass(PromptTooLongError, Exception)

    def test_dimension_too_small_error_inheritance(self):
        """Test DimensionTooSmallError inherits from AppCommandError."""
        assert issubclass(DimensionTooSmallError, Exception)
