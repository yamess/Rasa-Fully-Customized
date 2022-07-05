from engine.inference import predict_intent
from engine.train import train_horoscope_bot
import asyncio

if __name__ == "__main__":
    train_horoscope_bot(
        domain_path="domain.yml",
        config_path="config.yml",
        nlu_data_path="data/",
        model_to_fine_tune="models/20220627-210523-freezing-faucet.tar.gz"
    )
    # asyncio.run(predict_intent(text="Hi", model_path="models"))
