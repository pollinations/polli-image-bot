from config import initialize_models_async, ALLOWED_MODELS
from utils.logger import discord_logger


async def fetch_and_log_models(config, action: str) -> None:
    """
    Fetch models from API and update config with proper logging.

    Args:
        config: Configuration instance to update
        action: Action name for logging (e.g., "model_refresh", "async_model_init")
    """
    try:
        # Fetch new models from API
        models = await initialize_models_async(config)

        # Filter to only allowed models
        filtered_models = [model for model in models if model in ALLOWED_MODELS]

        # Update config with new models (clear and extend to maintain reference)
        config.MODELS.clear()
        config.MODELS.extend(filtered_models if filtered_models else [config.image_generation.fallback_model])

        # Log successful operation
        discord_logger.log_bot_event(
            action=action,
            status="success",
            details=f"Models {action.replace('_', ' ')}: {filtered_models}",
        )

    except Exception as e:
        # Fallback to single fallback model on error
        fallback = config.image_generation.fallback_model
        config.MODELS.clear()
        config.MODELS.append(fallback)

        # Log error with context
        discord_logger.log_error(
            error_type=f"{action}_error",
            error_message=str(e),
            traceback=None,
            context={"fallback_model": fallback},
        )
